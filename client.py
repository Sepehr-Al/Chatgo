import time
import sys
import socket as sck

new_socket = sck.socket()
host_name = input(str("Enter the host name: "))
port = 8880

new_socket.connect((host_name, port))
print("Connecting to the server... ")
print("Connected to the chat server!")

while 1:
    incomming_message = new_socket.recv(1024)
    incomming_message = incomming_message.decode()
    print("Server: {}".format(incomming_message))
    message = input(str(">> "))
    Message = message.encode()
    new_socket.send(Message)
    print("Message has been sent.")
