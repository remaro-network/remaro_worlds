cmake_minimum_required(VERSION 3.5)
project(remaro_worlds)

find_package(ament_cmake REQUIRED COMPONENTS)
find_package(ament_cmake_python REQUIRED COMPONENTS)

install(DIRECTORY launch Media worlds models
  DESTINATION share/${PROJECT_NAME}
)

ament_package()
