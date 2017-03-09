import pickle


class Field:
    def __init__(self):
        self.coord = []

    def add(self, x, y):
        self.coord.append({'x': x, 'y': y})


class Data:
    DBNAME = 'db.pickle'

    def __init__(self):
        self.my = Field()
        self.my_boats = Field()
        self.enemy = Field()
        self.turn = 0
        self.player = [1, 2]

        self.data = {
            'my': self.my,
            'enemy': self.enemy,
            'my_boats': self.my_boats,
            'turn': self.turn,
            'player': self.player
        }

    def save(self):
        with open(self.DBNAME, 'wb') as f:
            pickle.dump(self.data, f)

    def load(self):
        with open(self.DBNAME, 'rb') as f:
            self.data = pickle.load(f)

#data = Data()

#data.my.add(1,2)
#data.enemy.add(3,4)
#data.my_boats.add(5,6)
#data.save()
# print(data.my.coord)
