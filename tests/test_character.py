from unittest import TestCase
from levelup.character import Character

class Character(TestCase):
    DEFAULT_NAME: str = "Jane Doe"
    name_from_user: str = "Tierna"

    game_character_default_name = Character()
    game_character_user_name = Character(name_from_user)

    def initialize_character_with_default_name(self, DEFAULT_NAME):
        self.DEFAULT_NAME = DEFAULT_NAME

    def initialize_character_name_from_user(self, name_from_user):
        self.name_from_user = name_from_user

    def test_default_name(self):
        name = self.game_character_default_name.name
        assert name == self.DEFAULT_NAME
    
    def test_character_name(self):
        name = self.game_character_user_name.name
        assert name == self.name_from_user
        
    def test_get_name(self):
        name = self.game_character_user_name.get_name()
        assert name == self.name_from_user
