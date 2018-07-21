
from table_schedule import create_tables
from rules import bankpick, finish, remove_card, split, last_pick, define_action, check_limit
from rules import check_tables, pick_card, check_score, bank_check, first_pick, first_bet

# This function allow each player of a table to pick a card from the same hand,
# it then updates the cards and points of each player and display stats


if __name__ == '__main__':

    # To keep the game running...

    while True:
        i = 0  # NR OF TABLE PLAYING
        num = 1
        while True:
            print("Insert the number of players - an Integer")
            try:
                num = int(input())
                break
            except:
                print("Please Insert an Integer Value")

        num_of_tables = check_tables(num)                   #CHECK THE NR OF TABLES FROM DIVSION BY 3
        tables = create_tables(num_of_tables, num)          # CREATE EACH TABLE AND INITIALIZE PLAYERS AND DECKS

        # FIRST RUN ONE CARD

        for table in tables:
            first_pick(table)

        # BANKPICK ONE CARD AND PLAYER BET

        for table in tables:
            bankpick(table)
            first_bet(table)

        # MOVE SOME OBJECTS FROM TABLE SCHEDULING OF BEFORE, TO BE ABLE TO SCROLL THROUGH DECK AND NOT PLAYERS

        for table in tables:
            first_pick(table)
            for player in table.players:
                name = player.name
                for deck in player.decks:
                    deck.player = name
                    table.decks.append(deck)

        # LOOP UNTIL NO DECKS LEFT OR UNTIL ALL DECKS PASSED

        for table in tables:
            while len(table.decks) >= 0 and finish(table) is False:
                p = []
                for deck in table.decks:
                    # if check_limit(deck) is True:
                    #     table.decks.remove(deck)
                    #     continue
                    deck.action = define_action(deck)
                    if "Pass" in deck.action:
                        p.append(1)
                        continue
                    if "Split" in deck.action:
                        new_deck = split(deck)
                        if new_deck is not None:
                            table.decks.append(new_deck)
                    if "Hit" in deck.action:
                        card = pick_card(table.hand)
                        remove_card(table.hand, card)
                        last_pick(deck, card)

                    if check_limit(deck) is True:
                        table.decks.remove(deck)
                        print("Player {0} is out of game".format(deck.player))
                        continue

                    if len(p) == len(table.decks):
                        break

                if len(p) == len(table.decks):
                    break

                if finish(table) is True:
                    break

        # SCROLL THROUGH TABLES TO COMPARE SCORES AND CHECK THE WINNER

        for table in tables:
            if len(table.decks) == 0:
                print("Bank WON!")
                break
            while bank_check(table) is True:
                bankpick(table)
            winners = check_score(table)
            if len(winners) is 0:
                print("Bank WON at the point in table {}".format(table.id))
            for winner in winners:
                print("Player {0} won with SCORE: {1} and CARDS: {2} ".format(winner.player, winner.points, winner.cards))

        # ASK TO CONTINUE THE PROGRAM RUNNING, RESTARTING THE GAME

        print("Do you want to play again ?  <Yes> For yes or any other key to exit ")
        inp = input()
        if "Yes" not in inp:
            break




