import socket

from UserDialog import UserDialog


class Connection:
    def __init__(self):
        # UserDialog.getUserInputIp()
        self.host = '127.0.0.1'
        self.port = 6500
        # print(self.host, self.port)

        self.sock = socket.socket()
        self.sock.connect((self.host, self.port))
        data = self.sock.recv(24).decode()
        print(data)

        usernames = self.sock.recv(1024).decode('utf-8')
        userList = usernames.split()
        print('users: %s' % userList)

        while True:
            UserDialog.getUserNickName()
            self.nickname = UserDialog._nickname
            if self.nickname in userList:
                UserDialog.show_error_box('User name already exists, please change one!')
            else:
                break

        self.sock.sendall((self.nickname.encode('utf-8')))

    def send_message(self, msg):
        msg = ' '.join(map(str, msg))
        msg = msg + " Ø"
        try:
            print("Sent message: %s" % msg)
            msg = msg.encode('ISO-8859-1')
            self.sock.send(msg)
            # print("Sent message: %s" % msg)
        except UnicodeEncodeError:
            pass

    def receive_msg(self):
        msg = ''
        while True:
            data = self.sock.recv(1).decode('ISO-8859-1')
            if data == 'ß':
                print('recived:' + data)
                continue
            elif data == 'Ø':
                break
            else:
                pass

            msg += data

        return msg


if __name__ == '__main__':
    conn = Connection()
    conn.receive_msg()
    print('start')
