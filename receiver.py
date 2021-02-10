import socket
# socket.gethostname() = 192.168.56.1


headerSize = 10


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('192.168.56.1', 8000))




while True:
     fullMsg = ""
     newMsg = True

     while True:
          
          buffersize = 256
          message = s.recv(buffersize)
          msgLength = 0

          if newMsg:
               print(f"new message length: {message[:headerSize]}")
               msgLength = int(message[:headerSize])
               newMsg = False

          fullMsg += message.decode("utf-8")
          
          if len(fullMsg) - headerSize == msgLength:
               print("Message has been received.\n")
               print("Message content:\n\n" + fullMsg[headerSize:] + "\n")
               newMsg = True
               fullMsg = ""


          