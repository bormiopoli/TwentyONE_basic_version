

class Bank(object):

    def __init__(self):
        self.cards = []
        self.points = 0
        self.status = False
        self.action = None


class Player(object):

    def __init__(self):
        self.name = "No name"
        self.cards = []
        self.points = 0
        self.balance = 0
        self.status = False
        self.action = None

    def bet(self, amount):
        self.balance = int(self.balance) + int(amount)


class Table(object):

    def __init__(self):
        self.players = []
        self.id = 0
        self.hand = []

