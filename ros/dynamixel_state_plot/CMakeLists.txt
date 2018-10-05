cmake_minimum_required(VERSION 2.8.3)
project(dynamixel_state_plot)

## Compile as C++11, supported in ROS Kinetic and newer
# add_compile_options(-std=c++11)

## Find catkin macros and libraries
## if COMPONENTS list like find_package(catkin REQUIRED COMPONENTS xyz)
## is used, also find other catkin packages
find_package(catkin REQUIRED COMPONENTS
  roscpp
  rospy
  sensor_msgs
  std_msgs
  message_generation
  dynamixel_monitor_module
)

generate_messages(
  DEPENDENCIES
  std_msgs
)