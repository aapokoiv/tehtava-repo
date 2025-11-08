from rich.table import Table
from rich.console import Console
from player_stats import PlayerStats
from player_reader import PlayerReader


def main():
    season = get_season()
    nation = get_nation()

    url = f"https://studies.cs.helsinki.fi/nhlstats/{season}/players"
    reader = PlayerReader(url)
    stats = PlayerStats(reader)
    players = stats.top_scorers_by_nationality(nation)

    console = Console()
    table = Table(title=f"Season {season} players from {nation}")

    table.add_column("Player", style="green")
    table.add_column("Team", style="red")
    table.add_column("Goals", justify="right", style="green")
    table.add_column("Assists", justify="right", style="green")
    table.add_column("Points", justify="right", style="green")

    for player in players[:12]:
        table.add_row(
            f"{player.name}", f"{player.team}",
            f"{player.goals}", f"{player.assists}",
            f"{player.goals + player.assists}"
            )

    console.print(table)

def get_season():
    valid_seasons = [
        "2018-19", "2019-20", "2020-21",
        "2021-22", "2022-23", "2023-24",
        "2024-25", "2025-26"
    ]

    while True:
        season = input(
            "Season: [2018-19/2019-20/2020-21/2021-22/2022-23/2023-24/2024-25/2025-26] "
            ).strip()
        if season in valid_seasons:
            return season
        print("❌ Invalid season. Please enter one of the listed options.")

def get_nation():
    valid_nations = [
        "USA", "FIN", "CAN", "SWE", "CZE", "RUS", "SLO", "FRA", "GBR", "SVK",
        "DEN", "NED", "AUT", "BLR", "GER", "SUI", "NOR", "UZB", "LAT", "AUS"
    ]

    while True:
        nation = input(
            "Nationality: "
            "[USA/FIN/CAN/SWE/CZE/RUS/SLO/FRA/GBR/SVK/DEN/NED/AUT/BLR/GER/SUI/NOR/UZB/LAT/AUS] "
            ).strip().upper()
        if nation in valid_nations:
            return nation
        print("❌ Invalid nationality. Please enter one of the listed codes.")





if __name__ == "__main__":
    main()
