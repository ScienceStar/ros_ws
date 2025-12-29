import rclpy
from rclpy.node import Node
from rclpy.action import ActionServer
from robot_action_demo_interfaces.action import MoveRobot

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
        goal_handle.succeed()
        result = MoveRobot.Result()
        result.success = True
        return result

def main():
    rclpy.init()
    node = MoveRobotActionServer()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()