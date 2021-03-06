// Generated by gencpp from file asv/compass.msg
// DO NOT EDIT!


#ifndef ASV_MESSAGE_COMPASS_H
#define ASV_MESSAGE_COMPASS_H


#include <string>
#include <vector>
#include <map>

#include <ros/types.h>
#include <ros/serialization.h>
#include <ros/builtin_message_traits.h>
#include <ros/message_operations.h>


namespace asv
{
template <class ContainerAllocator>
struct compass_
{
  typedef compass_<ContainerAllocator> Type;

  compass_()
    : heading(0.0)
    , roll(0.0)
    , pitch(0.0)
    , pitch_der(0.0)
    , temperature(0.0)
    , depth(0.0)
    , m(0.0)
    , mx(0.0)
    , my(0.0)
    , mz(0.0)
    , a(0.0)
    , ax(0.0)
    , ay(0.0)
    , az(0.0)  {
    }
  compass_(const ContainerAllocator& _alloc)
    : heading(0.0)
    , roll(0.0)
    , pitch(0.0)
    , pitch_der(0.0)
    , temperature(0.0)
    , depth(0.0)
    , m(0.0)
    , mx(0.0)
    , my(0.0)
    , mz(0.0)
    , a(0.0)
    , ax(0.0)
    , ay(0.0)
    , az(0.0)  {
    }



   typedef float _heading_type;
  _heading_type heading;

   typedef float _roll_type;
  _roll_type roll;

   typedef float _pitch_type;
  _pitch_type pitch;

   typedef float _pitch_der_type;
  _pitch_der_type pitch_der;

   typedef float _temperature_type;
  _temperature_type temperature;

   typedef float _depth_type;
  _depth_type depth;

   typedef float _m_type;
  _m_type m;

   typedef float _mx_type;
  _mx_type mx;

   typedef float _my_type;
  _my_type my;

   typedef float _mz_type;
  _mz_type mz;

   typedef float _a_type;
  _a_type a;

   typedef float _ax_type;
  _ax_type ax;

   typedef float _ay_type;
  _ay_type ay;

   typedef float _az_type;
  _az_type az;




  typedef boost::shared_ptr< ::asv::compass_<ContainerAllocator> > Ptr;
  typedef boost::shared_ptr< ::asv::compass_<ContainerAllocator> const> ConstPtr;

}; // struct compass_

typedef ::asv::compass_<std::allocator<void> > compass;

typedef boost::shared_ptr< ::asv::compass > compassPtr;
typedef boost::shared_ptr< ::asv::compass const> compassConstPtr;

// constants requiring out of line definition



template<typename ContainerAllocator>
std::ostream& operator<<(std::ostream& s, const ::asv::compass_<ContainerAllocator> & v)
{
ros::message_operations::Printer< ::asv::compass_<ContainerAllocator> >::stream(s, "", v);
return s;
}

} // namespace asv

namespace ros
{
namespace message_traits
{



// BOOLTRAITS {'IsFixedSize': True, 'IsMessage': True, 'HasHeader': False}
// {'std_msgs': ['/opt/ros/indigo/share/std_msgs/cmake/../msg'], 'asv': ['/home/ric_94/catkin_ws/src/asv/msg']}

// !!!!!!!!!!! ['__class__', '__delattr__', '__dict__', '__doc__', '__eq__', '__format__', '__getattribute__', '__hash__', '__init__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', '_parsed_fields', 'constants', 'fields', 'full_name', 'has_header', 'header_present', 'names', 'package', 'parsed_fields', 'short_name', 'text', 'types']




template <class ContainerAllocator>
struct IsFixedSize< ::asv::compass_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::asv::compass_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::asv::compass_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::asv::compass_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct HasHeader< ::asv::compass_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct HasHeader< ::asv::compass_<ContainerAllocator> const>
  : FalseType
  { };


template<class ContainerAllocator>
struct MD5Sum< ::asv::compass_<ContainerAllocator> >
{
  static const char* value()
  {
    return "88afbcfc5596f414ffeacd3d60dc1ebd";
  }

