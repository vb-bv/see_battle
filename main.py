# coding: utf-8
'''
---- Sea battle ----

Main program file.

'''
from api.NetAPI import NetInterface
from data.main import Data
#from gui import SomeGui ## ???

def main():
    input('''

Hello! I am the game - @Sea battle@
    by python curs 2016-2017. IFMO.



Click Enter to start.

    ''')    

    api_type = None
    while not api_type:
        answer = input('''

Print your choice. You are:

    1 - [c]lient
    2 - [s]erver

    ''')
        if answer in ('1', 'c'):
            start_client()
            api_type = 'client'
        elif answer in ('2', 's'):
            start_server()
            api_type = 'server'

def start_client():
    server, port = None, None
    while True:
        addr = input('Print server address (like 192.168.0.1:8888): ')
        #print(f'..answer: {addr}')
        lst = addr.split(':')
        if len(lst) == 2:
            server, port = lst
            if not port.isnumeric():
                print(f'Oooops... Wrong port: {port}')
                continue
            srv_list = server.split('.')
            if len(srv_list)!= 4 or not all( s.isnumeric() for s in srv_list ):
                print(f'Oooops... Wrong server: {server}')
                continue
            print(f'OK. You are connecting to: {server}:{port}...')
            break
        else:
            print(f'Oooops... Wrong answer: {addr}')

def start_server():
    pass

if __name__=='__main__':
    main()