class TennisGame:
    SCORE_NAMES = ["Love", "Fifteen", "Thirty", "Forty"]
    MIN_ADVANTAGE_SCORE = 4

    def __init__(self, player1_name, player2_name):
        self.player1_name = player1_name
        self.player2_name = player2_name
        self.player1_points = 0
        self.player2_points = 0

    def won_point(self, player_name):
        if player_name == self.player1_name:
            self.player1_points += 1
        else:
            self.player2_points += 1

    def get_score(self):
        if self._is_tied():
            return self._tied_score()

        if self._is_endgame():
            return self._endgame_score()

        return self._regular_score()
    

    def _is_tied(self):
        return self.player1_points == self.player2_points
    

    def _is_endgame(self):
        return (self.player1_points >= self.MIN_ADVANTAGE_SCORE or
                self.player2_points >= self.MIN_ADVANTAGE_SCORE)

    def _tied_score(self):
        if self.player1_points < 3:
            return f"{self.SCORE_NAMES[self.player1_points]}-All"
        return "Deuce"

    def _endgame_score(self):
        score_diff = self.player1_points - self.player2_points

        if score_diff == 1:
            return f"Advantage {self.player1_name}"
        if score_diff == -1:
            return f"Advantage {self.player2_name}"
        if score_diff >= 2:
            return f"Win for {self.player1_name}"
        return f"Win for {self.player2_name}"

    def _regular_score(self):
        player1_score = self.SCORE_NAMES[self.player1_points]
        player2_score = self.SCORE_NAMES[self.player2_points]
        return f"{player1_score}-{player2_score}"