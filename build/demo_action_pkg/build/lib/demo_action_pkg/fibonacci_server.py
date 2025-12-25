import rclpy
from rclpy.node import Node
from rclpy.action import ActionServer
from demo_action_pkg.action import Fibonacci
from rclpy.executors import MultiThreadedExecutor

class FibonacciActionServer(Node):

    def __init__(self):
        super().__init__('fibonacci_server')
        self._action_server = ActionServer(
            self,
            Fibonacci,
            'fibonacci',
            self.execute_callback
        )

    def execute_callback(self, goal_handle):
        self.get_logger().info('Executing goal...')
        order = goal_handle.request.order
        feedback_msg = Fibonacci.Feedback()
        result = Fibonacci.Result()

        sequence = [0, 1]
        for i in range(2, order):
            sequence.append(sequence[i-1] + sequence[i-2])
            feedback_msg.partial_sequence = sequence.copy()
            goal_handle.publish_feedback(feedback_msg)
            self.get_logger().info(f'Feedback: {feedback_msg.partial_sequence}')

        result.sequence = sequence[:order]
        goal_handle.succeed()
        self.get_logger().info(f'Result: {result.sequence}')
        return result

def main(args=None):
    rclpy.init(args=args)
    node = FibonacciActionServer()
    executor = MultiThreadedExecutor()
    executor.add_node(node)
    try:
        executor.spin()
    finally:
        node.destroy_node()
        rclpy.shutdown()

if __name__ == '__main__':
    main()