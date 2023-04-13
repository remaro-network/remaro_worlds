# remaro_worlds: REMARO Worlds for ROS Simulation

## Screenshots

![small_pipeline](https://github.com/remaro-network/remaro_worlds/blob/main/imgs/small_pipeline.png)
![gas_infra](https://github.com/remaro-network/remaro_worlds/blob/main/imgs/gas_infra.png)

## Acknowledgements

<a href="https://remaro.eu/">
    <img height="60" alt="REMARO Logo" src="https://remaro.eu/wp-content/uploads/2020/09/remaro1-right-1024.png">
</a>

This work is part of the Reliable AI for Marine Robotics (REMARO) Project. For more info, please visit: <a href="https://remaro.eu/">https://remaro.eu/

<br>

<a href="https://research-and-innovation.ec.europa.eu/funding/funding-opportunities/funding-programmes-and-open-calls/horizon-2020_en">
    <img align="left" height="60" alt="EU Flag" src="https://remaro.eu/wp-content/uploads/2020/09/flag_yellow_low.jpg">
</a>

This project has received funding from the European Union's Horizon 2020 research and innovation programme under the Marie Skłodowska-Curie grant agreement No. 956200.

## Notes

- Gas Infrastructure models are part of the "3D Fuel Tank 4-X" collection created by Mykhailo Ohorodnichuk and currently available for free from [TurboSquid](https://www.turbosquid.com/3d-models/3d-fuel-tank-1443266). In order to use the gas_infrastructure world, as show in the image above, this collection should be, if necessary, and downloaded. Then, the corresponding model.obj and material.png files should be extracted and added to the appropriate models/structures subdirectories.

- Terrains created in [Blender](https://www.blender.org/download/) using the [ANT Landscape](https://docs.blender.org/manual/en/latest/addons/add_mesh/ant_landscape.html) add-on

- Other custom CAD models created in [AutoDesk Inventor](https://www.autodesk.com/products/inventor)

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
roslaunch remaro_worlds spawn small_pipeline_world.launch
```
