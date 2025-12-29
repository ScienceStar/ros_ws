import rclpy
from rclpy.node import Node
from rclpy.action import ActionServer
from robot_action_demo_interfaces.action import MoveRobot
import time

class MoveRobotActionServer(Node):

    def __init__(self):
        super().__init__('move_robot_action_server')
        self._action_server = ActionServer(
            self,
            MoveRobot,
            'move_robot',
            self.execute_callback
        )

    def execute_callback(self, goal_handle):
        self.get_logger().info(f'Received goal: {goal_handle.request.x}, {goal_handle.request.y}, {goal_handle.request.z}')
        feedback = MoveRobot.Feedback()

        try:
            while rclpy.ok():
                # 每秒发送一次反馈
                feedback.current_x = goal_handle.request.x
                feedback.current_y = goal_handle.request.y
                feedback.current_z = goal_handle.request.z
                goal_handle.publish_feedback(feedback)
                self.get_logger().info(f'Feedback: {feedback.current_x}, {feedback.current_y}, {feedback.current_z}')
                time.sleep(1)
        except KeyboardInterrupt:
            pass

        # 这里不调用 goal_handle.succeed()，永不结束
        return None


def main():
    rclpy.init()
    node = MoveRobotActionServer()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()