# Карты 3.0
# Демонстрирует наследование в части переопределения методов
class Card():
    """ Одна игральая карта """
    RANKS = ["A","1","2","3","4","5","6","7","8","9","10","J","Q","K"]
    SUITS = ["c","d","h","s"]

    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit

    def __str__(self):
        rep = self.rank + self.suit
        return rep

class Unprintable_Card(Card):
    """ Карта, номинал и масть которой не могут быть выведены на экран """
    def __str__(self):
        return "<Нельзя напечатать>"

class Positionable_Card(Card):
    """ Карта, которую можно положить лицом или рубашкой вверх """
    def __init__(self, rank, suit, face_up = True):
        # Вызывается конструктор надкласса
        super(Positionable_Card, self).__init__(rank, suit)
        self.is_face_up = face_up

class Hand(object):
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
        """ Очистить руку """
        self.cards = []

    def add(self, card):
        """ Добавление карты """
        self.cards.append(card)

    def give(self, card, other_hand):
        """ Отдать карты """
        self.cards.remove(card)
        other_hand.add(card)

class Deck(Hand):
    """ Колода игральных карт """
    def populate(self):
        """ Формирование колоды """
        self.cards = []
        for suit in Card.SUITS:
            for rank in Card.RANKS:
                self.add(Card(rank, suit))

    def shuffle(self):
        """ Перемешивание колоды, переставление карт в случайном порядке """
        import random
        random.shuffle(self.cards)

    def deal(self, hands, per_hand = 1):
        """ Расдача карт """
        for round in range(per_hand):
            for hand in hands:
                if self.cards:
                    top_card = self.cards[0]
                    self.give(top_card, hand)
                else:
                    print("Не могу больше сдавать: карты кончились!")