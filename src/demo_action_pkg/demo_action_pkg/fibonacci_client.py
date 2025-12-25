#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from demo_action_pkg.action import Fibonacci
from rclpy.action import ActionClient

class FibonacciActionClient(Node):
    def __init__(self):
        super().__init__('fibonacci_action_client')
        self._client = ActionClient(self, Fibonacci, 'fibonacci')
        self.send_goal(10)

    def send_goal(self, order):
        goal_msg = Fibonacci.Goal()
        goal_msg.order = order
        self._client.wait_for_server()
        self._client.send_goal_async(goal_msg)

def main(args=None):
    rclpy.init(args=args)
    node = FibonacciActionClient()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == '__main__':
    main()