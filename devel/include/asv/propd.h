// Generated by gencpp from file asv/propd.msg
// DO NOT EDIT!


#ifndef ASV_MESSAGE_PROPD_H
#define ASV_MESSAGE_PROPD_H


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
struct propd_
{
  typedef propd_<ContainerAllocator> Type;

  propd_()
    : prop_demand(0.0)  {
    }
  propd_(const ContainerAllocator& _alloc)
    : prop_demand(0.0)  {
    }



   typedef float _prop_demand_type;
  _prop_demand_type prop_demand;




  typedef boost::shared_ptr< ::asv::propd_<ContainerAllocator> > Ptr;
  typedef boost::shared_ptr< ::asv::propd_<ContainerAllocator> const> ConstPtr;

}; // struct propd_

typedef ::asv::propd_<std::allocator<void> > propd;

typedef boost::shared_ptr< ::asv::propd > propdPtr;
typedef boost::shared_ptr< ::asv::propd const> propdConstPtr;

// constants requiring out of line definition



template<typename ContainerAllocator>
std::ostream& operator<<(std::ostream& s, const ::asv::propd_<ContainerAllocator> & v)
{
ros::message_operations::Printer< ::asv::propd_<ContainerAllocator> >::stream(s, "", v);
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
struct IsFixedSize< ::asv::propd_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::asv::propd_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::asv::propd_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::asv::propd_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct HasHeader< ::asv::propd_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct HasHeader< ::asv::propd_<ContainerAllocator> const>
  : FalseType
  { };


template<class ContainerAllocator>
struct MD5Sum< ::asv::propd_<ContainerAllocator> >
{
  static const char* value()
  {
    return "b80390de6505fc9f662044172e64f5d7";
  }

  static const char* value(const ::asv::propd_<ContainerAllocator>&) { return value(); }
  static const uint64_t static_value1 = 0xb80390de6505fc9fULL;
  static const uint64_t static_value2 = 0x662044172e64f5d7ULL;
};

template<class ContainerAllocator>
struct DataType< ::asv::propd_<ContainerAllocator> >
{
  static const char* value()
  {
    return "asv/propd";
  }

  static const char* value(const ::asv::propd_<ContainerAllocator>&) { return value(); }
};

template<class ContainerAllocator>
struct Definition< ::asv::propd_<ContainerAllocator> >
{
  static const char* value()
  {
    return "float32 prop_demand\n\
";
  }

  static const char* value(const ::asv::propd_<ContainerAllocator>&) { return value(); }
};

} // namespace message_traits
} // namespace ros

namespace ros
{
namespace serialization
{

  template<class ContainerAllocator> struct Serializer< ::asv::propd_<ContainerAllocator> >
  {
    template<typename Stream, typename T> inline static void allInOne(Stream& stream, T m)
    {
      stream.next(m.prop_demand);
    }

    ROS_DECLARE_ALLINONE_SERIALIZER;
  }; // struct propd_

} // namespace serialization
} // namespace ros

namespace ros
{
namespace message_operations
{

template<class ContainerAllocator>
struct Printer< ::asv::propd_<ContainerAllocator> >
{
  template<typename Stream> static void stream(Stream& s, const std::string& indent, const ::asv::propd_<ContainerAllocator>& v)
  {
    s << indent << "prop_demand: ";
    Printer<float>::stream(s, indent + "  ", v.prop_demand);
  }
};

} // namespace message_operations
} // namespace ros

#endif // ASV_MESSAGE_PROPD_H