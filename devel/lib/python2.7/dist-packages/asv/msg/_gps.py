"""autogenerated by genpy from asv/gps.msg. Do not edit."""
import sys
python3 = True if sys.hexversion > 0x03000000 else False
import genpy
import struct


class gps(genpy.Message):
  _md5sum = "9c9f9b1f6b33d777ab50714e4764c884"
  _type = "asv/gps"
  _has_header = False #flag to mark the presence of a Header object
  _full_text = """float64 	latitude
float64 	longitude
float64 	time
int8 		number_of_satellites
int8 		fix
float64 	speed
float64 	x
float64 	y

"""
  __slots__ = ['latitude','longitude','time','number_of_satellites','fix','speed','x','y']
  _slot_types = ['float64','float64','float64','int8','int8','float64','float64','float64']

  def __init__(self, *args, **kwds):
    """
    Constructor. Any message fields that are implicitly/explicitly
    set to None will be assigned a default value. The recommend
    use is keyword arguments as this is more robust to future message
    changes.  You cannot mix in-order arguments and keyword arguments.

    The available fields are:
       latitude,longitude,time,number_of_satellites,fix,speed,x,y

    :param args: complete set of field values, in .msg order
    :param kwds: use keyword arguments corresponding to message field names
    to set specific fields.
    """
    if args or kwds:
      super(gps, self).__init__(*args, **kwds)
      #message fields cannot be None, assign default values for those that are
      if self.latitude is None:
        self.latitude = 0.
      if self.longitude is None:
        self.longitude = 0.
      if self.time is None:
        self.time = 0.
      if self.number_of_satellites is None:
        self.number_of_satellites = 0
      if self.fix is None:
        self.fix = 0
      if self.speed is None:
        self.speed = 0.
      if self.x is None:
        self.x = 0.
      if self.y is None:
        self.y = 0.
    else:
      self.latitude = 0.
      self.longitude = 0.
      self.time = 0.
      self.number_of_satellites = 0
      self.fix = 0
      self.speed = 0.
      self.x = 0.
      self.y = 0.

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
      buff.write(_struct_3d2b3d.pack(_x.latitude, _x.longitude, _x.time, _x.number_of_satellites, _x.fix, _x.speed, _x.x, _x.y))
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
      end += 50
      (_x.latitude, _x.longitude, _x.time, _x.number_of_satellites, _x.fix, _x.speed, _x.x, _x.y,) = _struct_3d2b3d.unpack(str[start:end])
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
      buff.write(_struct_3d2b3d.pack(_x.latitude, _x.longitude, _x.time, _x.number_of_satellites, _x.fix, _x.speed, _x.x, _x.y))
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
      end += 50
      (_x.latitude, _x.longitude, _x.time, _x.number_of_satellites, _x.fix, _x.speed, _x.x, _x.y,) = _struct_3d2b3d.unpack(str[start:end])
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e) #most likely buffer underfill

_struct_I = genpy.struct_I
_struct_3d2b3d = struct.Struct("<3d2b3d")