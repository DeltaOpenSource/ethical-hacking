from socket import *

serverPort = 8000
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
clientSocket.bind(('', serverPort))
clientSocket.listen(1)
print("Linstening is start")
controllerSocket, addr = clientSocket.accept()

command = ''
while command != "exit":
  command = input("Enter the command...")
  controllerSocket.send(command.encode())
  message = controllerSocket.recv(1024).decode()
  print(message)

controllerSocket.shutdown(SHUT_RDWR)
clientSocket.close()