  static const char* value(const ::asv::compass_<ContainerAllocator>&) { return value(); }
  static const uint64_t static_value1 = 0x88afbcfc5596f414ULL;
  static const uint64_t static_value2 = 0xffeacd3d60dc1ebdULL;
};

template<class ContainerAllocator>
struct DataType< ::asv::compass_<ContainerAllocator> >
{
  static const char* value()
  {
    return "asv/compass";
  }

  static const char* value(const ::asv::compass_<ContainerAllocator>&) { return value(); }
};

template<class ContainerAllocator>
struct Definition< ::asv::compass_<ContainerAllocator> >
{
  static const char* value()
  {
    return "float32 heading\n\
float32 roll\n\
float32 pitch\n\
float32 pitch_der\n\
float32 temperature\n\
float32 depth        \n\
float32 m\n\
float32 mx\n\
float32 my\n\
float32 mz\n\
float32 a\n\
float32 ax\n\
float32 ay\n\
float32 az\n\
\n\
";
  }

  static const char* value(const ::asv::compass_<ContainerAllocator>&) { return value(); }
};

} // namespace message_traits
} // namespace ros

namespace ros
{
namespace serialization
{

  template<class ContainerAllocator> struct Serializer< ::asv::compass_<ContainerAllocator> >
  {
    template<typename Stream, typename T> inline static void allInOne(Stream& stream, T m)
    {
      stream.next(m.heading);
      stream.next(m.roll);
      stream.next(m.pitch);
      stream.next(m.pitch_der);
      stream.next(m.temperature);
      stream.next(m.depth);
      stream.next(m.m);
      stream.next(m.mx);
      stream.next(m.my);
      stream.next(m.mz);
      stream.next(m.a);
      stream.next(m.ax);
      stream.next(m.ay);
      stream.next(m.az);
    }

    ROS_DECLARE_ALLINONE_SERIALIZER;
  }; // struct compass_

} // namespace serialization
} // namespace ros

namespace ros
{
namespace message_operations
{

template<class ContainerAllocator>
struct Printer< ::asv::compass_<ContainerAllocator> >
{
  template<typename Stream> static void stream(Stream& s, const std::string& indent, const ::asv::compass_<ContainerAllocator>& v)
  {
    s << indent << "heading: ";
    Printer<float>::stream(s, indent + "  ", v.heading);
    s << indent << "roll: ";
    Printer<float>::stream(s, indent + "  ", v.roll);
    s << indent << "pitch: ";
    Printer<float>::stream(s, indent + "  ", v.pitch);
    s << indent << "pitch_der: ";
    Printer<float>::stream(s, indent + "  ", v.pitch_der);
    s << indent << "temperature: ";
    Printer<float>::stream(s, indent + "  ", v.temperature);
    s << indent << "depth: ";
    Printer<float>::stream(s, indent + "  ", v.depth);
    s << indent << "m: ";
    Printer<float>::stream(s, indent + "  ", v.m);
    s << indent << "mx: ";
    Printer<float>::stream(s, indent + "  ", v.mx);
    s << indent << "my: ";
    Printer<float>::stream(s, indent + "  ", v.my);
    s << indent << "mz: ";
    Printer<float>::stream(s, indent + "  ", v.mz);
    s << indent << "a: ";
    Printer<float>::stream(s, indent + "  ", v.a);
    s << indent << "ax: ";
    Printer<float>::stream(s, indent + "  ", v.ax);
    s << indent << "ay: ";
    Printer<float>::stream(s, indent + "  ", v.ay);
    s << indent << "az: ";
    Printer<float>::stream(s, indent + "  ", v.az);
  }
};

} // namespace message_operations
} // namespace ros

#endif // ASV_MESSAGE_COMPASS_H
