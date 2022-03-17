# remaro_worlds: REMARO Worlds for ROS Simulation

## Screenshots

![min_world_far](https://github.com/remaro-network/remaro_worlds/blob/main/imgs/min_world_far.png)
![min_world_near](https://github.com/remaro-network/remaro_worlds/blob/main/imgs/min_world_near.png)

## Notes

- Terrains created in [Blender](https://www.blender.org/download/) using the [ANT Landscape](https://docs.blender.org/manual/en/latest/addons/add_mesh/ant_landscape.html) add-on

- CAD models created in [AutoDesk Inventor](https://www.autodesk.com/products/inventor)

 - Files and directories created following [this tutorial](http://gazebosim.org/tutorials?tut=ros_roslaunch#CreatingyourownGazeboROSPackage)

 - Worlds should work with any ROS-interfaced software (Gazebo, RViz, [Unreal](https://github.com/code-iai/ROSIntegration))

 - Initial goal is to work within [uuv_simulator](https://github.com/uuvsimulator/uuv_simulator) framework using [ROS Noetic](http://wiki.ros.org/noetic/Installation) and [Gazebo 11](http://gazebosim.org/)

## Installation

 - Install [Ubuntu 20 LTS](https://releases.ubuntu.com/20.04/ubuntu-20.04.3-desktop-amd64.iso).

  - Install [ROS Noetic](http://wiki.ros.org/noetic/Installation/Ubuntu).  Choose the "Desktop-Full Install" option so simulators are installed.

  - Ready workspace.

```bash
# Make directory for your workspace
mkdir -p ~/yourworkspacename/src

# Change directory to your workspace
cd ~/yourworkspacename/src

# Clone this package 
git clone https://github.com/remaro-network/remaro_worlds.git

# Move to root of your workspace directory
cd ~/yourworkspacename

# Make the workspace 
catkin_make

# Source your workspace in each terminal using this package.
source ~/yourworkspacename/devel/setup.bash

# If this is your only active ROS workspace,
# modify ~./bashrc to automatically source this workspace.
echo "source ~/yourworkspacename/devel/setup.bash" >> ~/.bashrc
```

## Usage
```bash
# To launch the simulated world
roslaunch remaro_worlds min_world.launch
```

## Acknowledgements
This project has received funding from the European Union’s Horizon 2020 research and innovation programme under the Marie Skłodowska-Curie grant agreement No. 956200.

Pleave visit [our website](https://remaro.eu/) for more info on our project.

![REMARO Logo](https://remaro.eu/wp-content/uploads/2020/09/remaro1-right-1024.png)