test_hands = [
    "AC 5C 10C 7C 3S",
    "2C 3D 4S 5H 2D",
    "2C 3D 4S 3H 2D",
    "5S 4C AD 4S 4H",
    "3H 7H 6S 4D 5S",
    "AC 5C 10C 7C 3C",
    "5C 8D 5H 8S 8H",
    "3D 7H 7S 7C 7D",
    "AS 10S QS KS JS",
]


def suit(card):         # para sacar el simbolo
    return card[-1]

def value(card):        # para sacar el valor
    if(card[0]=="A"):
        return 14

    if(card[0]=="J"):
        return 11

    if(card[0]=="Q"):
        return 12

    if(card[0]=="K"):
        return 13

    if(card[0]=="T"):
        return 10

    return(int(card[0:-1]))     # retorna un número que va desde el cero hasta antes del último caracter


def is_flush(cards):        # verifica si es que es verdadero o falso que el primer 'suit' es igual hasta el último suit de la cadena de texto --- si todos los suits de esa cadena son iguales
    return all([suit(card)==suit(cards[0]) for card in cards[1:]])

def hand_dist(cards):       # en un rango de del 1 al 14 se crea una grupo de distribución, donde por cada 'carta' en 'cartas' de un 'simbolo' se suma 1 siendo que si no hay nada se queda en 0
  dist = {i:0 for i in range(1, 15)}
  for card in cards:
    dist[value(card)] += 1
  dist[1] = dist[14]
  return dist

def straight_high_card(cards):      # si valor en un rango del 1 al 10 tiene como 1 de 'carta' en 'cartas' de corrido, es una escalera
  dist = hand_dist(cards)
  for value in range(1, 11):
    if all([dist[value + k] == 1 for k in range(5)]):
      return value + 4
      
  return None


def card_count(cards, num, but=None):
  dist = hand_dist(cards)
  for value in range(2, 15):
    if value == but:
      continue
    if dist[value] == num:
      return value
  return None

def hand_rank(cards):
  cards = cards.split()
  if straight_high_card(cards) is not None and is_flush(cards):
    return 8
  if card_count(cards, 4) is not None:
    return 7
  if card_count(cards, 3) is not None and card_count(cards, 2) is not None:
    return 6
  if is_flush(cards):
    return 5
  if straight_high_card(cards) is not None:
    return 4
  if card_count(cards, 3) is not None:
    return 3
  pair1 = card_count(cards, 2)
  if pair1 is not None:
    if card_count(cards, 2, but=pair1) is not None:
      return 2
    return 1
  return 0

def print_comparasion(hand1, hand2, winner):
  result = "\nIt\'s a draw!"
  hands_print = hand1 + " = " + hand2 + "\n"
  if winner == -1:
    result = "\nHand 1 wins"
    hands_print = hand1 + " defeats " + hand2 + "\n"
  
  if winner == 1:
    result = "\nHand 2 wins"
    hands_print = hand2 + " defeats " + hand1 + "\n"

  print (result)
  print (hands_print)


def compare_hands(hand1, hand2):
  score_hand1 = hand_rank(hand1)
  score_hand2 = hand_rank(hand2)
  result = 0
  if score_hand1 < score_hand2:
    result = -1
  if score_hand1 > score_hand2:
    result = 1
  # Need to add test for high cards - tie breakers
  return result

def showdown(hand1, hand2):
  result = compare_hands(hand1, hand2)
  print_comparasion(hand1, hand2, result)

showdown(test_hands[1], test_hands[1])
