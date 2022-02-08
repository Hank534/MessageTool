import socket
import os.path
import threading
"""
This program is creating a server on a localhost 
and will listen for clients trying to connect to it.
The socket will have the buffer space for 5 connections.

"""
HEADER = 2048
PORT = 9119
SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER, PORT)
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = '!DISCONNECT'
SEPARATOR = '<SEPERATE>'
FILE_FINISHED_SENDING = '<!FILE_SENT!>'

server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.bind(ADDR)


def handle_client(conn, addr):
    print(f'[NEW CONNECTION] {addr} connected.')
    connected = True
    current_file = None

    while connected:
        data = conn.recv(HEADER).decode(FORMAT)
        if data == DISCONNECT_MESSAGE:
            connected = False
        elif data == FILE_FINISHED_SENDING:
            current_file.close()
            current_file = None
            conn.send(b'file received.')
        else:
            data = data.split(SEPARATOR)
            if len(data) == 2 and data[1] == '':
                # The name of the file was sent, more will follow.
                current_file = open(data[0], 'w')
                conn.send(b'filename recieved')
            else:
                # File data was send, so write it to the current file
                current_file.write(data[1])
                print('chunk of file recv''d')
                conn.send(b'chunk received')
    conn.close()
    print(f'[DISCONNECT] {addr} disconnected')

def start():
    server.listen()
    print(f'[LISTENING] Server is listening on {SERVER}')
    while True:
        conn, addr = server.accept()
        thread = threading.Thread(target=handle_client, args=(conn,addr))
        thread.start()
        print(f'[ACTIVE CONNECTIONS] {threading.activeCount()-1}')


print("[STARTING] server is starting...")
start()