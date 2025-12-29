import rclpy
from rclpy.node import Node
from rclpy.action import ActionClient
from robot_action_demo_interfaces.action import MoveRobot

class MoveRobotActionClient(Node):

    def __init__(self):
        super().__init__('move_robot_action_client')
        self._client = ActionClient(self, MoveRobot, 'move_robot')

    def send_goal(self, x, y, z):
        goal_msg = MoveRobot.Goal()
        goal_msg.x = x
        goal_msg.y = y
        goal_msg.z = z

        self._client.wait_for_server()
        self._client.send_goal_async(goal_msg)
        self.get_logger().info(f'Sent goal: {x}, {y}, {z}')

def main():
    rclpy.init()
    client = MoveRobotActionClient()
    client.send_goal(1.0, 2.0, 3.0)
    rclpy.spin(client)
    client.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()