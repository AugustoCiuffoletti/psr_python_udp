import socket, sys

if len(sys.argv) != 3:            # Controllo parametri
  print('\nUsage: '+sys.argv[0]+' <local_IP> <local_port\n')
  exit(1)
local_IP=sys.argv[1]
local_Port=int(sys.argv[2])

Message = "Hello"
source = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
source.sendto("Hallo", (local_IP,local_Port))
