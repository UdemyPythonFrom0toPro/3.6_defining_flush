# Defining Flush
A game of seven-card Texas poker is in progress. There are five cards on the table and two cards in hand.
It is necessary to determine if there is a combination called Flush.
A flush combination is determined by the presence of five cards of the same suit (among all cards: both those that are on the table and those in the hand)

There are two variables in your solution file: table_cards and hand_cards.

Both variables contain lists of cards, the first contains five cards on the table, and the second contains two cards in hand.

Here are examples of lists that will be written to these variables to test your solution:

["A_S", "J_H", "7_D", "8_D", "10_D"], ["J_D", "3_D"]

["10_S", "7_S", "9_H", "4_S", "3_S"], ["K_S", "Q_S"]

["3_S", "10_H", "10_D", "10_C", "10_S"], ["3_S", "4_D"]

As you can see, each card is written in a specific format.
The first symbol indicates the "face value" of the card.
Possible values: 2, 3, 4, 5, 6, 7, 8, 9, 10, J, Q, K, A
The second character is always an underscore.
The third character is a suit. Possible values: S (spades), H (hearts), D (diamonds), C (clubs)

If there is a flash combination, output "Flush!" To the console, otherwise output "No Flush!"
