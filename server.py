import socket
import threading

# create an INET and STREAM socket
# INET for IP4 and STREAM for TCP 
_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


# create a connection
# param one is address param 2 is port
_socket.bind(('localhost', 8080))

_socket.listen(1) 


# create the main loop for the web server
# create an array to keep track of the connections 

connections = []

# create a handler for connections
# mainloop to recieve data
# for each individual connection in connections send the data in bytes over the server(max allowed is      1024 bytes)
# if no data is sent remove the connection from the list, close the client socket and break from the loop
def handler(c, a):
    global connections
    while True: 
        data = c.recv(1024)
        for connection in connections:
            connection.send(bytes(data))
        if not data:
            connections.remove(c)
            c.close()
            break

while True:
    # accept external connections 
    # append the connection to the array 
    (clientSocket, address) = _socket.accept()
    # create thread
    cthread = threading.Thread(target = handler, args = (clientSocket, address))
    cthread.daemon = True     
    cthread.start()
    connections.append(clientSocket)
    print(connections)
    