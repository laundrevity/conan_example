cmake_minimum_required(VERSION 3.8)
project(shmem)

set(CMAKE_CXX_STANDARD 20)
set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -pthread -fPIC -fsanitize=address -g -fno-omit-frame-pointer -Werror=return-type -Wall")

include(${CMAKE_BINARY_DIR}/conanbuildinfo.cmake)
conan_basic_setup()

add_executable(pressf main.cpp)
target_link_libraries(pressf PUBLIC ${Boost_LIBRARIES})
