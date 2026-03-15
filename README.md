# Wave_Rover_Base_ROS2_Jazzy
Allows ROS2 to communicate with the Wave Rover robot board through connection to the usb0 port.
Designed for use with ROS2 Jazzy on a Rubik Pi 3 board.
Place in ~ros2_ws/src/wave_rover_base

Build commands for my pi:
cd ~/ros2_ws
source /opt/ros/jazzy/setup.bash
colcon build --symlink-install --base-paths src --packages-select wave_rover_base
source install/setup.bash

Run command for my pi (assumes robot board is plugged in through usb to port 0):
ros2 run wave_rover_base base_node --ros-args -p port:=/dev/ttyUSB0
