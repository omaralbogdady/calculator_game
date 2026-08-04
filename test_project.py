import pytest
import sys
from project import parse_input, preamble, Player, Game_Complete, calculate

def test_parse_input():
    assert parse_input("2+2") == 4
    assert parse_input("4-3") == 1

def test_preamble():
    assert preamble() == True

def test_Game_Complete():
    with pytest.raises(SystemExit):
        Game_Complete("CPU")
        Game_Complete("Player")