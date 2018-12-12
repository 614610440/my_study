@[TOC](ROS2 创建自己的包)

> amnet 目前还没有类似catkin_created的命令，但是ros2自带的有

> #### ros2 pkg create命令
> + 创建包 **ros2 pkg create test** 会创建一个名为test的包
> + **ros2 pkg create test --dependencies std_msgs rclcpp** 创建包时添加 std_msgs和rclcpp依赖
> + **ros2 pkg create test --cpp-node-name my_test** 创建包时创建名为my_test节点,内容如下:
>> ```c++
>> #include <cstdio>
>> 
>> int main(int argc, char ** argv)
>> {
>>   (void) argc;
>>   (void) argv;
>> 
>>   printf("hello world my_test package\n");
>>   return 0;
>> }
>> ```
> + **ros2 pkg create test --cpp-library-name my_test** 创建包时创建名为mytest的库，在include/test/会生成my_test.hpp和visibility_control.h
> + **ros2 pkg create test --dependencies  std_msgs rclcpp --cpp-node-name my_node --cpp-library-name my_lib** 创建一个包含节点和库的包，并且依赖std_msgs和rclcpp，可以看到结果
>> ```txt
>> going to create a new package
>> package name: test
>> destination directory: /home/wxx/ros2_ws/src/wxxtest
>> package format: 2
>> version: 0.0.0
>> description: TODO: Package description
>> maintainer: ['wxx <wxx@todo.todo>']
>> licenses: ['TODO: License declaration']
>> build type: ament_cmake
>> dependencies: ['std_msgs', 'rclcpp']
>> cpp_node_name: my_node
>> cpp_library_name: my_lib
>> creating folder ./test
>> creating ./test/package.xml
>> creating source and include folder
>> creating folder ./test/src
>> creating folder ./test/include/test
>> creating ./test/CMakeLists.txt
>> creating ./test/src/my_node.cpp
>> creating ./test/include/test/my_lib.hpp
>> creating ./test/src/my_lib.cpp
>> creating ./test/include/test/visibility_control.h
>> ```