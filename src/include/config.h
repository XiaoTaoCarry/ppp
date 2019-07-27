

#ifndef CONFIG__H
#define CONFIG__H

/* used files */

#define MSK_FILE                "msk.conf"


/* buffer sizes */
#define BUFFER_SIZE             1024
#define SECURITY_BITS           256
#define MAX_ID_LEN              (SECURITY_BITS/8)
#define IBE_BUFFER_SIZE         128


/* server parameters */
#define LISTEN_BACKLOG          50

#define SERVER_ID              "Server"
#define SERVER_ID_LEN           6
#define SERVER_IP_ADDRESS       "127.0.0.1"
#define SERVER_LISTEN_PORT      5001
#define SERVER_RUN_PORT         5002

#define SC_LEN 4
#define DATA_LEN 252
#define HV_LEN 16

#define KEY "ABCDEF0123456789ABC2019200436358"

#define CLIENT_ID           "CLIENT"
#define CLIENT_ID_LEN       6
#define CLIENT_PORT         10001


#endif


