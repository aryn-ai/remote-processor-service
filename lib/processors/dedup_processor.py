import re
import sys
import json
from sycamore.functions.simhash import shinglesDist
from lib.processors.processor import RequestProcessor, ResponseProcessor
from lib.search_request import SearchRequest
from lib.search_response import SearchResponse

class DedupResponseProcessor(ResponseProcessor):
    nulRe = re.compile(rb'\x00+$')
    
    def __init__(self, threshold: float, verbose: int) -> None:
        super().__init__()
        self.threshold = threshold
        self.verbose = verbose

    @staticmethod
    def from_config(config) -> ResponseProcessor:
        t = config["threshold"]
        v = config.get("verbose", 0)
        return DedupResponseProcessor(threshold=t, verbose=v)

    @staticmethod
    def get_class_name() -> str:
        return "dedup-response"

    def process_response(self, req: SearchRequest, resp: SearchResponse) -> SearchResponse:
        try:
            hitAry = resp.internal_response.hits.hits
            n = len(hitAry)
        except AttributeError:
            n = 0
        if n == 0:
            return resp

        validAry = [True] * n
        sketchAry = []
        for i, hit in enumerate(hitAry):
            try:
                raw_i = hit.source
                raw_i = self.nulRe.sub(b"", raw_i)  # FIXME: Issue #3
                obj_i = json.loads(raw_i)
                # !!! must ask for shingles and text_representation in query
                sketch_i = obj_i.get("shingles")
                text_i = obj_i.get("text_representation", "")
            except (AttributeError, KeyError):
                sketch_i = None
                text_i = ""
            sketchAry.append(sketch_i)
            if sketch_i is None:
                continue
            for j in range(i):
                if not validAry[j]:
                    continue
                sketch_j = sketchAry[j]
                if sketch_j is None:
                    continue
                dist = shinglesDist(sketch_i, sketch_j)
                if dist < self.threshold:
                    validAry[i] = False
                    if self.verbose:
                        try:
                            raw_j = hitAry[j].source
                            raw_j = self.nulRe.sub(b"", raw_j)  # FIXME: #3
                            obj_j = json.loads(raw_j)
                            text_j = obj_j.get("text_representation", "")
                            print("DROP", dist, file=sys.stderr)
                            print("PREV", text_j, file=sys.stderr)
                            print("CURR", text_i, file=sys.stderr)
                        except (AttributeError, KeyError):
                            pass
                    break

        del sketchAry
        newAry = []
        if not self.verbose:
            for valid, hit in zip(validAry, hitAry):
                if valid:
                    newAry.append(hit)
        else:
            for valid, hit in zip(validAry, hitAry):
                try:
                    raw = hit.source
                    raw = self.nulRe.sub(b"", raw)  # FIXME: Issue #3
                    obj = json.loads(raw)
                    props = obj["properties"]
                    fn = props.get("_location")
                    if fn is None:
                        fn = props["path"]
                    pn = props.get("page_number", 0)
                    name = fn + " " + str(pn)
                except (AttributeError, KeyError):
                    name = "None 0"
                if valid:
                    newAry.append(hit)
                    print("KEEP", name, file=sys.stderr)
                else:
                    print("NUKE", name, file=sys.stderr)
        resp.internal_response.hits.total_hits.value = len(newAry)
        del resp.internal_response.hits.hits[:]
        resp.internal_response.hits.hits.extend(newAry)
        return resp
