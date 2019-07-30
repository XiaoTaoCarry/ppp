add_executable (sender ${CMAKE_SOURCE_DIR}/src/sender.c)
target_link_libraries (sender commapi cryptoapi packet pthread)

add_executable (receiver ${CMAKE_SOURCE_DIR}/src/receiver.c)
target_link_libraries (receiver commapi cryptoapi packet pthread)
