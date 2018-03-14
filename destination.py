import socket, sys

if len(sys.argv) != 3:
  print('\nUsage: '+sys.argv[0]+' <local_IP> <local_port\n')
  exit(1)
local_IP=sys.argv[1]
local_Port=int(sys.argv[2])

target = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
target.bind((local_IP,local_Port))
data, source = target.recvfrom(400)
print data, "from", source
