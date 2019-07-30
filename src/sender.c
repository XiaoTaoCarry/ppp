#include <config.h>
#include <stdlib.h>
#include <stdio.h>

#include "sender.h"
#include "comm.h"
#include "base.h"

int main()
{
    socket_main(CLIENT_ID, CLIENT_ID_LEN, CLIENT_PORT, &SC);

}