#include <config.h>
#include <stdio.h>

#include "base.h"
#include "crypto.h"
#include "comm.h"
#include "packet.h"

void handlePacket(char *packet, int *sc)
{
	int it;

    char m[256];
    int m_len;    
    sc_decrypt(packet, 256, KEY, m, &m_len);

    char h[16];
    hash(h, m);

    int k;
    for(k=0; k<16; k++) {

        if(packet[256+k] != h[k]) {

            ERROR("the hash value is not the same!");
            return ;
        }
        
    }

    int SC_tmp = *(int *)m;

    if(SC_tmp != *sc) {

        ERROR("SC is not the same");
        return ;

    }

    update(sc);

    for (k=0; k<252; k++) {
        
        if(m[4+k] == (0x01)) {
            fprintf(stderr, "\n");
            break;            
        }

        fprintf(stderr, "%c", m[4+k]);

    }


}
