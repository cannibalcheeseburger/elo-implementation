from .const import ranks
from random import choice,randint
from .classes import player

def generate(num):
    players = []
    for i in range(num):
        play = player(str(i),choice(list(ranks)),str(i))
        play.value = randint(100,2100)
        players.append(play)
    return players