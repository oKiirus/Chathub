import socket
from threading import Thread

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

ip = "127.0.0.1"
port = 1111

server.bind((ip, port))
server.listen()

clients = []
nicknames = []

print("server is running")

def removeNickname(nickname):
    if nickname in nicknames:
        nicknames.remove(nickname)
        
def remove(client):
    if client in clients:
        clients.remove(client)

def broadcast(message, connection):
    for i in clients:
        if(i != connection):
            try:
                i.send(message.encode("utf-8"))
            except:
                remove(i)


def clientThread(connection, nickname):
    connection.send("Welcome to the Chatroom!".encode("utf-8"))
    while(True):
        try:
            message = connection.recv(2048).decode("utf-8")
            if message:
                
                print(message)
                broadcast(message, connection)
            else:
                remove(connection)
                removeNickname(nickname)
        except:
            continue

while(True):

    connection, address = server.accept()

    connection.send("NICKNAME".encode("utf-8"))
    nickname = connection.recv(2048).decode("utf-8")

    clients.append(connection)
    nicknames.append(nickname)

    print(nickname + " connected")

    newThread = Thread(target=clientThread, args=(connection, address))
    newThread.start()



