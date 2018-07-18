
from table_schedule import create_tables
from rules import bankpick,finish,remove_card, sum_points
from rules import card_value, check_tables, pick_card, check_limit, bank_check, check_score


def first_pick(tab):
    for play in tab.players:
        card = pick_card(tab.hand)
        play.cards.append(card)
        print("{} picked a card".format(play.name))
        remove_card(tab.hand, card)
        add_points = card_value(card, play)
        play.points = sum_points(add_points, play.points)
        print(play.name)
        print(play.cards, play.points)




def second_pick(tab):
    for play in tab.players:
        card = pick_card(tab.hand)
        play.cards.append(card)
        print("{} picked a card".format(play.name))
        remove_card(tab.hand, card)
        add_points = card_value(card, play)
        play.points = sum_points(add_points, play.points)
        print(play.name)
        print(play.cards, play.points)


def first_bet(tab):
    for play in tab.players:
        print("{}... Now insert the bet amount [Integer Value] or <pass> to pass the turn".format(play.name))
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


def define_action(tab):
    for play in tab.players:
        if play.status is False:
            while True:
                print("Insert the action for play {}".format(play.name))
                play.action = input()
                if "Hit" in play.action or "Pass" in play.action:
                    break
                if "Split" in play.action:
                    print("Please reinsert <Hit> or <Pass> or <Split>")


def last_pick(tab):
    for playe in tab.players:
        if "Hit" in playe.action:
            card = pick_card(tab.hand)
            playe.cards.append(card)
            print("{} picked a card".format(playe.name))
            remove_card(tab.hand, card)
            add_points = card_value(card, playe)
            playe.points = sum_points(add_points, playe.points)
            if check_limit(playe):
                tab.players.remove(playe)
                print("playe {} is out of game".format(playe.name))
            print(playe.cards, playe.points)

        if finish(tab) is True:
            break
        if "Pass" in playe.action:
            continue
        if "Split" in playe.action:
            print("Split not yet implemented")


if __name__ == '__main__':
    while True:
        i=0  # NR OF TABLE PLAYING
        players = []
        num = ""
        while True:
            print("Insert the number of players - an Integer")
            try:
                num = int(input())
                break
            except:
                print("Please Insert an Integer Value")

        num_of_tables = check_tables(num)
        tables = create_tables(num_of_tables, num)

        for table in tables:
            first_pick(table)

        for table in tables:
            bankpick(table)
            first_bet(table)

        for table in tables:
            second_pick(table)

        for table in tables:
            while True:
                define_action(table)
                p=[]
                for player in table.players:
                    if "Pass" in player.action:
                        p.append("Pass")
                if len(p) is len(table.players):
                    break
                last_pick(table)

        for table in tables:
            while bank_check(table) is True:
                bankpick(table)
            winners = check_score(table)
            if len(winners) is 0:
                print("Bank WON at the point in table {}".format(table.id))
            for winner in winners:
                print("Player {0} won with SCORE: {1} and CARDS: {2} ".format(winner.name, winner.points, winner.cards))

        print("Do you want to play again ?  [Yes] = <Yes> otherwise any key = <No> ")
        inp = input()
        if "Yes" not in inp:
            break




