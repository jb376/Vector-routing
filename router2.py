from socket import *
import sys
host = '104.238.130.63'
port = 50011
socket = socket(AF_INET,SOCK_STREAM)##Im using TCP
socket.bind((host, port))
socket.listen(1)

table = {
    
    'destination0': { 'interface': "104.238.130.242", 'Cost': 2},
    'destination1': {'interface': '104.238.129.39', 'Cost': 1},
    'destination2': {'interface': 'Local', 'Cost': 0},
    'destination3': {'interface': '104.238.135.148', 'Cost': 4}}

print ('Socket binding complete')
while 1:
    client, addr = socket.accept()

    print ('Got connection from', addr)
    sentence = client.recv(1024).decode()
    print(sentence)
    table = str(table)
    client.send(table.encode())
    client.close()
else:
    
    client.close()
print('unable to connect')
