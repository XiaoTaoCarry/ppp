#include "stdio.h"
#include <stdlib.h>
// #include <stdint.h>
#include "first.h"
int main()
{
    char key[]="ABCDEF0123456789ABC2019200436358";
    char m[]="Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.";

    char *c = (char *)malloc(1000);
    char *r = (char *)malloc(1000);


    int c_len=0;
    int r_len=0;

    encrypt(m,strlen(m) ,key,c,&c_len);
    
    printf("cipher:\n");
    int i;
    for (i=0; i<c_len; i++) {

        if(i%4==0) printf(" ");
        if(i%16==0) printf("\n");
        printf("%02x", (uint8_t)c[i]);

    }
    printf("\n");

    decrypt(c,c_len,key,r,&r_len);
    
    
    printf("\ndecrypted message : \n\t%s\n\n",r);

    return 0;

}