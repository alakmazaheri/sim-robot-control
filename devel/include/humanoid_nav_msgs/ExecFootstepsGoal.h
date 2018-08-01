// Generated by gencpp from file humanoid_nav_msgs/ExecFootstepsGoal.msg
// DO NOT EDIT!


#ifndef HUMANOID_NAV_MSGS_MESSAGE_EXECFOOTSTEPSGOAL_H
#define HUMANOID_NAV_MSGS_MESSAGE_EXECFOOTSTEPSGOAL_H


#include <string>
#include <vector>
#include <map>

#include <ros/types.h>
#include <ros/serialization.h>
#include <ros/builtin_message_traits.h>
#include <ros/message_operations.h>

#include <humanoid_nav_msgs/StepTarget.h>

namespace humanoid_nav_msgs
{
template <class ContainerAllocator>
struct ExecFootstepsGoal_
{
  typedef ExecFootstepsGoal_<ContainerAllocator> Type;

  ExecFootstepsGoal_()
    : footsteps()
    , feedback_frequency(0.0)  {
    }
  ExecFootstepsGoal_(const ContainerAllocator& _alloc)
    : footsteps(_alloc)
    , feedback_frequency(0.0)  {
  (void)_alloc;
    }



   typedef std::vector< ::humanoid_nav_msgs::StepTarget_<ContainerAllocator> , typename ContainerAllocator::template rebind< ::humanoid_nav_msgs::StepTarget_<ContainerAllocator> >::other >  _footsteps_type;
  _footsteps_type footsteps;

   typedef double _feedback_frequency_type;
  _feedback_frequency_type feedback_frequency;





  typedef boost::shared_ptr< ::humanoid_nav_msgs::ExecFootstepsGoal_<ContainerAllocator> > Ptr;
  typedef boost::shared_ptr< ::humanoid_nav_msgs::ExecFootstepsGoal_<ContainerAllocator> const> ConstPtr;

}; // struct ExecFootstepsGoal_

typedef ::humanoid_nav_msgs::ExecFootstepsGoal_<std::allocator<void> > ExecFootstepsGoal;

typedef boost::shared_ptr< ::humanoid_nav_msgs::ExecFootstepsGoal > ExecFootstepsGoalPtr;
typedef boost::shared_ptr< ::humanoid_nav_msgs::ExecFootstepsGoal const> ExecFootstepsGoalConstPtr;

// constants requiring out of line definition



template<typename ContainerAllocator>
std::ostream& operator<<(std::ostream& s, const ::humanoid_nav_msgs::ExecFootstepsGoal_<ContainerAllocator> & v)
{
ros::message_operations::Printer< ::humanoid_nav_msgs::ExecFootstepsGoal_<ContainerAllocator> >::stream(s, "", v);
return s;
}

} // namespace humanoid_nav_msgs

namespace ros
{
namespace message_traits
{



// BOOLTRAITS {'IsFixedSize': False, 'IsMessage': True, 'HasHeader': False}
// {'humanoid_nav_msgs': ['/home/xbotcore/urdf_ws/src/humanoid_msgs/humanoid_nav_msgs/msg', '/home/xbotcore/urdf_ws/devel/share/humanoid_nav_msgs/msg'], 'actionlib_msgs': ['/opt/ros/kinetic/share/actionlib_msgs/cmake/../msg'], 'std_msgs': ['/opt/ros/kinetic/share/std_msgs/cmake/../msg'], 'geometry_msgs': ['/opt/ros/kinetic/share/geometry_msgs/cmake/../msg']}

// !!!!!!!!!!! ['__class__', '__delattr__', '__dict__', '__doc__', '__eq__', '__format__', '__getattribute__', '__hash__', '__init__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', '_parsed_fields', 'constants', 'fields', 'full_name', 'has_header', 'header_present', 'names', 'package', 'parsed_fields', 'short_name', 'text', 'types']




template <class ContainerAllocator>
struct IsFixedSize< ::humanoid_nav_msgs::ExecFootstepsGoal_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::humanoid_nav_msgs::ExecFootstepsGoal_<ContainerAllocator> const>
  : FalseType
  { };

template <class ContainerAllocator>
struct IsMessage< ::humanoid_nav_msgs::ExecFootstepsGoal_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::humanoid_nav_msgs::ExecFootstepsGoal_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct HasHeader< ::humanoid_nav_msgs::ExecFootstepsGoal_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct HasHeader< ::humanoid_nav_msgs::ExecFootstepsGoal_<ContainerAllocator> const>
  : FalseType
  { };


template<class ContainerAllocator>
struct MD5Sum< ::humanoid_nav_msgs::ExecFootstepsGoal_<ContainerAllocator> >
{
  static const char* value()
  {
    return "40a3f8092ef3bb49c3253baa6eb94932";
  }

