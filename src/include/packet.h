#ifndef PACKET_H 
#define PACKET_H

void split(char **dest, int num, char *src);
void addSC(char *dest);
void addZero(char *dest, int num);
void hash(char *dest, char *src);
void addHash(char *dest, char *src);
void update(int *sc);
void initial();
void hash(char *dest, char *src);



#endif