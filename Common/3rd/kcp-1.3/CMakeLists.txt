
cmake_minimum_required(VERSION 2.6)

project(kcp)

set(CMAKE_INSTALL_PREFIX "${PROJECT_SOURCE_DIR}/../../../Server/external")
aux_source_directory(. SRC_FILES)

add_library(kcp STATIC ${SRC_FILES})

install(FILES "${PROJECT_SOURCE_DIR}/ikcp.h"
	DESTINATION "include")
install(FILES "${PROJECT_BINARY_DIR}/libkcp.a"
	DESTINATION "lib")
