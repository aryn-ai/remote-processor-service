import re
import json
from sycamore.functions.simhash import shinglesDist
from lib.processors.processor import RequestProcessor, ResponseProcessor
from lib.search_request import SearchRequest
from lib.search_response import SearchResponse

class DedupResponseProcessor(ResponseProcessor):
    nulRe = re.compile(rb'\x00+$')
    
    def __init__(self, threshold: float) -> None:
        super().__init__()
        self.threshold = threshold

    @staticmethod
    def from_config(config) -> ResponseProcessor:
        return DedupResponseProcessor(threshold=config["threshold"])

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
                raw = hit.source
                raw = self.nulRe.sub(b"", raw)  # FIXME: bug
                obj = json.loads(raw)
                sketch_i = obj["shingles"]  # FIXME: must ask for shingles in q
            except (AttributeError, KeyError):
                sketch_i = None
            sketchAry.append(sketch_i)
            if sketch_i is None:
                continue
            for j in range(i):
                if not validAry[j]:
                    continue
                sketch_j = sketchAry[j]
                if sketch_j is None:
                    continue
                if shinglesDist(sketch_i, sketch_j) < self.threshold:
                    validAry[i] = False
                    break

        del sketchAry
        newAry = []
        for valid, hit in zip(validAry, hitAry):
            if valid:
                newAry.append(hit)
        del resp.internal_response.hits.hits[:]
        resp.internal_response.hits.hits.extend(newAry)
        return resp
