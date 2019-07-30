#ifndef COMM_H 
#define COMM_H 

#include<stdio.h>

int socket_main(const char* entity_id, int id_len, int port, int *sc);
void sendPlaintext(int *sc, FILE *write_file);
void handlePacket(char *packet, int *sc);



#endif