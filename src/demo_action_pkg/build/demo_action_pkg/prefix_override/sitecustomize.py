import sys
if sys.prefix == '/usr':
    sys.real_prefix = sys.prefix
    sys.prefix = sys.exec_prefix = '/root/ros_ws/src/demo_action_pkg/install/demo_action_pkg'
