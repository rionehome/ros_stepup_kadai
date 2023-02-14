cmake_minimum_required(VERSION 3.0.2)
project(ros_stepup_kadai)

find_package(catkin REQUIRED COMPONENTS
	rospy
	std_msgs
	message_generation
)

add_message_files(
	FILES
	Okuha_kataranai.msg
)

generate_messages(
	DEPENDENCIES
	std_msgs
)

catkin_package(
   CATKIN_DEPENDS rospy std_msgs message_runtime
)

include_directories(
# include
# ${catkin_INCLUDE_DIRS}
)
