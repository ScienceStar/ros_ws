import rclpy
from rclpy.node import Node
from rclpy.action import ActionClient
from robot_action_demo_interfaces.action import MoveRobot

class MoveRobotActionClient(Node):

    def __init__(self):
        super().__init__('move_robot_action_client')
        self._action_client = ActionClient(self, MoveRobot, 'move_robot')

    def send_goal(self, x, y, z):
        self._action_client.wait_for_server()
        goal_msg = MoveRobot.Goal()
        goal_msg.x = x
        goal_msg.y = y
        goal_msg.z = z

        future = self._action_client.send_goal_async(goal_msg, feedback_callback=self.feedback_callback)
        rclpy.spin_until_future_complete(self, future)
        goal_handle = future.result()
        if not goal_handle.accepted:
            self.get_logger().info('Goal rejected')
            return

        self.get_logger().info('Goal accepted, waiting for feedback...')
        result_future = goal_handle.get_result_async()
        while rclpy.ok():
            rclpy.spin_once(self, timeout_sec=1.0)
            if result_future.done():
                result = result_future.result().result
                self.get_logger().info(f'Result: {result.success}')
                break  # 如果你想永不结束，这里可以去掉 break

    def feedback_callback(self, feedback_msg):
        fb = feedback_msg.feedback
        self.get_logger().info(f'Feedback received: {fb.current_x}, {fb.current_y}, {fb.current_z}')

def main():
    rclpy.init()
    client = MoveRobotActionClient()
    client.send_goal(1.0, 2.0, 3.0)
    rclpy.spin(client)
    client.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()