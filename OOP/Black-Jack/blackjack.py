# Блек-Джек
# От 1 до 7 игроков против дилера
import cards, games

class BJ_Card(cards.Card):
    """ Карта для игры в Блек-Джек """
    ACE_VALUE = 1

    @property
    def value(self):
        if self.is_face_up:
            v = BJ_Card.RANKS.index(self.rank) + 1
            if v > 10:
                v = 10
        else:
            v = None
        return v

class BJ_Deck(cards.Deck):
    """ Колода для игры в Блек-Джек """
    def populate(self):
        for suit in BJ_Card.SUITS:
            for rank in BJ_Card.RANKS:
                self.cards.append(BJ_Card(rank, suit))


class BJ_Hand(cards.Hand):
    """ 'Рука': набор карт "Блек-Джека" у одного игрока """
    def __init__(self, name):
        super(BJ_Hand, self).__init__()
        self.name = name

    def __str__(self):
        rep = self.name + ":\t" + super(BJ_Hand, self).__str__()
        if self.total:
            rep += "(" + str(self.total) + ")"
        return rep

    @property
    def total(self):
        # если у одной из карт value равно None, то и всё свойство равно None
        for card in self.cards:
            if not card.value:
                return None
        # суммируем очки, считая каждый туз за 1 очко
        t = 0
        for card in self.cards:
            t += card.value
        # определяем, есть ли туз на руках у игрока
        contains_ace = False
        for card in self.cards:
            if card.value == BJ_Card.ACE_VALUE:
                contains_ace = True

        # если на руках есть туз и сумма очков не превышает 11, считаем туз за 11 очков
        if contains_ace and t <= 11:
            # прибавить нужно лишь 10, потому что единица уже вошла в общую сумму
            t += 10
        return t

    def is_busted(self):
        return self.total > 21

class BJ_Player(BJ_Hand):
    """ Игрок в "Блек-Джек" """

    def is_hitting(self):
        """ Определяет нужно ли тянуть ещё карту """
        response = games.ask_yes_no("\n" + self.name + ", будете брать ещё карты? (Y/N): ")
        return response == "y"

    def bust(self):
        """ Перебор """
        print(self.name, " перебрал.")
        self.lose()

    def lose(self):
        """ Проиграл """
        pass

