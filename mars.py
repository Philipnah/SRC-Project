import socket

# socket.gethostname() = 192.168.56.1

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("192.168.56.1", 8000))

while True:
     buffersize = 256
     message = s.recv(buffersize)
     print(message.decode("utf-8"))
     