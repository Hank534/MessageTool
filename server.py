import socket
"""
This program is creating a server on a localhost 
and will listen for clients trying to connect to it.
The socket will have the buffer space for 5 connections.
"""
# takes TCP or UPD, defualt is IPV4 TCP
soc = socket.socket()
print('Socket Created....')
# must be a tuple data type
soc.bind(('localhost', 9919))
# allocating buffer size of 5 connections 
soc.listen(2)
size = 2
print("Waiting for connections....")

while size > 0:
    connections, addr = soc.accept()
    data_connection = connections.getsockname()
    print('The following address has been bounded to the connection via =>', addr)
    print('='*80)
    print('Connection made with the following socket object => ', data_connection)
    print('='*80)
    connections.send(bytes('Thank you for connecting to the LGC repo! ', 'utf-8'))
    connections.send(bytes('The socket object has been created', 'utf-8'))
    connections.close()
    size -= 1
    