import unittest
from statistics_service import StatisticsService
from player import Player

class PlayerReaderStub:
    def get_players(self):
        return [
            Player("Semenko", "EDM", 4, 12),  #  4+12 = 16
            Player("Lemieux", "PIT", 45, 54), # 45+54 = 99
            Player("Kurri",   "EDM", 37, 53), # 37+53 = 90
            Player("Yzerman", "DET", 42, 56), # 42+56 = 98
            Player("Gretzky", "EDM", 35, 89)  # 35+89 = 124
        ]

class TestStatisticsService(unittest.TestCase):
    def setUp(self):
        self.stats = StatisticsService(PlayerReaderStub())

    def test_search_finds_existing_player(self):
        player = self.stats.search("Gretzky")
        self.assertEqual(player.name, "Gretzky")

    def test_search_returns_none_when_player_not_found(self):
        player = self.stats.search("Unknown")
        self.assertIsNone(player)

    def test_team_returns_all_players_in_team(self):
        team = self.stats.team("EDM")
        self.assertEqual(len(team), 3)
        self.assertTrue(all(p.team == "EDM" for p in team))

    def test_team_returns_empty_list_if_team_not_found(self):
        team = self.stats.team("NYR")
        self.assertEqual(len(team), 0)

    def test_top_returns_correct_number_of_players(self):
        top_players = self.stats.top(2)
        self.assertEqual(len(top_players), 3)

    def test_top_returns_players_sorted_by_points_descending(self):
        top_players = self.stats.top(2)
        points = [p.points for p in top_players]
        self.assertEqual(points, sorted(points, reverse=True))

    def test_top_0_returns_top_player_only(self):
        top_players = self.stats.top(0)
        self.assertEqual(len(top_players), 1)
        self.assertEqual(top_players[0].name, "Gretzky")