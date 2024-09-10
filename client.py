#Name: Iman Khaleda binti Zamri (이만)
# Student ID: 2021079443
import socket
import random as r

HEADER = 64 #tells us on the length of message that will come next in byte
PORT = 12345 #use a port that is inactive
SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER, PORT)
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "DISCONNECT!"

#Create a TCP/IP socket
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR) #connect to the server

#- After the connection is established using connect(), data can be sent through the 
#  socket with send() and received with recv(). 
def send(msg):
    message = msg.encode(FORMAT)
    msg_length = len(message)
    send_length = str(msg_length).encode(FORMAT)
    send_length += b' '*(HEADER-len(send_length))
    client.send(send_length)
    client.send(message)
    print(client.recv(2048).decode(FORMAT))

# Generate a random word each time client.py is run to provide a variety of words in the program.
def randomMessage ():

    alphaChars = ['apple', 'ball', 'cow', 'doll', 'ear', 'fan', 'jar', 'hello', 'ice', 'jug', 'kreme', 'lemon', 'mandarin', 'noir', 'orange', 'popcorn', 'rolls', 'sauce']
    
   
    for a in range(len(alphaChars)):
        return r.choice(alphaChars)

send(randomMessage())
send(randomMessage())
send(randomMessage())
send(DISCONNECT_MESSAGE)