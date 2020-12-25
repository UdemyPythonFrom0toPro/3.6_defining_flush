import sys

table_cards = sys.argv[1] # exemple ["A_S", "J_H", "7_D", "8_D", "10_D"]
hand_cards = sys.argv[2]

flush = any([sum([card[-1] == suit for card in table_cards + hand_cards]) >= 5 for suit in 'CHSD'])
if flush:
  print('Flush!')
else:
  print('No Flush!')
