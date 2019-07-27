#include <config.h>
#include <stdlib.h>
#include <stdio.h>

#include "sender.h"
#include "comm.h"
#include "base.h"

void sendPlaintext()
{

	FILE *read_file, *write_file;
	connect_socket_server(SERVER_IP_ADDRESS, SERVER_LISTEN_PORT, &read_file,  &write_file);
	char m[]="Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.";
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
        hash(h, sgmt[k]);
        addHash(sgmt[k], h);

        if(k == num-1) {
            sc_encrypt(sgmt[k], last_len, KEY, c, &c_len);
            memcpy(sgmt[k], c, c_len);
            addZero(sgmt[k], 256-c_len);
        }
        else {
            sc_encrypt(sgmt[k], 256, KEY, c, &c_len);
            memcpy(sgmt[k], c, 256);
        }


        int it;
        for (it=0; it<256+16; it+=4) {
            if(it%16==0) printf("\n");
            printf("%08x ", sgmt[k][it]);
        }

        update();
        Write(fileno(write_file), sgmt[k], 256+16);
        
    }

    printf("send finish\n");

}


int main()
{
    socket_main(CLIENT_ID, CLIENT_ID_LEN, CLIENT_PORT, sendPlaintext);
    


}