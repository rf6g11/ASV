// Generated by gencpp from file asv/rudderd.msg
// DO NOT EDIT!


#ifndef ASV_MESSAGE_RUDDERD_H
#define ASV_MESSAGE_RUDDERD_H


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
struct rudderd_
{
  typedef rudderd_<ContainerAllocator> Type;

  rudderd_()
    : rudder_demand(0.0)  {
    }
  rudderd_(const ContainerAllocator& _alloc)
    : rudder_demand(0.0)  {
    }



   typedef float _rudder_demand_type;
  _rudder_demand_type rudder_demand;




  typedef boost::shared_ptr< ::asv::rudderd_<ContainerAllocator> > Ptr;
  typedef boost::shared_ptr< ::asv::rudderd_<ContainerAllocator> const> ConstPtr;

}; // struct rudderd_

typedef ::asv::rudderd_<std::allocator<void> > rudderd;

typedef boost::shared_ptr< ::asv::rudderd > rudderdPtr;
typedef boost::shared_ptr< ::asv::rudderd const> rudderdConstPtr;

// constants requiring out of line definition



template<typename ContainerAllocator>
std::ostream& operator<<(std::ostream& s, const ::asv::rudderd_<ContainerAllocator> & v)
{
ros::message_operations::Printer< ::asv::rudderd_<ContainerAllocator> >::stream(s, "", v);
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
struct IsFixedSize< ::asv::rudderd_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::asv::rudderd_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::asv::rudderd_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::asv::rudderd_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct HasHeader< ::asv::rudderd_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct HasHeader< ::asv::rudderd_<ContainerAllocator> const>
  : FalseType
  { };


template<class ContainerAllocator>
struct MD5Sum< ::asv::rudderd_<ContainerAllocator> >
{
  static const char* value()
  {
    return "60078da9d4c3d9307b5235a0a0d7c95a";
  }

  static const char* value(const ::asv::rudderd_<ContainerAllocator>&) { return value(); }
  static const uint64_t static_value1 = 0x60078da9d4c3d930ULL;
  static const uint64_t static_value2 = 0x7b5235a0a0d7c95aULL;
};

template<class ContainerAllocator>
struct DataType< ::asv::rudderd_<ContainerAllocator> >
{
  static const char* value()
  {
    return "asv/rudderd";
  }

  static const char* value(const ::asv::rudderd_<ContainerAllocator>&) { return value(); }
};

template<class ContainerAllocator>
struct Definition< ::asv::rudderd_<ContainerAllocator> >
{
  static const char* value()
  {
    return "float32 rudder_demand\n\
";
  }

  static const char* value(const ::asv::rudderd_<ContainerAllocator>&) { return value(); }
};

} // namespace message_traits
} // namespace ros

namespace ros
{
namespace serialization
{

  template<class ContainerAllocator> struct Serializer< ::asv::rudderd_<ContainerAllocator> >
  {
    template<typename Stream, typename T> inline static void allInOne(Stream& stream, T m)
    {
      stream.next(m.rudder_demand);
    }

    ROS_DECLARE_ALLINONE_SERIALIZER;
  }; // struct rudderd_

} // namespace serialization
} // namespace ros

namespace ros
{
namespace message_operations
{

template<class ContainerAllocator>
struct Printer< ::asv::rudderd_<ContainerAllocator> >
{
  template<typename Stream> static void stream(Stream& s, const std::string& indent, const ::asv::rudderd_<ContainerAllocator>& v)
  {
    s << indent << "rudder_demand: ";
    Printer<float>::stream(s, indent + "  ", v.rudder_demand);
  }
};

} // namespace message_operations
} // namespace ros

#endif // ASV_MESSAGE_RUDDERD_H
