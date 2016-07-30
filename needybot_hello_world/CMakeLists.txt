cmake_minimum_required(VERSION 2.8.3)

project(needybot_hello_world)

catkin_python_setup()          

catkin_package(
  LIBRARIES
    ${PROJECT_NAME}
  CATKIN_DEPENDS
    needybot
    needybot_speech
    needybot_msgs 
    needybot_srvs
)
