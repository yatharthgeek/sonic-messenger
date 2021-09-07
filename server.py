print("""
░██████╗░█████╗░███╗░░██╗██╗░█████╗░
██╔════╝██╔══██╗████╗░██║██║██╔══██╗
╚█████╗░██║░░██║██╔██╗██║██║██║░░╚═╝
░╚═══██╗██║░░██║██║╚████║██║██║░░██╗
██████╔╝╚█████╔╝██║░╚███║██║╚█████╔╝
╚═════╝░░╚════╝░╚═╝░░╚══╝╚═╝░╚════╝░

███╗░░░███╗███████╗░██████╗░██████╗███████╗███╗░░██╗░██████╗░███████╗██████╗░
████╗░████║██╔════╝██╔════╝██╔════╝██╔════╝████╗░██║██╔════╝░██╔════╝██╔══██╗
██╔████╔██║█████╗░░╚█████╗░╚█████╗░█████╗░░██╔██╗██║██║░░██╗░█████╗░░██████╔╝
██║╚██╔╝██║██╔══╝░░░╚═══██╗░╚═══██╗██╔══╝░░██║╚████║██║░░╚██╗██╔══╝░░██╔══██╗
██║░╚═╝░██║███████╗██████╔╝██████╔╝███████╗██║░╚███║╚██████╔╝███████╗██║░░██║
╚═╝░░░░░╚═╝╚══════╝╚═════╝░╚═════╝░╚══════╝╚═╝░░╚══╝░╚═════╝░╚══════╝╚═╝░░╚═╝ SERVER 1.0""")

import socket
import threading
insert=input("Host >> ")
# Connection Data
host = insert
port = 55555
print("Server Started on Port :",port)

# Starting Server
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((host, port))
server.listen(5)

# Lists For Clients and Their usernames
clients = []
usernames = []



# Sending Messages To All Connected Clients
def broadcast(message):
    for client in clients:
        client.send(message)


# Handling Messages From Clients
def handle(client):
    while True:
        try:
            # Broadcasting Messages
            message = client.recv(1024)
            broadcast(message)
        except:
            # Removing And Closing Clients
            index = clients.index(client)
            clients.remove(client)
            client.close()
            username = usernames[index]
            broadcast('{} left!'.format(username).encode('ascii'))
            usernames.remove(username)
            break

# Receiving / Listening Function
def receive():
    while True:
        # Accept Connection
        client, address = server.accept()
        print("Connected with {}".format(str(address)))

        # Request And Store Nickname
        client.send('USER'.encode('ascii'))
        username = client.recv(1024).decode('ascii')
        usernames.append(username)
        clients.append(client)

        # Print And Broadcast Nickname
        print("Username is {}".format(username))
        broadcast("{} joined!".format(username).encode('ascii'))
        client.send('Connected to server!'.encode('ascii'))

        # Start Handling Thread For Client
        thread = threading.Thread(target=handle, args=(client,))
        thread.start()

receive()
