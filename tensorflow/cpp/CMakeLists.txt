cmake_minimum_required(VERSION 3.0)
project(tf_cpp_test)
set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -g -std=c++11 -W")
add_definitions(-D_GLIBCXX_USE_CXX11_ABI=0)

link_directories("/home/wxx/lib/tensorflow/bazel-bin/tensorflow")
include_directories(
    "/home/wxx/lib/tensorflow-1.15.0/"
    "/home/wxx/lib/tensorflow/abseil-cpp/"
    "/home/wxx/lib/tensorflow-1.15.0/bazel-bin"
    "/home/wxx/.cache/bazel/_bazel_wxx/138d3064134b4f4fbe572fbcabe939b1/external/com_google_protobuf/src"
    "/usr/include/eigen3"
)
   
add_executable(tf_cpp_test src/test.cpp)
target_link_libraries(tf_cpp_test tensorflow_cc tensorflow_framework)