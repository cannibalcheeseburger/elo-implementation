from math import floor
from .const import ranks

class player:
    def __init__(self, name, rank,username,team="None"):
        self.name = name
        self.rank = rank
        self.value = ranks[rank]
        self.team = team
        self.username = username

    def print_player(self):
        print("Name:",self.name,"\tElo:",self.value,'\tUsername: ',self.username)

    def __str__(self) -> str:
        return self.name

class team:
    def __init__(self,name):
        self.players = []
        self.name = name

    def add_player(self,player):
        self.players.append(player)
        self.get_average()

    def print_team(self):
        print("\n\n","="*5,self.name,"="*5)
        print("Team Average: ",self.rank)
        print("PLAYERS: ")
        for player in self.players:
            player.print_player()

    def get_average(self):
        self.average = sum(p.value for p in self.players) /len(self.players)
        self.rank = get_key_from_value(ranks,floor(self.average))
        return self.rank

    def __str__(self) -> str:
        return self.name

    def is_full(self):
        return not len(self.players)<5

    def overflow(self):
        return len(self.players)>5


def get_key_from_value(d, val):
    keys = [k for k, v in d.items() if v == val]
    if keys:
        return keys[0]
    return None