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

    def __send(self, data:str):
        data = data.encode('utf-8')
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect((self.ip, self.PORT))
            s.sendall(data)
            
    def send_point(self, data:str):
        self.__send(data)
        
    def send_answer(self, data:str):
        self.__send(data)
        
    def get_answer(self):
        return self.q.get()
    
    def get_poinr(self):
        return self.q.get()

if __name__ == '__main__':
    client = NetInterface('192.168.0.8')
    client.send('sadads')
    print(client.q.get())

