from setuptools import setup

package_name = 'demo_action_pkg'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='Your Name',
    maintainer_email='you@example.com',
    description='Demo Fibonacci Action Package',
    license='Apache License 2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'talker = demo_action_pkg.publisher_node:main',
            'listener = demo_action_pkg.subscriber_node:main',
            'fibonacci_server = demo_action_pkg.fibonacci_server:main',
            'fibonacci_client = demo_action_pkg.fibonacci_client:main',
        ],
    },
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        ('share/' + package_name + '/action', ['action/Fibonacci.action']),
    ],
)