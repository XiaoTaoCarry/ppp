#include <stdio.h>

#include "first.h"
int sc_encrypt(char *pl_text, int pl_len, char *key, char *a, int *a_len)

{
    int i,j,t,tmp,k;
    int S[ST_LEN];
    int T[ST_LEN];

   for (i=0;i<ST_LEN;i++)
   {
       S[i] = i;
       T[i] = key [i %KEY_LEN];
   }
    
    j=0;
    for (i=0;i<ST_LEN;i++)
    {
        j = (j+S[i]+T[i]) % ST_LEN;
        tmp=S[i];
        S[i]=S[j];
        S[j]=tmp;

    }

    int r=0;
    for(r=0;r<pl_len;r++)
    {

        i = (i+1)% ST_LEN;
        j = (j+S[i])% ST_LEN;
        tmp=S[i];
        S[i]=S[j];
        S[j]=tmp;
        t = (S[i]+S[j])% ST_LEN;
        k = S[t];
        a[r]=k^pl_text[r];
    
    }



    *a_len=pl_len;
    return 0;

}