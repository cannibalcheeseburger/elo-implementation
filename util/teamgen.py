from .const import ranks
from random import choice,randint
from .classes import team
from .playergen import generate

def generateteam(num):
    players = generate(5*num)
    teams = []
    i = 0
    for i in range(num):
        t = team(str(i))
        for play in players[:5]:
            t.add_player(play)
            players.remove(play)
        teams.append(t)
        i = i+1
    return teams