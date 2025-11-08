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

        return self.sort_players(players, sort_by)

    def sort_players(self, players, sort_by):
        def by_points(player):
            return player.goals + player.assists

        def by_goals(player):
            return player.goals

        def by_assists(player):
            return player.assists

        key_func = None
        if sort_by == SortBy.POINTS:
            key_func = by_points
        elif sort_by == SortBy.GOALS:
            key_func = by_goals
        elif sort_by == SortBy.ASSISTS:
            key_func = by_assists
        else:
            raise ValueError(f"Unknown sort type: {sort_by}")

        return sorted(players, reverse=True, key=key_func)
