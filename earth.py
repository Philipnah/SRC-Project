import socket

headerSize = 10

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(("127.0.0.1", 8000))
s.listen(5)

while True:
     clientsocket, address = s.accept()
     print(f"Connection from {address} has been established.")
     
     message = "Contact!"
     message = f'{len(message):<{headerSize}}' + message
     clientsocket.send(message.encode("utf-8"))
     
     