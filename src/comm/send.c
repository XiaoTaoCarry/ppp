#include <comm.h>
#include <base.h>
#include <crypto.h>
#include <packet.h>

#include <stdio.h>

void sendPlaintext(int *sc, FILE *write_file)
{

	char m[1024]={0};
    printf("What do you want to send?\n");
    scanf("%s", m);
	int m_len = strlen(m);
    int last_len = m_len % 256;
    
	char c[256];
	int c_len;
    int k;

	int num = (m_len+255)/256;
	char *sgmt[num];
	split(sgmt, num, m);
    char h[16];

    for(k=0;k<num;k++)
    {

        addSC(sgmt[k]);

        if(k == num-1) {
            addZero(sgmt[k]+4, 256-last_len);
        }

        hash(h, sgmt[k]);
        addHash(sgmt[k], h);


        int it;

        sc_encrypt(sgmt[k], 256, KEY, c, &c_len);
        memcpy(sgmt[k], c, 256);

        printf("\n\n");

        update(sc);
        Write(fileno(write_file), sgmt[k], 256+16);
        
    }

    printf("send finish\n");

}
