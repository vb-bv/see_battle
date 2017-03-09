import socket
from threading import Thread
from queue import Queue

class NetInterface:

    HOST = ''
    SRV_PORT = 50010
    CL_PORT = 50005

    def __init__(self, ip):
        q = Queue()
        srv_thread = Thread(target=self.listen, args=q, )
        srv_thread.start()
        self.ip = ip

    def listen(self, q:Queue):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.bind((self.HOST, self.SRV_PORT))
            s.listen(1)
            while True:
                conn, addr = s.accept()
                with conn:
                    print('Connected by', addr)#123
                    q.put(conn.recv(1024).decode('utf-8'))

    def send(self, data:str):
        data = data.encode('utf-8')
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect((self.ip, self.CL_PORT))
            s.sendall(data)






