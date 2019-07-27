#include <stdio.h>
#include "first.h"

int sc_decrypt(char *cp_text, int cp_len, char *key, char *a, int *a_len)

{
    int i,j,t,tmp,k;
    int S[ST_LEN];
    int T[ST_LEN];

   for (i=0;i<256;i++)
   {
       S[i] = i;
       T[i] = key [i %KEY_LEN];
   }
    
    j=0;
    for (i=0;i<256;i++)
    {
        j = (j+S[i]+T[i]) % 256;
        tmp=S[i];
        S[i]=S[j];
        S[j]=tmp;

    }
    int r=0;
    for(r=0;r<cp_len;r++)
    {

        i = (i+1)%256;
        j = (j+S[i])%256;
        tmp=S[i];
        S[i]=S[j];
        S[j]=tmp;
        t = (S[i]+S[j])%256;
        k = S[t];
        a[r]=k^cp_text[r];
    
    }

    *a_len=cp_len;
    return 0;
    



}