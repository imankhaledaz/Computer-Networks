#Name: Iman Khaleda binti Zamri (이만)
# Student ID: 2021079443

import socket
import threading


#we will run each client on a different thread so that while one piece of code is waiting
#and not doing something, the other piece of code (the other thread) can run.
#We will put the message handling stuffs in separate thread for each client that is connected
#to our server. This is so that our client, will not have to wait for other clients to finish their
#message transmission

HEADER = 64 #tells us on the length of message that will come next in byte
PORT = 12345 #use a port that is inactive
SERVER = socket.gethostbyname(socket.gethostname()) #automatically attained the local IP address
ADDR = (SERVER, PORT)
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "DISCONNECT!"

#make a TCP socket to open up device to other connections
#AF_INET, SOCK_STREAM: standard option of streaming data through the streams
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #(arg1:family, arg2:type)
server.bind(ADDR) #bound socket to the address in ADDR

#- this function is created to handle all communication between client and server. It is able to 
#  handle individual connection between client and server
def handle_client(conn, addr):
    print(f"[NEW CONNECTION] {addr} connected.")

    connected = True
    while connected:
        msg_length = conn.recv(HEADER).decode(FORMAT) #we will not pass this line of code until we receive a message from client
        if msg_length:
            msg_length = int(msg_length) 
            msg = conn.recv(msg_length).decode(FORMAT)
            if msg == DISCONNECT_MESSAGE:
                connected = False

            print(f"[{addr}] {msg}")
            conn.send("Message received".encode(FORMAT))

    conn.close() #after the communication with a client is finished, connection is cleared using close(). 


#	- this function will allow server to start listening for connection. It handles new
#	  connection and distribute those to where they need to go. When a connection happens, the 
#	  handling of those connection will be passed to handle client in a new thread.
#- the while block in this function is set to repeat on loop until we want to stop listening for new 
#   connection or when the server came to a crash.
def start():
    server.listen()
    print(f"[LISTENING] Server is listening on {SERVER}")
    while True: 
        #addr: store IP address and the port it came from of the new connection
        #conn : store actual object that will allow us to send info back to that connection
        conn,addr = server.accept() #wait for a new connection to occur then store the connection address
        
        #when a new connection occurs pass the connection to handle client
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start() #start a new thread

        #tells us how many threads are active are active in this process
        # no. of thread = no. of client. 
        #subtract by one since the start thread is always running
        print(f"[ACTIVE CONNECTIONS] {threading.activeCount() -1}") 
        

print ("[STARTING] server is starting...")
start()