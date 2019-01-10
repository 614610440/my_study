## ROS2 自定义自己的消息

## CMakeLists.txt
````
cmake_minimum_required(VERSION 3.5)
project(wxx_msgs)

if(NOT CMAKE_CXX_STANDARD)
  set(CMAKE_CXX_STANDARD 14)
endif()

if(CMAKE_COMPILER_IS_GNUCXX OR CMAKE_CXX_COMPILER_ID MATCHES "Clang")
  add_compile_options(-Wall -Wextra -Wpedantic -Werror)
endif()

find_package(ament_cmake REQUIRED)
find_package(builtin_interfaces REQUIRED)
find_package(geometry_msgs REQUIRED)
find_package(rosidl_default_generators REQUIRED)
find_package(std_msgs REQUIRED)

rosidl_generate_interfaces(${PROJECT_NAME}
  "msg/Test.msg"
  "srv/Test.srv"
  DEPENDENCIES builtin_interfaces geometry_msgs std_msgs
)

ament_export_dependencies(rosidl_default_runtime)

ament_package()
````

## package.xml
**注意**，下面的 format="3" 如果为2编译可能报错
````
<?xml version="1.0"?>
<?xml-model href="http://download.ros.org/schema/package_format2.xsd" schematypens="http://www.w3.org/2001/XMLSchema"?>
<package format="3">
  <name>wxx_msgs</name>
  <version>0.0.0</version>
  <description>TODO: Package description</description>
  <maintainer email="wxx@todo.todo">wxx</maintainer>
  <license>TODO: License declaration</license>

  <buildtool_depend>ament_cmake</buildtool_depend>

  <build_depend>rclcpp</build_depend>
  <build_depend>std_msgs</build_depend>
  <build_depend>builtin_interfaces</build_depend>
  <build_depend>rosidl_default_generators</build_depend>
  <build_depend>geometry_msgs</build_depend>

  <exec_depend>rclcpp</exec_depend>
  <exec_depend>std_msgs</exec_depend>
  <exec_depend>builtin_interfaces</exec_depend>
  <exec_depend>rosidl_default_runtime</exec_depend>
  <exec_depend>geometry_msgs</exec_depend>

  <test_depend>ament_lint_common</test_depend>
  <test_depend>ament_lint_auto</test_depend>
  <test_depend>ament_cmake_gtest</test_depend>
  <test_depend>ament_cmake_pytest</test_depend>

  <member_of_group>rosidl_interface_packages</member_of_group>

  <export>
    <build_type>ament_cmake</build_type>
  </export>
</package>
````

## msg/Test.msg
````
int32 test1
string name
````

## srv/Test.srv
````
int32 get_data
---
int32 result_data
````