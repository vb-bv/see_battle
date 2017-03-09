import socket
from threading import Thread
from queue import Queue

class NetInterface:

    HOST = ''
    PORT = 50010

    def __init__(self, ip=''):
        self.q = Queue()
        srv_thread = Thread(target=self.listen)
        srv_thread.start()
        self.ip = ip

    def listen(self):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.bind((self.HOST, self.PORT))
            s.listen(1)
            while True:
                conn, addr = s.accept()
                if not self.ip:
                    self.ip = addr[0]
                with conn:
                    data = conn.recv(1024).decode('utf-8')
                    self.q.put(data)

    def send(self, data:str):
        data = data.encode('utf-8')
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect((self.ip, self.PORT))
            s.sendall(data)

if __name__ == '__main__':
    client = NetInterface()
    print(client.q.get())
    client.send('server send')








