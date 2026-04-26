"""
Unit tests for Rock Paper Scissors game logic.
"""

import unittest
from src.game import determine_winner, get_result_message, get_computer_choice, GameSession


class TestDetermineWinner(unittest.TestCase):

    def test_draw(self):
        self.assertEqual(determine_winner("rock", "rock"), "draw")
        self.assertEqual(determine_winner("paper", "paper"), "draw")
        self.assertEqual(determine_winner("scissors", "scissors"), "draw")

    def test_player_wins(self):
        self.assertEqual(determine_winner("rock", "scissors"), "player")
        self.assertEqual(determine_winner("scissors", "paper"), "player")
        self.assertEqual(determine_winner("paper", "rock"), "player")

    def test_computer_wins(self):
        self.assertEqual(determine_winner("scissors", "rock"), "computer")
        self.assertEqual(determine_winner("paper", "scissors"), "computer")
        self.assertEqual(determine_winner("rock", "paper"), "computer")

    def test_invalid_player_choice_raises(self):
        with self.assertRaises(ValueError):
            determine_winner("banana", "rock")

    def test_invalid_computer_choice_raises(self):
        with self.assertRaises(ValueError):
            determine_winner("rock", "banana")


class TestGetResultMessage(unittest.TestCase):

    def test_draw_message(self):
        msg = get_result_message("draw", "rock", "rock")
        self.assertIn("draw", msg.lower())

    def test_player_win_message(self):
        msg = get_result_message("player", "rock", "scissors")
        self.assertIn("win", msg.lower())

    def test_computer_win_message(self):
        msg = get_result_message("computer", "scissors", "rock")
        self.assertIn("computer", msg.lower())


class TestGetComputerChoice(unittest.TestCase):

    def test_returns_valid_choice(self):
        for _ in range(20):
            choice = get_computer_choice()
            self.assertIn(choice, ["rock", "paper", "scissors"])


class TestGameSession(unittest.TestCase):

    def setUp(self):
        self.session = GameSession()

    def test_initial_score_is_zero(self):
        score = self.session.get_score()
        self.assertEqual(score["player"], 0)
        self.assertEqual(score["computer"], 0)
        self.assertEqual(score["rounds"], 0)

    def test_rounds_increase_after_play(self):
        self.session.play_round("rock")
        self.assertEqual(self.session.get_score()["rounds"], 1)

    def test_score_adds_up_over_multiple_rounds(self):
        for _ in range(5):
            self.session.play_round("rock")
        score = self.session.get_score()
        total = score["player"] + score["computer"] + score["draws"]
        self.assertEqual(total, 5)
