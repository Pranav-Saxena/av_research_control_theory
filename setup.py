from setuptools import find_packages, setup

package_name = 'av_research_control_theory'
data_files =[]
data_files.append(('share/ament_index/resource_index/packages', ['resource/' + package_name]))
data_files.append(('share/' + package_name + '/launch', ['launch/lane_follower_tesla_launch.py','launch/lane_follower_bmwx5_launch.py']))
data_files.append(('share/' + package_name + '/worlds', ['worlds/tesla.wbt','worlds/bmwx5.wbt','worlds/.city.wbproj','worlds/city.wbt','worlds/.world.wbproj']))
data_files.append(('share/' + package_name + '/resource', ['resource/my_vehicle.urdf']))
data_files.append(('share/' + package_name, ['package.xml']))

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=data_files,
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='Vedant87',
    maintainer_email='vedant@todo.todo',
    description='TODO: Package description',
    license='Apache-2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'lane_follower = av_research_control_theory.lane_follower:main'
        ],
        'launch.frontend.launch_extension': ['launch_ros = launch_ros']

    },
)