  static const char* value(const ::humanoid_nav_msgs::ExecFootstepsGoal_<ContainerAllocator>&) { return value(); }
  static const uint64_t static_value1 = 0x40a3f8092ef3bb49ULL;
  static const uint64_t static_value2 = 0xc3253baa6eb94932ULL;
};

template<class ContainerAllocator>
struct DataType< ::humanoid_nav_msgs::ExecFootstepsGoal_<ContainerAllocator> >
{
  static const char* value()
  {
    return "humanoid_nav_msgs/ExecFootstepsGoal";
  }

  static const char* value(const ::humanoid_nav_msgs::ExecFootstepsGoal_<ContainerAllocator>&) { return value(); }
};

template<class ContainerAllocator>
struct Definition< ::humanoid_nav_msgs::ExecFootstepsGoal_<ContainerAllocator> >
{
  static const char* value()
  {
    return "# ====== DO NOT MODIFY! AUTOGENERATED FROM AN ACTION DEFINITION ======\n\
# Define the goal\n\
humanoid_nav_msgs/StepTarget[] footsteps\n\
float64 feedback_frequency\n\
\n\
================================================================================\n\
MSG: humanoid_nav_msgs/StepTarget\n\
# Target for a single stepping motion of a humanoid's leg\n\
\n\
geometry_msgs/Pose2D pose   # step pose as relative offset to last leg\n\
uint8 leg                   # which leg to use (left/right, see below)\n\
\n\
uint8 right=0               # right leg constant\n\
uint8 left=1                # left leg constant\n\
\n\
================================================================================\n\
MSG: geometry_msgs/Pose2D\n\
# This expresses a position and orientation on a 2D manifold.\n\
\n\
float64 x\n\
float64 y\n\
float64 theta\n\
";
  }

  static const char* value(const ::humanoid_nav_msgs::ExecFootstepsGoal_<ContainerAllocator>&) { return value(); }
};

} // namespace message_traits
} // namespace ros

namespace ros
{
namespace serialization
{

  template<class ContainerAllocator> struct Serializer< ::humanoid_nav_msgs::ExecFootstepsGoal_<ContainerAllocator> >
  {
    template<typename Stream, typename T> inline static void allInOne(Stream& stream, T m)
    {
      stream.next(m.footsteps);
      stream.next(m.feedback_frequency);
    }

    ROS_DECLARE_ALLINONE_SERIALIZER
  }; // struct ExecFootstepsGoal_

} // namespace serialization
} // namespace ros

namespace ros
{
namespace message_operations
{

template<class ContainerAllocator>
struct Printer< ::humanoid_nav_msgs::ExecFootstepsGoal_<ContainerAllocator> >
{
  template<typename Stream> static void stream(Stream& s, const std::string& indent, const ::humanoid_nav_msgs::ExecFootstepsGoal_<ContainerAllocator>& v)
  {
    s << indent << "footsteps[]" << std::endl;
    for (size_t i = 0; i < v.footsteps.size(); ++i)
    {
      s << indent << "  footsteps[" << i << "]: ";
      s << std::endl;
      s << indent;
      Printer< ::humanoid_nav_msgs::StepTarget_<ContainerAllocator> >::stream(s, indent + "    ", v.footsteps[i]);
    }
    s << indent << "feedback_frequency: ";
    Printer<double>::stream(s, indent + "  ", v.feedback_frequency);
  }
};

} // namespace message_operations
} // namespace ros

#endif // HUMANOID_NAV_MSGS_MESSAGE_EXECFOOTSTEPSGOAL_H
