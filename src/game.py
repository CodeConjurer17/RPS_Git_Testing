"""
Rock Paper Scissors game logic.
"""

import random

CHOICES = ["rock", "paper", "scissors"]


def get_computer_choice() -> str:
    """Return a random choice for the computer."""
    return random.choice(CHOICES)


def determine_winner(player: str, computer: str) -> str:
    """
    Determine the winner of a round.

    Returns 'player', 'computer', or 'draw'.
    """
    if player not in CHOICES:
        raise ValueError(f"Invalid choice: {player}. Must be one of {CHOICES}")
    if computer not in CHOICES:
        raise ValueError(f"Invalid choice: {computer}. Must be one of {CHOICES}")

    if player == computer:
        return "draw"

    wins_against = {
        "rock": "scissors",
        "scissors": "paper",
        "paper": "rock",
    }

    if wins_against[player] == computer:
        return "player"
    return "computer"


def get_result_message(winner: str, player: str, computer: str) -> str:
    """Return a human-readable result message."""
    if winner == "draw":
        return f"It's a draw! You both chose {player}."
    if winner == "player":
        return f"You win! {player.capitalize()} beats {computer}."
    return f"Computer wins! {computer.capitalize()} beats {player}."


class GameSession:
    """Tracks score across multiple rounds."""

    def __init__(self):
        self.player_score = 0
        self.computer_score = 0
        self.draws = 0
        self.rounds = 0

    def play_round(self, player_choice: str) -> str:
        """Play one round and update scores. Returns result message."""
        computer_choice = get_computer_choice()
        winner = determine_winner(player_choice, computer_choice)

        self.rounds += 1
        if winner == "player":
            self.player_score += 1
        elif winner == "computer":
            self.computer_score += 1
        else:
            self.draws += 1

        return get_result_message(winner, player_choice, computer_choice)

    def get_score(self) -> dict:
        """Return current score as a dictionary."""
        return {
            "player": self.player_score,
            "computer": self.computer_score,
            "draws": self.draws,
            "rounds": self.rounds,
        }