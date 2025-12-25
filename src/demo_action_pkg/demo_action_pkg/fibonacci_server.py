#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from demo_action_pkg.action import Fibonacci
from rclpy.action import ActionServer

class FibonacciActionServer(Node):
    def __init__(self):
        super().__init__('fibonacci_action_server')
        self._action_server = ActionServer(
            self,
            Fibonacci,
            'fibonacci',
            self.execute_callback)

    def execute_callback(self, goal_handle):
        order = goal_handle.request.order
        sequence = [0, 1]
        for i in range(2, order):
            sequence.append(sequence[i-1] + sequence[i-2])
        goal_handle.succeed()
        result = Fibonacci.Result()
        result.sequence = sequence[:order]
        return result

def main(args=None):
    rclpy.init(args=args)
    node = FibonacciActionServer()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == '__main__':
    main()