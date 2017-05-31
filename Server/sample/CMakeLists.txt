
cmake_minimum_required(VERSION 2.6)

include(../server.cmake)

include_directories(../external/include)
link_directories(${CMAKE_CURRENT_SOURCE_DIR}/../external/lib)
link_libraries(libevent.a)

add_executable(echo_server.bin echo_server.cc)
