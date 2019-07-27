# add the executable
add_executable (cryptotest crypto_test.c)
target_link_libraries (cryptotest cryptoapi pthread)

