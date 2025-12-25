cmake_minimum_required(VERSION 3.8)
project(demo_action_pkg)

find_package(ament_cmake REQUIRED)
find_package(rclpy REQUIRED)
find_package(rosidl_default_generators REQUIRED)

rosidl_generate_interfaces(${PROJECT_NAME}
  "action/Fibonacci.action"
  DEPENDENCIES action_msgs
)

ament_export_dependencies(rosidl_default_runtime)

ament_python_install_package(${PROJECT_NAME})

install(PROGRAMS
  demo_action_pkg/fibonacci_server.py
  demo_action_pkg/fibonacci_client.py
  DESTINATION lib/${PROJECT_NAME}
)

ament_package()