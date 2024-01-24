import socket
import threading
import time


class Server:
    Clients = []
    client_msg = {}

    def __init__(self, host, port):
        self.host = host
        self.port = port

        self.network = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.network.bind((self.host, self.port))
        self.network.listen(20)

        print(f'server listen at {self.port}')

    def start(self):
        while True:
            client_sock, client_addr = self.network.accept()
            print(f'client {client_addr} connected')

            client_sock.send('Connected Successfully!'.encode())
            time.sleep(0.1)

            msg = ' '
            for client in Server.Clients:
                msg = msg + ' ' + client.clientID
            client_sock.send(msg.encode('utf-8'))
            client_thread = threading.Thread(target=self.wait_for_user_nickname, args=[client_sock])
            client_thread.start()

    def wait_for_user_nickname(self, client_sock):
        new_user_id = client_sock.recv(128).decode('utf-8')
        print('new user choose nickname: ' + new_user_id)
        client = Client(client_sock, new_user_id)

        for client_ID in Server.client_msg:
            client_msg = Server.client_msg[client_ID]
            client_msg = client_msg.encode('ISO-8859-1')
            client_sock.sendall(client_msg)

            Server.Clients.append(client)
            client.start()
            Server.client_msg[client_ID] += client.msg
            print('new user choose nickname: ' + Server.client_msg)


class Client:
    def __init__(self, sock, clientID):
        self.sock = sock
        self.clientID = clientID
        self._run = True
        Server.client_msg[self.clientID] = ''

    def terminate(self):
        self._run = False

    def start(self):
        while self._run:
            msg = ''
            while True:
                data = self.sock.recv(1).decode('ISO-8859-1')
                msg += data
                if data == 'Ø':
                    break
            if msg[0] == 'D' or msg[0] == 'M':
                self.broadcast2Clients(msg)
            pass

    def broadcast2Clients(self, msg):
        print(msg)
        msgList = msg.split(' ')
        if msgList[0] == 'M':
            msg = msg.replace('&', self.clientID)
        if msgList[0] != 'M':
            Server.client_msg[self.clientID] += msg
        msg = msg.encode('ISO-8859-1')

        for client in Server.Clients:
            if client.clientID == self.clientID and msgList[0] == "M":
                continue
            client.sock.sendall(msg)


if __name__ == '__main__':
    server = Server('0.0.0.0', 6500)
    server.start()
