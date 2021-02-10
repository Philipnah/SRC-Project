import zlib as z
from random import randint

spacer = "<<spacer>>"


def ComposeMsg(message):
    
     checksum = z.adler32(message.encode('ascii'))

     message = str(checksum) + spacer + message

     print("The following will be sent: " + message + "\n")
     return message


def ReceiveMsg(msg):
     try:
          splitMsg = msg.split(spacer)
     except:
          print("Message was destroyed while under travel")
     try:
          if splitMsg[0] == str(z.adler32(splitMsg[1].encode('ascii'))):
               print("Intact message was recevied:\n")
               print(splitMsg[1])
          else:
               print("Message was destroyed while under travel")
     except:
          print("Message was destroyed while under travel")


message = input("message: ")

receivedmsg = ComposeMsg(message)


# remove random character
i = randint(0, len(receivedmsg) - 1)
receivedmsg = receivedmsg[:i] + receivedmsg[i + 1:]
print(receivedmsg)


ReceiveMsg(receivedmsg)