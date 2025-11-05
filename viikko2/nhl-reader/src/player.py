class Player:
    def __init__(self, dict):
        self.name = dict['name']
        self.nation = dict['nationality']
        self.assists = dict['assists']
        self.goals = dict['goals']
        self.team = dict['team']

    def __str__(self):
        return f"{self.name:20}"
