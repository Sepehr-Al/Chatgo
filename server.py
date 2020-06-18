import sys
import socket as sck
import time

# Create new socket
new_socket = sck.socket()
# Get the host name
host_name = sck.gethostname()
print("Server will start on the : {} host.".format(host_name))
port = 8880

try :
    # Bind the host and the port
    new_socket.bind((host_name, port))
    print("Server is binding....")
    print("Server is bind successfully!")
    print("Server is waiting for new connection...")
except Exception as e :
    # Raise an message if there is any error
    print("There is an error occured here. If you are the developer the error is : {}".format(e))

# Socket listening
new_socket.listen(port)
# Connection created
connection, address = new_socket.accept()
print("{} Has connected to the server and is online...".format(address))

while 1:
    # Get a message from user in STRING
    display_mess = input(str(">>"))
    # Encode the message
    display_mess = display_mess.encode()
    # Send the message
    connection.send(display_mess)
    print("Message has been sent.")
    # The buffer size
    in_meesage = connection.recv(1024)
    # Decode the message
    in_meesage = in_meesage.decode()    
    print(" Client: {}".format(in_meesage))
