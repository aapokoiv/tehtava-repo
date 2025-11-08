class Player:
    def __init__(self, data):
        self.name = data['name']
        self.nation = data['nationality']
        self.assists = data['assists']
        self.goals = data['goals']
        self.team = data['team']

    def __str__(self):
        return f"{self.name:20}"
