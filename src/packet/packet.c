#include <stdlib.h>
#include <string.h>

#include "sender.h"
#include "config.h"
#include "packet.h"


void split(char **dest, int num, char *src)
{
    int k;
    char *p = src;

    for(k=0;k<num;k++)
    {
        dest[k] = (char *)malloc(256+16);
        memcpy(dest[k]+4, p, 252);
        p+= 252;

    }


    
}
void addSC(char *dest)
{

    int *p= (int *)dest;
    *p = SC;

}
void addZero(char *dest, int num)
{
    int k;

    char *p = dest + 255;
    for (k=0; k < num-1; k++)
    {
        /* code */
        *p = 0;
        p--;
        
    }

    if(num==0)
       return;
    *p = 1;

    
}
void hash(char *dest, char *src)
{
    int k;
    for(k=0;k<16;k++)
    {
        dest[k] = 0;

    }

    for(k=0; k<256;k++ )
    {

        dest[k%16] ^= src[k];

    }
    
}
void addHash(char *dest, char *src)
{
    int k;

    char *p= dest+256;
    for(k=0;k<16;k++)
    {

        *p=src[k];
        p++;

    }
}
void update(int *SC)
{

    *SC = *SC + 1;

}
void initial()
{

    SC = 0;
    i=0;
    j=0;


}


