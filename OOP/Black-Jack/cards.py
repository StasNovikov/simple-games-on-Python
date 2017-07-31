# Модуль cards
# Набор базовых классов для карточной игры
class Card():
    """ Одна игральная карта """
    RANKS = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
    SUITS = ["c", "d", "h", "s"]

    def __init__(self, rank, suit, face_up = True):
        self.rank = rank
        self.suit = suit
        self.is_face_up = face_up

    def __str__(self):
        if self.is_face_up:
            rep = self.rank + self.suit
        else:
            rep = "XX"
        return rep

    def flip(self):
        """ Изменение значения свойства is_face_up """
        self.is_face_up = not self.is_face_up

class Hand:
    """ 'Рука': набор карт на руках у одного игрока """
    def __init__(self):
        self.cards = []

    def __str__(self):
        if self.cards:
            rep = ""
            for card in self.cards:
                rep += str(card) + "\t"
        else:
            rep = "<пусто>"
        return rep

    def clear(self):
        """ Очитстить руку """
        self.cards = []

    def add(self, card):
        """ Добавить карту в руку """
        self.cards.append(card)

    def give(self, card, other_hand):
        """ Поделиться картой """
        self.cards.remove(card)
        other_hand.add(card)

class Deck(Hand):
    """ Колода игральных карт """

    def populate(self):
        """ Создание колоды карт """
        for suit in Card.SUITS:
            for rank in Card.RANKS:
                self.add(Card(rank, suit))

    def shuffle(self):
        """ Перемешивание колоды карт """
        import random
        random.shuffle(self.cards)

    def deal(self, hands, per_hand = 1):
        """ Сдача карт ишрокам """
        for round in range(per_hand):
            for hand in hands:
                if self.cards:
                    top_card = self.cards[0]
                    self.give(top_card, hand)
                else:
                    print("Не могу больше сдвавать: карты закончились!")

if __name__ == "__main__":
    print("Это модуль, содержащий классы для карточных игр")
    input("\n\nНажмите Enter, чтобы выйти.")