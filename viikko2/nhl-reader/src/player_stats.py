import requests
from player import Player
from enum import Enum

class SortBy(Enum):
    POINTS = 1
    GOALS = 2
    ASSISTS = 3

class PlayerStats:
    def __init__(self, reader):
        self._players = reader.get_players()

    def top_scorers_by_nationality(self, nation, sort_by=SortBy.POINTS):
        players = []
        for player in self._players:
            if player.nation == nation:
                players.append(player)

        if sort_by == SortBy.POINTS:
            key_func = lambda player: player.goals + player.assists
        elif sort_by == SortBy.GOALS:
            key_func = lambda player: player.goals
        elif sort_by == SortBy.ASSISTS:
            key_func = lambda player: player.assists
        
        sorted_players = sorted(
            players,
            reverse=True,
            key=key_func
        )

        return sorted_players