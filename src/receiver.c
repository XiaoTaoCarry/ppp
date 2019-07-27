#include "sender.h"
#include "comm.h"
#include "base.h"
#include "receiver.h"
#include "first.h"

#include <config.h>
#include <stdlib.h>
#include <stdio.h>




int main()
{

    socket_main(SERVER_ID, SERVER_ID_LEN, SERVER_LISTEN_PORT, NULL);

}