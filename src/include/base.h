/**!
 * @file base.h
 * @author Wang Ruikai 
 * @date July 14th, 2019 
 * @brief This file contains the data, macro common to both client and server
 */

#ifndef BASE_H
#define BASE_H

#include <unistd.h>
#include <stdio.h>
#include <stdlib.h>
#include <stddef.h>
#include <stdbool.h>
#include <string.h>
#include <signal.h>
#include <errno.h>
#include <fcntl.h>
#include <time.h>
#include <sys/types.h>
#include <sys/wait.h>
#include <sys/stat.h>
#include <sys/socket.h>
#include <netinet/in.h>
#include <arpa/inet.h>
#include <config.h>

#define __SOCKET_MODE__

// #define SA                      struct sockaddr

#define SYSTEM_LOG "/tmp/ibe_log"
#define NUM_THREADS 1

#define ERROR(s) {  \
    fprintf(stderr, s); \
    fprintf(stderr, "\n"); \
}


/*****************************************************
 * 类型定义
 * ***************************************************/
typedef struct sockaddr SA;

/*****************************************************
 * 函数声明
 * ***************************************************/
/*
 * socket 包装函数
 */
int   Fgets(char* s, int size, FILE* stream);
ssize_t Write(int fd, const void *vptr, size_t n);
int     Accept(int sockfd, struct sockaddr *addr, socklen_t *addrlen);

/* 
 * socket 监听与连接函数
 */
int create_listening_socket(int listen_port);
int connect_socket_server(char* ip_addr, int port, FILE** read_file, FILE** write_file);
int disconnect_socket_server(FILE* read_file, FILE* write_file);
int run_listen_core(const char* server_id, FILE* read_file, FILE* write_file, FILE* log_file);
void *socket_listener_run(void *args);
void sig_chld(int signo);


/* 
 * 系统函数
 */
FILE* open_log_file();

/**!
 * @brief run the user interface. Generally, it receives a request from the 
 *      the user and do something 
 * @param entity_id the id of the user 
 * @param id_len the length of the id 
 * @return -1 when something wrong, 0 when no errors
 */
int socket_interface_run(const char* entity_id, int id_len, void (*f) ());

#endif
