print("""𝐒𝐎𝐍𝐈𝐂
𝐌𝐄𝐒𝐒𝐄𝐍𝐆𝐄𝐑""")

import socket
import threading

# Username and Host 
username = input("Choose your username: ")
inserth=input("Connection Host >> ")

host= inserth
port= 55555


client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((host, port))


def receive():
    while True:
        try:
           
            message = client.recv(1024).decode('ascii')
            if message == 'USER':
                client.send(username.encode('ascii'))
            else:
                print(message)
        except:
            
            print("An error occured!")
            client.close()
            break



def write():
    while True:
        message = '{}: {}'.format(username, input(''))
        client.send(message.encode('ascii'))

# Starting Threads For Listening And Writing
receive_thread = threading.Thread(target=receive)
receive_thread.start()

write_thread = threading.Thread(target=write)
write_thread.start()


