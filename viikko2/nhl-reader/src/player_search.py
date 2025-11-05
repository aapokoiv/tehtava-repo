import requests
from player import Player

def main(nation, ordering):
    url = "https://studies.cs.helsinki.fi/nhlstats/2024-25/players"
    response = requests.get(url).json()

    print("JSON-muotoinen vastaus:")
    print(response)

    players = []

    for player_dict in response:
        player = Player(player_dict)
        if player.nation == nation:
            players.append(player)

    print("Oliot:")

    for player in players:
        print(f"{player} team {player.team:15} {player.goals} + {player.assists} = {player.goals + player.assists}")