import json

from gen.search_response_pb2 import SearchHit, SearchHits, SearchResponse, SearchResponseSections, SearchShardTarget, TotalHits

from lib.processors.dedup_processor import DedupResponseProcessor


def mkShingles(x: int):
    ary = []
    for i in range(16):
        ary.append(x & 1)
        x //= 2
    return ary


def mkJson(x: int):
    id = "%08x-%04x-%04x-%04x-%012x" % (x, x, x, x, x)
    txt = "The quick brown fox jumps over %d lazy dogs." % x
    d = {
        "doc_id": id,
        "parent_id": id,
        "type": "NarrativeText",
        "text_representation": txt,
        "elements": [],
        "properties": {
            "path": "%08x.pdf" % x,
            "page_number": x,
        },
        "shingles": mkShingles(x),
    }
    s = json.dumps(d, separators=(",", ":"))
    return s.encode("utf-8")


def mkHit(x: int):
    return SearchHit(
        doc_id=x,
        score=100 - (x / 100),
        id="%08x-%04x-%04x-%04x-%012x" % (x, x, x, x, x),
        version=-1,
        source=mkJson(x),
        shard=SearchShardTarget(
            shard_id="%x" % x,
            index_id="%x" % x,
            node_id="%022x" % x,
        ),
    )


def mkHitAry():
    return [
        mkHit(0),
        mkHit(1),
        mkHit(2),
        mkHit(3),
    ]


def mkHits():
    ary = mkHitAry()
    return SearchHits(
        total_hits=TotalHits(value=len(ary), relation=TotalHits.Relation.EQUAL_TO),
        hits=ary,
        max_score=1,
    )


def mkSearchResp():
    return SearchResponse(
        internal_response=SearchResponseSections(
            hits=mkHits(),
            num_reduce_phases=1,
        ),
        total_shards=2,
        successful_shards=2,
        took_in_millis=12,
    )


class TestDedupProcessor:

    def test_smoke(self):
        req = None
        resp = mkSearchResp()
        assert len(resp.internal_response.hits.hits) == 4
        cfg = {"threshold": 0.4}
        proc = DedupResponseProcessor.from_config(cfg)
        resp = proc.process_response(req, resp)
        assert len(resp.internal_response.hits.hits) == 3
