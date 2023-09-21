import pytest
from src.levelup.character import Character

class Character:
    DEFAULT_NAME: str = "Jane Doe"
    name_from_user: str = "Tierna"

    game_character = Character()

    def initialize_character_with_default_name(self, DEFAULT_NAME):
        self.DEFAULT_NAME = DEFAULT_NAME

    def initialize_character_name_from_user(self, name_from_user):
        self.name_from_user = name_from_user

    def test_default_name(self, expected):
        name = self.game_character.name
        assert name == self.DEFAULT_NAME
    
    def test_character_name(self, expected):
        name = self.game_character.name
        assert name == self.name_from_user
        