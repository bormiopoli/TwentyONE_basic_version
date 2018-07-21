

class Bank(object):

    def __init__(self):
        self.cards = []
        self.points = 0
        self.status = False
        self.action = None


class Player(object):

    def __init__(self):
        self.name = "No name"
        self.status = False
        self.decks = []


class Table(object):

    def __init__(self):
        self.players = []
        self.id = 0
        self.hand = []
        self.decks = []


class Deck(object):

    def __init__(self):
        self.cards = []
        self.points = 0
        self.status = False
        self.split = False
        self.action = None


