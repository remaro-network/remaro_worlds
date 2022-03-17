cmake_minimum_required(VERSION 2.8.3)
project(remaro_worlds)

find_package(catkin REQUIRED COMPONENTS gazebo_ros)
# link_directories(${GAZEBO_LIBRARY_DIRS})
# include_directories(${Boost_INCLUDE_DIR} ${catkin_INCLUDE_DIRS} ${GAZEBO_INCLUDE_DIRS})
# install(DIRECTORY launch Media worlds models
#         DESTINATION ${CATKIN_PACKAGE_SHARE_DESTINATION}
#         PATTERN "*~" EXCLUDE)