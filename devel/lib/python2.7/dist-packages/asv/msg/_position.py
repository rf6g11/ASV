"""autogenerated by genpy from asv/position.msg. Do not edit."""
import sys
python3 = True if sys.hexversion > 0x03000000 else False
import genpy
import struct


class position(genpy.Message):
  _md5sum = "0ff27e09213a0df37db82ae00fb8aecd"
  _type = "asv/position"
  _has_header = False #flag to mark the presence of a Header object
  _full_text = """float32 X
float32 Y
float32 speed
float64 lat
float64 long
float64 time
int8 ValidGPSfix
int8 number_of_satellites

"""
  __slots__ = ['X','Y','speed','lat','long','time','ValidGPSfix','number_of_satellites']
  _slot_types = ['float32','float32','float32','float64','float64','float64','int8','int8']

  def __init__(self, *args, **kwds):
    """
    Constructor. Any message fields that are implicitly/explicitly
    set to None will be assigned a default value. The recommend
    use is keyword arguments as this is more robust to future message
    changes.  You cannot mix in-order arguments and keyword arguments.

    The available fields are:
       X,Y,speed,lat,long,time,ValidGPSfix,number_of_satellites

    :param args: complete set of field values, in .msg order
    :param kwds: use keyword arguments corresponding to message field names
    to set specific fields.
    """
    if args or kwds:
      super(position, self).__init__(*args, **kwds)
      #message fields cannot be None, assign default values for those that are
      if self.X is None:
        self.X = 0.
      if self.Y is None:
        self.Y = 0.
      if self.speed is None:
        self.speed = 0.
      if self.lat is None:
        self.lat = 0.
      if self.long is None:
        self.long = 0.
      if self.time is None:
        self.time = 0.
      if self.ValidGPSfix is None:
        self.ValidGPSfix = 0
      if self.number_of_satellites is None:
        self.number_of_satellites = 0
    else:
      self.X = 0.
      self.Y = 0.
      self.speed = 0.
      self.lat = 0.
      self.long = 0.
      self.time = 0.
      self.ValidGPSfix = 0
      self.number_of_satellites = 0

  def _get_types(self):
    """
    internal API method
    """
    return self._slot_types

  def serialize(self, buff):
    """
    serialize message into buffer
    :param buff: buffer, ``StringIO``
    """
    try:
      _x = self
      buff.write(_struct_3f3d2b.pack(_x.X, _x.Y, _x.speed, _x.lat, _x.long, _x.time, _x.ValidGPSfix, _x.number_of_satellites))
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(_x))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(_x))))

  def deserialize(self, str):
    """
    unpack serialized message in str into this message instance
    :param str: byte array of serialized message, ``str``
    """
    try:
      end = 0
      _x = self
      start = end
      end += 38
      (_x.X, _x.Y, _x.speed, _x.lat, _x.long, _x.time, _x.ValidGPSfix, _x.number_of_satellites,) = _struct_3f3d2b.unpack(str[start:end])
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e) #most likely buffer underfill


  def serialize_numpy(self, buff, numpy):
    """
    serialize message with numpy array types into buffer
    :param buff: buffer, ``StringIO``
    :param numpy: numpy python module
    """
    try:
      _x = self
      buff.write(_struct_3f3d2b.pack(_x.X, _x.Y, _x.speed, _x.lat, _x.long, _x.time, _x.ValidGPSfix, _x.number_of_satellites))
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(_x))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(_x))))

  def deserialize_numpy(self, str, numpy):
    """
    unpack serialized message in str into this message instance using numpy for array types
    :param str: byte array of serialized message, ``str``
    :param numpy: numpy python module
    """
    try:
      end = 0
      _x = self
      start = end
      end += 38
      (_x.X, _x.Y, _x.speed, _x.lat, _x.long, _x.time, _x.ValidGPSfix, _x.number_of_satellites,) = _struct_3f3d2b.unpack(str[start:end])
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e) #most likely buffer underfill

_struct_I = genpy.struct_I
_struct_3f3d2b = struct.Struct("<3f3d2b")
