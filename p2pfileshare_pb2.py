# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: p2pfileshare.proto
# Protobuf Python Version: 4.25.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x12p2pfileshare.proto\x12\x0cp2pfileshare\"\x12\n\x10ListFilesRequest\"&\n\x11ListFilesResponse\x12\x11\n\tfilenames\x18\x01 \x03(\t\"\'\n\x13\x44ownloadFileRequest\x12\x10\n\x08\x66ilename\x18\x01 \x01(\t\"\'\n\x14\x44ownloadFileResponse\x12\x0f\n\x07message\x18\x01 \x01(\t\"%\n\x11UploadFileRequest\x12\x10\n\x08\x66ilename\x18\x01 \x01(\t\"%\n\x12UploadFileResponse\x12\x0f\n\x07message\x18\x01 \x01(\t2\x88\x02\n\x10\x46ileShareService\x12L\n\tListFiles\x12\x1e.p2pfileshare.ListFilesRequest\x1a\x1f.p2pfileshare.ListFilesResponse\x12U\n\x0c\x44ownloadFile\x12!.p2pfileshare.DownloadFileRequest\x1a\".p2pfileshare.DownloadFileResponse\x12O\n\nUploadFile\x12\x1f.p2pfileshare.UploadFileRequest\x1a .p2pfileshare.UploadFileResponseb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'p2pfileshare_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  DESCRIPTOR._options = None
  _globals['_LISTFILESREQUEST']._serialized_start=36
  _globals['_LISTFILESREQUEST']._serialized_end=54
  _globals['_LISTFILESRESPONSE']._serialized_start=56
  _globals['_LISTFILESRESPONSE']._serialized_end=94
  _globals['_DOWNLOADFILEREQUEST']._serialized_start=96
  _globals['_DOWNLOADFILEREQUEST']._serialized_end=135
  _globals['_DOWNLOADFILERESPONSE']._serialized_start=137
  _globals['_DOWNLOADFILERESPONSE']._serialized_end=176
  _globals['_UPLOADFILEREQUEST']._serialized_start=178
  _globals['_UPLOADFILEREQUEST']._serialized_end=215
  _globals['_UPLOADFILERESPONSE']._serialized_start=217
  _globals['_UPLOADFILERESPONSE']._serialized_end=254
  _globals['_FILESHARESERVICE']._serialized_start=257
  _globals['_FILESHARESERVICE']._serialized_end=521
# @@protoc_insertion_point(module_scope)
