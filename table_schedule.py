from classes import Table, Bank, Player
from rules import shuffle_cards


def create_tables(num_of_tables, num):
    tables = []
    i = 0
    while i+1 <= num_of_tables:
        table = Table()
        bank = Bank()
        if i + 1 is num_of_tables:
            if num%3 == 0:
                for m in range(3):
                    print("Insert the name of player {}".format(i*3 + m + 1))
                    name = input()
                    player = Player()
                    player.name = name
                    table.players.append(player)
                table.hand = shuffle_cards()
                table.id = i + 1
                bank.name = "Bank"
                bank.status = False
                table.bank = bank
                tables.append(table)
                if (i*3 + m + 1) == num:
                    break

            if (num-i*3)%2 == 0 and (num-i*3)//2 == 1:
                for m in range(2):
                    print("Insert the name of player {}".format(i*3 + m + 1))
                    name = input()
                    player = Player()
                    player.name = name
                    table.players.append(player)
                table.hand = shuffle_cards()
                table.id = i + 1
                bank.name = "Bank"
                bank.status = False
                table.bank = bank
                tables.append(table)
                if i*3 + m + 1 == num:
                    break

            if ((num-3*i)//1) == 1:
                for m in range(1):
                    print("Insert the name of player {}".format(i*3 + m + 1))
                    name = input()
                    player = Player()
                    player.name = name
                    table.players.append(player)
                table.hand = shuffle_cards()
                table.id = i + 1
                bank.name = "Bank"
                bank.status = False
                table.bank = bank
                tables.append(table)
                if (i*3 + m + 1) == num:
                    break
        else:
            for m in range(3):
                print("Insert the name of player {}".format(i*3 + m + 1))
                name = input()
                player = Player()
                player.name = name
                table.players.append(player)
            table.hand = shuffle_cards()
            table.id = i + 1
            bank.name = "Bank"
            bank.status = False
            table.bank = bank
            tables.append(table)
            i = i + 1

        # else:
        #     table = Table()
        #     bank = Bank()
        #     for j in range(num % 3):
        #         print("Insert the name of player {}".format(i*3 + j + 1))
        #         name = input()
        #         player = Player()
        #         player.name = name
        #         table.players.append(player)
        #     table.hand = shuffle_cards()
        #     table.id = i + 1
        #     bank.name = "Bank"
        #     bank.status = False
        #     table.bank = bank
        #     tables.append(table)
        #     i = i + 1
    return tables
