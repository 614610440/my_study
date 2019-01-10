## ROS2 使用自定义消息

> [创建自定义消息](https://mp.csdn.net/mdeditor/84970610#)

> [示例代码](https://github.com/614610440/ROS2_demo)

## service
````
#include <inttypes.h>
#include <memory>

#include "rclcpp/rclcpp.hpp"
#include "wxx_msgs/srv/test.hpp"

#define TestService wxx_msgs::srv::Test

rclcpp::Node::SharedPtr g_node = nullptr;

void handle_service(
  const std::shared_ptr<rmw_request_id_t> request_header,
  const std::shared_ptr<TestService::Request> request,
  const std::shared_ptr<TestService::Response> response)
{
  (void)request_header;
  response->result_data = request->get_data + 10;
  RCLCPP_INFO(g_node->get_logger(), "I get data： %d, I response data: %d", request->get_data, response->result_data)
}

int main(int argc, char ** argv)
{
  rclcpp::init(argc, argv);
  g_node = rclcpp::Node::make_shared("test_service");
  auto server = g_node->create_service<TestService>("test", handle_service);
  rclcpp::spin(g_node);
  rclcpp::shutdown();
  return 0;
}
````

## client
````
#include <cinttypes>
#include <memory>
#include <chrono>

#include "wxx_msgs/srv/test.hpp"
#include "rclcpp/rclcpp.hpp"

#define TestService wxx_msgs::srv::Test

int main(int argc, char * argv[])
{
  rclcpp::init(argc, argv);
  auto node = rclcpp::Node::make_shared("test_client");
  auto client = node->create_client<TestService>("test");

  auto request = std::make_shared<TestService::Request>();

  for (int i = 0; i <= 10000; i++)
  {
    request->get_data = i;
    auto result_future = client->async_send_request(request);

    if (rclcpp::spin_until_future_complete(node, result_future) != 
        rclcpp::executor::FutureReturnCode::SUCCESS)
    {
       RCLCPP_ERROR(node->get_logger(), "service call failed!");
       continue;
    }

    auto result = result_future.get();

    RCLCPP_INFO(node->get_logger(), "I get result: %d", result->result_data);
    rclcpp::sleep_for(std::chrono::seconds(1));
  }
  
  rclcpp::shutdown();

  return 0;
}
````
