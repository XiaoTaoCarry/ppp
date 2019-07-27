#ifndef SENDER_H
#define SENDER_H

int i,j;
int SC;

void split(char **dest, int num, char *src);
void addSC(char *dest);
void addZero(char *dest, int num);
void hash(char *dest, char *src);
void addHash(char *dest, char *src);
void update();
void initial();


#endif