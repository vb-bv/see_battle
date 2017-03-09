# coding: utf-8
'''
---- Sea battle ----

Main program file.

'''
from api.NetAPI import NetInterface
from data.main import Data
from gui.shoot_handler import Field

data = Data()
field = Field()

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
        server = input('Print server address (like 192.168.0.1): ')
        srv_list = server.split('.')
        if len(srv_list)!= 4 or not all( s.isnumeric() for s in srv_list ):
            print(f'Oooops... Wrong server: {server}')
            continue
        print(f'OK. You are connecting to: {server}:{port}...')
        break
    name = make_my_name()
    api = NetInterface(server)

    api.send_user_name(name)
    opponent = api.get_opponent_name()

    while True:
        make_my_step(op_ships)
        get_his_step(ships)
        data.up_turn()

def make_my_step(op_ships):
    choice = input('Make your choice (like E2): ')
    api.send_point(choice)
    answer = api.get_answer()

def get_his_step(ships):
    opponent_choice = api.get_point()
    # FIXME make answer ???
    api.send_answer(my_answer)
    field.pole(ships)

def start_server():
    name = make_my_name()
    api = NetInterface()

    opponent = api.get_opponent_name()
    api.send_user_name(name)

    while True:
        ship = input('Give me ship:')
        # FIXME when to stop?

    ships, op_ships = [
        [],
        [],
        [],
        #...
    ], [
        [],
        [],
        [],
        #...
    ]

    field.pole(ships)

    while True:
        get_his_step(ships)
        make_my_step(op_ships)

        data.up_turn()


def make_my_name():
    name = ''
    while len(name) == 0:
        name = input('Print your name: ')
    data.set_my_name(name)
    return name
    
def make_my_pole():
    # FIXME draw pole ???

if __name__=='__main__':
    main()