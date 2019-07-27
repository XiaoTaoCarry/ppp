# add the executable
add_executable (servertest servertest.c)
target_link_libraries (servertest commapi pthread)
add_executable (clienttest clienttest.c)
target_link_libraries (clienttest commapi pthread)
