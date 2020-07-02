from unittest import TestCase

from pyboy.pyboy import PyBoy

from DataManipulation.OpponentPokemonGetter import OpponentPokemonGetter
from DataManipulation.PokemonEditor import PokemonEditor


class TestPokemonEditor(TestCase):
    def test_change_enemy_pokemon_to_mew(self):
        pyboy_instance = PyBoy('../ROMs/gamerom.gbc')

        altered_state = open("altered_save_state.state", "r+b")
        pokemon_editor = PokemonEditor(pyboy_instance)
        pokemon_editor.edit_opponent_pokemon(0, 151)
        pyboy_instance.save_state(altered_state)
        opponent_pokemon_getter = OpponentPokemonGetter(pyboy_instance)
        actual_hex = opponent_pokemon_getter.read_opponent_pokemon_species_hex()
        altered_state.close()

        self.assertEqual(actual_hex, 151)

    def test_change_enemy_second_pokemon_to_chansey(self):
        pyboy_instance = PyBoy('../ROMs/gamerom.gbc')

        altered_state = open("altered_save_state.state", "r+b")
        pokemon_editor = PokemonEditor(pyboy_instance)
        pokemon_editor.edit_opponent_pokemon(1, 113)
        pyboy_instance.save_state(altered_state)
        actual_hex = pyboy_instance.get_memory_value(56663)
        altered_state.close()

        self.assertEqual(actual_hex, 113)
