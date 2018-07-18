import random


def card_value(card, player):
    if card is "A":
        print("player {} picked an Ace, do you wanna give it value as 1 or 11 ?".format(player.name))
        while True:
            try:
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


def shuffle_cards():
    hand = ["A", "A", "A", "A", "2", "2", "2", "2", "3", "3", "3", "3", "4", "4", "4", "4", "5", "5", "5", "5", "6",
            "6", "6", "6", "7", "7", "7", "7", "8", "8", "8", "8", "9", "9", "9", "9", "10", "10", "10", "10", "J", "J",
            "J", "J", "Q", "Q", "Q", "Q", "K", "K", "K", "K"]
    return hand


def remove_card(list,card):
    try:
        list.remove(card)
    except Exception as exc:
        print (exc)


def check_limit(player):
    if player.points > 21:
        player.status = True
        return True
    return False


def bank_check(table):
    if table.bank.points < 17:
        return True
    return False


def bankpick(table):
    bank_pick = pick_card(table.hand)
    table.bank.cards.append(bank_pick)
    table.bank.points = int(table.bank.points) + int(card_value(bank_pick, table.bank))
    print("Bank at table {0} have {1} points".format(table.id, table.bank.points))
    print("Bank at table {0} have cards: {1}".format(table.id,table.bank.cards))


def finish(table):
    if len(table.players) == 0:
            print("Bank WON at table {}".format(table.id))
            return True
    if check_limit(table.bank):
        print("Bank lost at table {}".format(table.id))
        return True
    return False


def check_score(table):
    bank_p = table.bank.points
    winners = []
    for player in table.players:
        if ((player.points <= 21) and (player.points > bank_p)) or bank_p > 21:
            winners.append(player)
    return winners


def take_action(player, action):
    if "Hit" in action:
        player.action = "Hit"
    if "Stay" in action:
        player.action = "Stay"
    if "Split" in action:
        player.action = "Split"




