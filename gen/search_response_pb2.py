# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: gen/search_response.proto
# Protobuf Python Version: 4.25.0
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x19gen/search_response.proto\"\xe9\x02\n\x0eSearchResponse\x12\x32\n\x11internal_response\x18\x01 \x01(\x0b\x32\x17.SearchResponseSections\x12\x16\n\tscroll_id\x18\x02 \x01(\tH\x00\x88\x01\x01\x12\x1d\n\x10point_in_time_id\x18\x03 \x01(\tH\x01\x88\x01\x01\x12\x14\n\x0ctotal_shards\x18\x04 \x01(\x05\x12\x19\n\x11successful_shards\x18\x05 \x01(\x05\x12\x16\n\x0eskipped_shards\x18\x06 \x01(\x05\x12+\n\x0eshard_failures\x18\x07 \x03(\x0b\x32\x13.SearchShardFailure\x12\x1b\n\x08\x63lusters\x18\x08 \x01(\x0b\x32\t.Clusters\x12\x16\n\x0etook_in_millis\x18\t \x01(\x03\x12\x1e\n\nphase_took\x18\n \x01(\x0b\x32\n.PhaseTookB\x0c\n\n_scroll_idB\x13\n\x11_point_in_time_id\"H\n\x12SearchShardFailure\x12\x0e\n\x06reason\x18\x01 \x01(\t\x12\"\n\x06target\x18\x02 \x01(\x0b\x32\x12.SearchShardTarget\"H\n\x11SearchShardTarget\x12\x10\n\x08shard_id\x18\x01 \x01(\t\x12\x10\n\x08index_id\x18\x02 \x01(\t\x12\x0f\n\x07node_id\x18\x03 \x01(\t\">\n\x08\x43lusters\x12\r\n\x05total\x18\x01 \x01(\x05\x12\x12\n\nsuccessful\x18\x02 \x01(\x05\x12\x0f\n\x07skipped\x18\x03 \x01(\x05\"v\n\tPhaseTook\x12\x34\n\x0ephase_took_map\x18\x01 \x03(\x0b\x32\x1c.PhaseTook.PhaseTookMapEntry\x1a\x33\n\x11PhaseTookMapEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\x03:\x02\x38\x01\"\x98\x02\n\x16SearchResponseSections\x12\x19\n\x04hits\x18\x01 \x01(\x0b\x32\x0b.SearchHits\x12#\n\x0c\x61ggregations\x18\x02 \x01(\x0b\x32\r.Aggregations\x12\x19\n\x07suggest\x18\x03 \x01(\x0b\x32\x08.Suggest\x12\x33\n\x0fprofile_results\x18\x04 \x01(\x0b\x32\x1a.SearchProfileShardResults\x12\x11\n\ttimed_out\x18\x05 \x01(\x08\x12\x18\n\x10terminated_early\x18\x06 \x01(\x08\x12\x19\n\x11num_reduce_phases\x18\x07 \x01(\x05\x12&\n\x0bsearch_exts\x18\x08 \x03(\x0b\x32\x11.SearchExtBuilder\"\xa2\x01\n\nSearchHits\x12\x1e\n\ntotal_hits\x18\x01 \x01(\x0b\x32\n.TotalHits\x12\x18\n\x04hits\x18\x02 \x03(\x0b\x32\n.SearchHit\x12\x11\n\tmax_score\x18\x03 \x01(\x02\x12\x1b\n\x0e\x63ollapse_field\x18\x05 \x01(\tH\x00\x88\x01\x01\x12\x17\n\x0f\x63ollapse_values\x18\x06 \x03(\x0c\x42\x11\n\x0f_collapse_field\"y\n\tTotalHits\x12\r\n\x05value\x18\x01 \x01(\x03\x12%\n\x08relation\x18\x02 \x01(\x0e\x32\x13.TotalHits.Relation\"6\n\x08Relation\x12\x0c\n\x08\x45QUAL_TO\x10\x00\x12\x1c\n\x18GREATER_THAN_OR_EQUAL_TO\x10\x01\"\x8a\x06\n\tSearchHit\x12\x0e\n\x06\x64oc_id\x18\x01 \x01(\x05\x12\r\n\x05score\x18\x02 \x01(\x02\x12\n\n\x02id\x18\x03 \x01(\t\x12\"\n\tnested_id\x18\x04 \x01(\x0b\x32\x0f.NestedIdentity\x12\x0f\n\x07version\x18\x05 \x01(\x03\x12\x0e\n\x06seq_no\x18\x06 \x01(\x03\x12\x14\n\x0cprimary_term\x18\x07 \x01(\x03\x12\x0e\n\x06source\x18\x08 \x01(\x0c\x12\x37\n\x0f\x64ocument_fields\x18\t \x03(\x0b\x32\x1e.SearchHit.DocumentFieldsEntry\x12/\n\x0bmeta_fields\x18\n \x03(\x0b\x32\x1a.SearchHit.MetaFieldsEntry\x12\x39\n\x10highlight_fields\x18\x0b \x03(\x0b\x32\x1f.SearchHit.HighlightFieldsEntry\x12&\n\x0bsort_values\x18\x0c \x01(\x0b\x32\x11.SearchSortValues\x12\x17\n\x0fmatched_queries\x18\r \x03(\t\x12!\n\x05shard\x18\x0e \x01(\x0b\x32\x12.SearchShardTarget\x12\r\n\x05index\x18\x0f \x01(\t\x12\x14\n\x0c\x63lusterAlias\x18\x10 \x01(\t\x12\x32\n\rsource_as_map\x18\x11 \x03(\x0b\x32\x1b.SearchHit.SourceAsMapEntry\x1a\x45\n\x13\x44ocumentFieldsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\x1d\n\x05value\x18\x02 \x01(\x0b\x32\x0e.DocumentField:\x02\x38\x01\x1a\x41\n\x0fMetaFieldsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\x1d\n\x05value\x18\x02 \x01(\x0b\x32\x0e.DocumentField:\x02\x38\x01\x1aG\n\x14HighlightFieldsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\x1e\n\x05value\x18\x02 \x01(\x0b\x32\x0f.HighlightField:\x02\x38\x01\x1a\x32\n\x10SourceAsMapEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\x0c:\x02\x38\x01\"O\n\x0eNestedIdentity\x12\r\n\x05\x66ield\x18\x01 \x01(\t\x12\x0e\n\x06offset\x18\x02 \x01(\x05\x12\x1e\n\x05\x63hild\x18\x03 \x01(\x0b\x32\x0f.NestedIdentity\"-\n\rDocumentField\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x0e\n\x06values\x18\x02 \x03(\x0c\"1\n\x0eHighlightField\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x11\n\tfragments\x18\x02 \x03(\t\"J\n\x10SearchSortValues\x12\x1d\n\x15\x66ormatted_sort_values\x18\x01 \x03(\x0c\x12\x17\n\x0fraw_sort_values\x18\x02 \x03(\x0c\"$\n\x0c\x41ggregations\x12\x14\n\x0c\x61ggregations\x18\x01 \x01(\x0c\"\x1e\n\x07Suggest\x12\x13\n\x0bsuggestions\x18\x01 \x01(\x0c\",\n\x19SearchProfileShardResults\x12\x0f\n\x07results\x18\x01 \x01(\x0c\"\'\n\x10SearchExtBuilder\x12\x13\n\x0bsearch_exts\x18\x01 \x01(\x0c\x42\x35\n\x1forg.opensearch.pb.action.searchB\x10PBSearchResponseP\x01\x62\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'gen.search_response_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  _globals['DESCRIPTOR']._options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\037org.opensearch.pb.action.searchB\020PBSearchResponseP\001'
  _globals['_PHASETOOK_PHASETOOKMAPENTRY']._options = None
  _globals['_PHASETOOK_PHASETOOKMAPENTRY']._serialized_options = b'8\001'
  _globals['_SEARCHHIT_DOCUMENTFIELDSENTRY']._options = None
  _globals['_SEARCHHIT_DOCUMENTFIELDSENTRY']._serialized_options = b'8\001'
  _globals['_SEARCHHIT_METAFIELDSENTRY']._options = None
  _globals['_SEARCHHIT_METAFIELDSENTRY']._serialized_options = b'8\001'
  _globals['_SEARCHHIT_HIGHLIGHTFIELDSENTRY']._options = None
  _globals['_SEARCHHIT_HIGHLIGHTFIELDSENTRY']._serialized_options = b'8\001'
  _globals['_SEARCHHIT_SOURCEASMAPENTRY']._options = None
  _globals['_SEARCHHIT_SOURCEASMAPENTRY']._serialized_options = b'8\001'
  _globals['_SEARCHRESPONSE']._serialized_start=30
  _globals['_SEARCHRESPONSE']._serialized_end=391
  _globals['_SEARCHSHARDFAILURE']._serialized_start=393
  _globals['_SEARCHSHARDFAILURE']._serialized_end=465
  _globals['_SEARCHSHARDTARGET']._serialized_start=467
  _globals['_SEARCHSHARDTARGET']._serialized_end=539
  _globals['_CLUSTERS']._serialized_start=541
  _globals['_CLUSTERS']._serialized_end=603
  _globals['_PHASETOOK']._serialized_start=605
  _globals['_PHASETOOK']._serialized_end=723
  _globals['_PHASETOOK_PHASETOOKMAPENTRY']._serialized_start=672
  _globals['_PHASETOOK_PHASETOOKMAPENTRY']._serialized_end=723
  _globals['_SEARCHRESPONSESECTIONS']._serialized_start=726
  _globals['_SEARCHRESPONSESECTIONS']._serialized_end=1006
  _globals['_SEARCHHITS']._serialized_start=1009
  _globals['_SEARCHHITS']._serialized_end=1171
  _globals['_TOTALHITS']._serialized_start=1173
  _globals['_TOTALHITS']._serialized_end=1294
  _globals['_TOTALHITS_RELATION']._serialized_start=1240
  _globals['_TOTALHITS_RELATION']._serialized_end=1294
  _globals['_SEARCHHIT']._serialized_start=1297
  _globals['_SEARCHHIT']._serialized_end=2075
  _globals['_SEARCHHIT_DOCUMENTFIELDSENTRY']._serialized_start=1814
  _globals['_SEARCHHIT_DOCUMENTFIELDSENTRY']._serialized_end=1883
  _globals['_SEARCHHIT_METAFIELDSENTRY']._serialized_start=1885
  _globals['_SEARCHHIT_METAFIELDSENTRY']._serialized_end=1950
  _globals['_SEARCHHIT_HIGHLIGHTFIELDSENTRY']._serialized_start=1952
  _globals['_SEARCHHIT_HIGHLIGHTFIELDSENTRY']._serialized_end=2023
  _globals['_SEARCHHIT_SOURCEASMAPENTRY']._serialized_start=2025
  _globals['_SEARCHHIT_SOURCEASMAPENTRY']._serialized_end=2075
  _globals['_NESTEDIDENTITY']._serialized_start=2077
  _globals['_NESTEDIDENTITY']._serialized_end=2156
  _globals['_DOCUMENTFIELD']._serialized_start=2158
  _globals['_DOCUMENTFIELD']._serialized_end=2203
  _globals['_HIGHLIGHTFIELD']._serialized_start=2205
  _globals['_HIGHLIGHTFIELD']._serialized_end=2254
  _globals['_SEARCHSORTVALUES']._serialized_start=2256
  _globals['_SEARCHSORTVALUES']._serialized_end=2330
  _globals['_AGGREGATIONS']._serialized_start=2332
  _globals['_AGGREGATIONS']._serialized_end=2368
  _globals['_SUGGEST']._serialized_start=2370
  _globals['_SUGGEST']._serialized_end=2400
  _globals['_SEARCHPROFILESHARDRESULTS']._serialized_start=2402
  _globals['_SEARCHPROFILESHARDRESULTS']._serialized_end=2446
  _globals['_SEARCHEXTBUILDER']._serialized_start=2448
  _globals['_SEARCHEXTBUILDER']._serialized_end=2487
# @@protoc_insertion_point(module_scope)
