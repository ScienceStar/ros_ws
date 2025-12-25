from setuptools import find_packages, setup

package_name = 'demo_action_pkg'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
<<<<<<< HEAD
        # 添加 action 文件
        ('share/' + package_name + '/action', ['action/Fibonacci.action'])
=======
>>>>>>> c575643 (update:项目更新)
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='root',
    maintainer_email='sciencestar9346@163.com',
    description='TODO: Package description',
    license='TODO: License declaration',
    extras_require={
        'test': [
            'pytest',
        ],
    },
    entry_points={
        'console_scripts': [
        'talker = demo_action_pkg.publisher_node:main',
        'listener = demo_action_pkg.subscriber_node:main',
    ],
    },
)
