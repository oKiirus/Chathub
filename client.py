import socket
from threading import Thread

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

nickname = input("Enter nickname here: ")
ip = "127.0.0.1"
port = 1111

client.connect((ip, port))

print("Connected to server")

def receive():
    while(True):
        try:
            message = client.recv(2048).decode("utf-8")
            if message == "NICKNAME":
                client.send(nickname.encode("utf-8"))
            else:
                print(message)
        except:
            print("ERROR")
            client.close()
            break

def send():
    while(True):
        message = nickname + ": " + input("Message: ")
        client.send(message.encode('utf-8'))

receiveThread = Thread(target=receive)
receiveThread.start()
       
sendThread = Thread(target=send)
sendThread.start()
