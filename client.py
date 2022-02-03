# my client
import socket 

c = socket.socket()
c.connect(('localhost',9919))
# print(c.recv(1024).decode())
# print(c.recv(1024).decode())

data = c.recv(1024).decode()
data2 = c.recv(1024).decode()
#data3 = c.recv(1024).decode()


file1 = open("Report.txt", "ab")
file1.write(data.encode())
file1.write(data2.encode())
#file1.write(data3)
file1.close()