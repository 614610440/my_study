# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: test.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='test.proto',
  package='',
  syntax='proto3',
  serialized_pb=_b('\n\ntest.proto\"$\n\x07\x42\x61seMsg\x12\x19\n\x07msgType\x18\x01 \x01(\x0e\x32\x08.MsgType\"A\n\x08Test1Msg\x12\x19\n\x07msgType\x18\x01 \x01(\x0e\x32\x08.MsgType\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x0c\n\x04text\x18\x03 \x01(\t\"@\n\x08Test2Msg\x12\x19\n\x07msgType\x18\x01 \x01(\x0e\x32\x08.MsgType\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x0b\n\x03pwd\x18\x03 \x01(\t*>\n\x07MsgType\x12\x0f\n\x0b\x42\x61seMsgType\x10\x00\x12\x10\n\x0cTest1MsgType\x10\x01\x12\x10\n\x0cTest2MsgType\x10\x02\x62\x06proto3')
)
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

_MSGTYPE = _descriptor.EnumDescriptor(
  name='MsgType',
  full_name='MsgType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='BaseMsgType', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='Test1MsgType', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='Test2MsgType', index=2, number=2,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=185,
  serialized_end=247,
)
_sym_db.RegisterEnumDescriptor(_MSGTYPE)

MsgType = enum_type_wrapper.EnumTypeWrapper(_MSGTYPE)
BaseMsgType = 0
Test1MsgType = 1
Test2MsgType = 2



_BASEMSG = _descriptor.Descriptor(
  name='BaseMsg',
  full_name='BaseMsg',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='msgType', full_name='BaseMsg.msgType', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=14,
  serialized_end=50,
)


_TEST1MSG = _descriptor.Descriptor(
  name='Test1Msg',
  full_name='Test1Msg',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='msgType', full_name='Test1Msg.msgType', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='name', full_name='Test1Msg.name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='text', full_name='Test1Msg.text', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=52,
  serialized_end=117,
)


_TEST2MSG = _descriptor.Descriptor(
  name='Test2Msg',
  full_name='Test2Msg',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='msgType', full_name='Test2Msg.msgType', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='name', full_name='Test2Msg.name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='pwd', full_name='Test2Msg.pwd', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=119,
  serialized_end=183,
)

_BASEMSG.fields_by_name['msgType'].enum_type = _MSGTYPE
_TEST1MSG.fields_by_name['msgType'].enum_type = _MSGTYPE
_TEST2MSG.fields_by_name['msgType'].enum_type = _MSGTYPE
DESCRIPTOR.message_types_by_name['BaseMsg'] = _BASEMSG
DESCRIPTOR.message_types_by_name['Test1Msg'] = _TEST1MSG
DESCRIPTOR.message_types_by_name['Test2Msg'] = _TEST2MSG
DESCRIPTOR.enum_types_by_name['MsgType'] = _MSGTYPE

BaseMsg = _reflection.GeneratedProtocolMessageType('BaseMsg', (_message.Message,), dict(
  DESCRIPTOR = _BASEMSG,
  __module__ = 'test_pb2'
  # @@protoc_insertion_point(class_scope:BaseMsg)
  ))
_sym_db.RegisterMessage(BaseMsg)

Test1Msg = _reflection.GeneratedProtocolMessageType('Test1Msg', (_message.Message,), dict(
  DESCRIPTOR = _TEST1MSG,
  __module__ = 'test_pb2'
  # @@protoc_insertion_point(class_scope:Test1Msg)
  ))
_sym_db.RegisterMessage(Test1Msg)

Test2Msg = _reflection.GeneratedProtocolMessageType('Test2Msg', (_message.Message,), dict(
  DESCRIPTOR = _TEST2MSG,
  __module__ = 'test_pb2'
  # @@protoc_insertion_point(class_scope:Test2Msg)
  ))
_sym_db.RegisterMessage(Test2Msg)


# @@protoc_insertion_point(module_scope)
