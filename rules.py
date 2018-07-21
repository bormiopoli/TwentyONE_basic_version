import random
from classes import Deck


def card_value(card):
    if card is "A":
        while True:
            try:
                print("picked an A, do you wanna give it value 11 or 1 ?")
                val = int(input())
                if (int(val) is 11) or (int(val) is 1):
                    return val
            except:
                print("Please Insert a proper value: 1 or 11")

    if card is "J":
        val = 1
        return val
    if card is "Q":
        val = 2
        return val
    if card is "K":
        val = 3
        return val
    else:
        val = int(card)
        return val


def check_tables(num):
    if num % 3 == 0:
        num_of_tables = num//3
        return num_of_tables
    if (num // 3) >= 0 and num % 3 > 0:
        num_of_tables = num // 3 + 1
        print ("Number of tables : "); print (num_of_tables)
        return num_of_tables


def pick_card(hand):
    picked = random.sample(hand, 1)
    return picked[0]


def sum_points(points_to_add, points_of_player):
    new_points = int(points_of_player) + int(points_to_add)
    return new_points


def subtract_points(points_to_subtract, points_of_deck):
    new_points = int(points_of_deck) - int(points_to_subtract)
    return new_points


def shuffle_cards():
    hand = ["A", "A", "A", "A", "2", "2", "2", "2", "3", "3", "3", "3", "4", "4", "4", "4", "5", "5", "5", "5", "6",
            "6", "6", "6", "7", "7", "7", "7", "8", "8", "8", "8", "9", "9", "9", "9", "10", "10", "10", "10", "J", "J",
            "J", "J", "Q", "Q", "Q", "Q", "K", "K", "K", "K", ]

    return hand


def remove_card(hand, card):
    try:
        hand.remove(card)
        return True
    except Exception as exc:
        print(exc)
        return False


def check_limit(deck):
    if deck.points > 21:
        deck.status = True
        return True
    return False


def bank_check(_table):
    if _table.bank.points < 17:
        return True
    return False


def bankpick(table):
    bank_pick = pick_card(table.hand)
    table.bank.cards.append(bank_pick)
    table.bank.points = int(table.bank.points) + int(card_value(bank_pick))
    print("Bank at table {0} have {1} points".format(table.id, table.bank.points))
    print("Bank at table {0} have cards: {1}".format(table.id, table.bank.cards))
    return True


def finish(table):
    if len(table.decks) == 0:
            print("Bank WON at table {}".format(table.id))
            return True
    if check_limit(table.bank):
        print("Bank lost at table {}".format(table.id))
        return True
    return False


def check_score(table):
    bank_p = table.bank.points
    winners = []
    for deck in table.decks:
        if ((deck.points <= 21) and (deck.points > bank_p)) or bank_p > 21:
            winners.append(deck)
    return winners


def check_split(dck):
    cards_can_split = []
    decks_can_split = []
    if dck.split is True:
        var = set()
        for one_cart in dck:
            if dck.count(one_cart) > 1:
                var.add(one_cart)
        cards_can_split = sorted(var)
        for i in range(len(cards_can_split)):
            if len(cards_can_split[i]) > 0:
                decks_can_split.append(i + 1)
    if dck.split is False:
        var = set()
        for one_card in dck.cards:
            if dck.cards.count(one_card) > 1:
                var.add(one_card)
        cards_can_split = sorted(var)
        if len(cards_can_split) > 0:
            decks_can_split.append(1)

    return cards_can_split, decks_can_split


def split_cards(card, deck):
    if deck.split is False:
        deck.cards.remove(card[0])
        deck.points = subtract_points(card_value(card[0]), deck.points)
        new_deck = Deck()
        new_deck.cards.append(card[0])
        new_deck.player = deck.player
        new_deck.points = card_value(card[0])
        new_deck.status = False
        print("This deck of {0} has split as following: {1}".format(deck.player, deck.cards))
        deck.split = True
        return new_deck
    return None


def split(deck):
    cards_can_split, decks_can_split = check_split(deck)
    if len(decks_can_split) > 1:
        print(
            "Which _deck do you want to split from?  Decks available FOR SPLITTING: {}".format(decks_can_split))
        dck = int(input())
        if len(cards_can_split[dck]) > 1:
            print("Which card do you want to Split with?")
            crd = input()
            new_deck = split_cards(crd, deck)
            return new_deck
        if len(cards_can_split[dck]) == 1:
            new_deck = split_cards(cards_can_split, deck)
            return new_deck
    if len(decks_can_split) is 1:
        if len(cards_can_split) > 1:
            print("Which card do you want to Split with?")
            crd = input()
            new_deck = split_cards(crd, deck)
            return new_deck
        if len(cards_can_split) == 1:
            new_deck = split_cards(cards_can_split, deck)
            return new_deck

    if len(decks_can_split) is 0:
        print("This _deck has no same cards to split")


def last_pick(deck, card):
    if "Hit" in deck.action:
        deck.cards.append(card)
        add_points = card_value(card)
        deck.points = sum_points(add_points, deck.points)
    print(deck.player, deck.cards, deck.points)


def define_action(deck):
    if (deck.status is False) and (deck.action is not "Pass"):
        print("Player {0},  Insert the action for deck with points {1} and cards {2} - "
              "Options: [Hit] or [Pass] or [Split]".format(deck.player, deck.points, deck.cards))
        deck.action = input()
        if ("Hit" in deck.action) or ("Pass" in deck.action) or ("Split" in deck.action):
            return deck.action
        print("No valid action, user is going to pass...")
        return "Pass"


def first_pick(tab):
    for play in tab.players:
        for deck in play.decks:
            card = pick_card(tab.hand)
            deck.cards.append(card)
            print("{} picked a card".format(play.name))
            remove_card(tab.hand, card)
            add_points = card_value(card)
            deck.points = sum_points(add_points, deck.points)
            print(play.name)
            print(deck.cards, deck.points)

# This function allow each player of a table to pick a card from the same hand,
# it then updates the cards and points of each player and display stats


def first_bet(tab):
    for play in tab.players:
        i = 0
        for deck in play.decks:
            i = i + 1
            print("{0}... Now insert the bet amount for deck {1} [Integer Value] or <pass> to pass the turn".format(play.name, i))
            bet = input()
            if bet == "pass":
                continue
            while True:
                try:
                    int(bet)
                    break
                except:
                    print("Please reinsert an integer amount or pass")
                    bet = input()



