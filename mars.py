import socket
# socket.gethostname() = 192.168.56.1


headerSize = 10

message = "Contact!"

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("127.0.0.1", 8000))




while True:
     fullMsg = ""
     newMsg = True

     while True:
          
          buffersize = 256
          message = s.recv(buffersize)

          if newMsg:
               print(f"new message length: {message[:headerSize]}")
               msgLength = int(message[:headerSize])
               newMsg = False

          fullMsg += message.decode("utf-8")
          
          if len(fullMsg) - headerSize == msgLength:
               print("Full message received.\n")
               print("Message:\n\n" + fullMsg[headerSize:])
               newMsg = True
               fullMsg = ""

     print(fullMsg)
          