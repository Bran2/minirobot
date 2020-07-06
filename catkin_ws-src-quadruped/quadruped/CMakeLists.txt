cmake_minimum_required(VERSION 2.8.3)

project(quadruped)

find_package(catkin REQUIRED COMPONENTS
  urdf
)

catkin_package()

include_directories(
# include
  ${catkin_INCLUDE_DIRS}
)

add_executable(parser src/parser.cpp)
target_link_libraries(parser ${catkin_LIBRARIES})

find_package(roslaunch)

foreach(dir config launch meshes urdf)
	install(DIRECTORY ${dir}/
		DESTINATION ${CATKIN_PACKAGE_SHARE_DESTINATION}/${dir})
endforeach(dir)
