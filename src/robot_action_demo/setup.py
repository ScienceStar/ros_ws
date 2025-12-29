from setuptools import setup

package_name = 'robot_action_demo'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    entry_points={
        'console_scripts': [
            'robot_action_server = robot_action_demo.robot_action_server:main',
            'robot_action_client = robot_action_demo.robot_action_client:main',
        ],
    },
)