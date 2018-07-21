TWENTYONE BASIC IMPLEMENTATION WITH COMMAND LINE INTERFACE

HOW TO RUN:

The code requires a Python interpreter (3.6) or lower. Once installed the python interpreter, the code can be executed by executing the file "Game.py" from the command line at the same location of where the file is located:

python Game.py


RULES OF THE GAME:

TwentyOne is a game of chance. The chance of winning is based on the cards dealt by the program. The game is similar to Blackjack, but differs in some areas, so please read this section carefully.

All players in the game place their bets after receiving their first card. Once everyone has placed their bets, the participants get a second card.

One by one, the players of the game get the opportunity to play. Each play, the players have the option to ‘stand’ (hold your total and end your turn), ‘hit’ (ask for a card to bring your points as close as possible to 21), or perform special actions (here only ‘split’). If a player has more than 21 points in his hand, he is ‘bust’, and his bets are lost.

If all players are ready (stand or bust) the bank must play (only if there are players who are not bust). The rules for the bank are simple: The bank must hit when it has a total of 16 points or less and must stand with a total of 17 points or more. When the bank and player have the same number of points, the bank wins. If the bank has more than 21 points, the bank is bust and all players that are standing, win.

When a player gets two identical cards, he can choose to ‘split’. This means that the cards are placed next to each other on the table and the player can play twice, one game per card.

The number of points for the cards is as follows:
    • King 3 points, queen 2 points, jack 1 point.
    • Ace is 1 or 11 points of your choice.
    • Cards 2 to 10 have their normal point value.
    • The ‘suit’ of the card is not important.
    • The Joker does not play

Note that the game cards are pre-shuffled and that there cannot be more than 3 players per deck (for more players you will need more than one deck).
Players grouped by 3 are assigned to each table. Spare players (reminder of division of <num> mod <3>, are inserted in the last table.


FURTHER FEATURES:

IF ALL PLAYER PASS, THEN BANK PICKS AND GAME GOES TO THE POINTS
BANK CANNOT SPLIT




