import random
import pytest
from io import StringIO
from unittest.mock import patch
from guess_game import guess_number

# Test the random number generation function (or logic)
def test_random_number_generation():
    random.seed(0)  # Fix the seed to get consistent results for tests
    generated_number = random.randint(1, 100)
    assert generated_number == 50  # Adjust this as per your fixed seed value

# Test the game logic - patching input and output
@patch('builtins.input', side_effect=[50])  # User enters 50
@patch('sys.stdout', new_callable=StringIO)  # Capture the printed output
def test_game_flow(mock_input, mock_stdout):
    guess_number()
    output = mock_stdout.getvalue().strip().lower()
    assert "you've guessed the number" in output
