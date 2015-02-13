// Generated by gencpp from file asv/gps.msg
// DO NOT EDIT!


#ifndef ASV_MESSAGE_GPS_H
#define ASV_MESSAGE_GPS_H


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
struct gps_
{
  typedef gps_<ContainerAllocator> Type;

  gps_()
    : latitude(0.0)
    , longitude(0.0)
    , time(0.0)
    , number_of_satellites(0)
    , fix(0)
    , speed(0.0)
    , x(0.0)
    , y(0.0)  {
    }
  gps_(const ContainerAllocator& _alloc)
    : latitude(0.0)
    , longitude(0.0)
    , time(0.0)
    , number_of_satellites(0)
    , fix(0)
    , speed(0.0)
    , x(0.0)
    , y(0.0)  {
    }



   typedef double _latitude_type;
  _latitude_type latitude;

   typedef double _longitude_type;
  _longitude_type longitude;

   typedef double _time_type;
  _time_type time;

   typedef int8_t _number_of_satellites_type;
  _number_of_satellites_type number_of_satellites;

   typedef int8_t _fix_type;
  _fix_type fix;

   typedef double _speed_type;
  _speed_type speed;

   typedef double _x_type;
  _x_type x;

   typedef double _y_type;
  _y_type y;




  typedef boost::shared_ptr< ::asv::gps_<ContainerAllocator> > Ptr;
  typedef boost::shared_ptr< ::asv::gps_<ContainerAllocator> const> ConstPtr;

}; // struct gps_

typedef ::asv::gps_<std::allocator<void> > gps;

typedef boost::shared_ptr< ::asv::gps > gpsPtr;
typedef boost::shared_ptr< ::asv::gps const> gpsConstPtr;

// constants requiring out of line definition



template<typename ContainerAllocator>
std::ostream& operator<<(std::ostream& s, const ::asv::gps_<ContainerAllocator> & v)
{
ros::message_operations::Printer< ::asv::gps_<ContainerAllocator> >::stream(s, "", v);
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
struct IsFixedSize< ::asv::gps_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::asv::gps_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::asv::gps_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::asv::gps_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct HasHeader< ::asv::gps_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct HasHeader< ::asv::gps_<ContainerAllocator> const>
  : FalseType
  { };


template<class ContainerAllocator>
struct MD5Sum< ::asv::gps_<ContainerAllocator> >
{
  static const char* value()
  {
    return "9c9f9b1f6b33d777ab50714e4764c884";
  }

  static const char* value(const ::asv::gps_<ContainerAllocator>&) { return value(); }
  static const uint64_t static_value1 = 0x9c9f9b1f6b33d777ULL;
  static const uint64_t static_value2 = 0xab50714e4764c884ULL;
};

template<class ContainerAllocator>
struct DataType< ::asv::gps_<ContainerAllocator> >
{
  static const char* value()
  {
    return "asv/gps";
  }

  static const char* value(const ::asv::gps_<ContainerAllocator>&) { return value(); }
};

template<class ContainerAllocator>
struct Definition< ::asv::gps_<ContainerAllocator> >
{
  static const char* value()
  {
    return "float64 	latitude\n\
float64 	longitude\n\
float64 	time\n\
int8 		number_of_satellites\n\
int8 		fix\n\
float64 	speed\n\
float64 	x\n\
float64 	y\n\
";
  }

  static const char* value(const ::asv::gps_<ContainerAllocator>&) { return value(); }
};

} // namespace message_traits
} // namespace ros

namespace ros
{
namespace serialization
{

  template<class ContainerAllocator> struct Serializer< ::asv::gps_<ContainerAllocator> >
  {
    template<typename Stream, typename T> inline static void allInOne(Stream& stream, T m)
    {
      stream.next(m.latitude);
      stream.next(m.longitude);
      stream.next(m.time);
      stream.next(m.number_of_satellites);
      stream.next(m.fix);
      stream.next(m.speed);
      stream.next(m.x);
      stream.next(m.y);
    }

    ROS_DECLARE_ALLINONE_SERIALIZER;
  }; // struct gps_

} // namespace serialization
} // namespace ros

namespace ros
{
namespace message_operations
{

template<class ContainerAllocator>
struct Printer< ::asv::gps_<ContainerAllocator> >
{
  template<typename Stream> static void stream(Stream& s, const std::string& indent, const ::asv::gps_<ContainerAllocator>& v)
  {
    s << indent << "latitude: ";
    Printer<double>::stream(s, indent + "  ", v.latitude);
    s << indent << "longitude: ";
    Printer<double>::stream(s, indent + "  ", v.longitude);
    s << indent << "time: ";
    Printer<double>::stream(s, indent + "  ", v.time);
    s << indent << "number_of_satellites: ";
    Printer<int8_t>::stream(s, indent + "  ", v.number_of_satellites);
    s << indent << "fix: ";
    Printer<int8_t>::stream(s, indent + "  ", v.fix);
    s << indent << "speed: ";
    Printer<double>::stream(s, indent + "  ", v.speed);
    s << indent << "x: ";
    Printer<double>::stream(s, indent + "  ", v.x);
    s << indent << "y: ";
    Printer<double>::stream(s, indent + "  ", v.y);
  }
};

} // namespace message_operations
} // namespace ros

#endif // ASV_MESSAGE_GPS_H