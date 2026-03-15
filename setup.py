from setuptools import setup

package_name = 'wave_rover_base'

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
    maintainer='Beau Dougan',
    maintainer_email='beau.dougan@gmail.com',
    description='ROS 2 base driver for Waveshare Wave Rover over USB serial',
    license='Apache-2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'base_node = wave_rover_base.base_node:main',
        ],
    },
)
