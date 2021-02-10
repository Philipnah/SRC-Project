import socket

headerSize = 10

message = input("Type your message here: ")

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('192.168.56.1', 8000))
s.listen(5)

while True:
     clientsocket, address = s.accept() # this accepts all incoming requests
     print(f"Connection from {address} has been established.")
     
     # the following step is done to add a header to the message
     message = f'{len(message):<{headerSize}}' + message

     # this step actually sends the message over the network
     clientsocket.send(message.encode("utf-8"))
     