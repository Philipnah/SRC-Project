import socket


message = "Contact!"

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((socket.gethostname(), 8000))
s.listen(5)

while True:
     clientsocket, address = s.accept()
     print(f"Connection from {address} has been established.")
     clientsocket.send(message.encode("utf-8"))
     clientsocket.close()