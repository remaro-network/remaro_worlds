cmake_minimum_required(VERSION 3.5)
project(remaro_worlds)

find_package(ament_cmake REQUIRED COMPONENTS)

# Hooks
ament_environment_hooks("hooks/resource_paths.dsv.in")
ament_environment_hooks("hooks/resource_paths.sh")

install(DIRECTORY
  launch
  Media
  worlds
  models
  DESTINATION share/${PROJECT_NAME}
)

ament_package()
