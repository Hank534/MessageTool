# my client
import socket
from pathlib import Path

HEADER = 2048
PORT = 9119
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = '!DISCONNECT'
SEPARATOR = '<SEPERATE>'
FILE_FINISHED_SENDING = '<!FILE_SENT!>'
SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER, PORT)

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)

def chunker(string: str, size: int):
    return (string[pos:pos + size] for pos in range(0, len(string), size))


def send(msg):
    message = msg.encode(FORMAT)
    client.send(message)
    print(client.recv(HEADER).decode(FORMAT))


def send_file(filepath: str):
    with open(filepath, 'r', encoding=FORMAT) as f:
        data = f.read()

    first_bits = f'{Path(filepath).name}{SEPARATOR}'  # Easy way of getting just a file's name from its path
    send(first_bits)  # Send the filename to the server
    for chunk in chunker(data, HEADER-48):  # Leave a safe buffer
        # Send each chunk of the file
        send(f"{SEPARATOR}{chunk}")

    # Tell the server that's all for this file.
    # Now it can close the file object.
    send(FILE_FINISHED_SENDING)


send_file("C:/Users/J91307/Desktop/Projects/.ipynb_checkpoints/MessageTool/demo.txt")
send(DISCONNECT_MESSAGE)
# c = socket.socket()
# c.connect(('localhost',9919))
# # print(c.recv(1024).decode())
# # print(c.recv(1024).decode())

# data = c.recv(1024).decode()
# data2 = c.recv(1024).decode()
# #data3 = c.recv(1024).decode()


# file1 = open("Report.txt", "ab")
# file1.write(data.encode())
# file1.write(data2.encode())
# #file1.write(data3)
# file1.close()