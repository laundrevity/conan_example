cmake_minimum_required(VERSION 3.8)
project(shmem)

set(CMAKE_CXX_STANDARD 20)
set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -pthread")

set(CMAKE_MODULE_PATH ${CMAKE_CURRENT_SOURCE_DIR}/build)
find_package(Boost REQUIRED)
include_directories(${Boost_INCLUDE_DIRS})

add_executable(main main.cpp)
target_link_libraries(main ${Boost_LIBRARIES})