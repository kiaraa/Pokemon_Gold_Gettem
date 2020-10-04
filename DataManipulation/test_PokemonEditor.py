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
        actual_hex = pyboy_instance.get_memory_value(56717)
        altered_state.close()

        self.assertEqual(actual_hex, 113)

    def test_change_enemy_third_pokemon_to_articuno(self):
        pyboy_instance = PyBoy('../ROMs/gamerom.gbc')

        altered_state = open("altered_save_state.state", "r+b")
        pokemon_editor = PokemonEditor(pyboy_instance)
        pokemon_editor.edit_opponent_pokemon(2, 144)
        pyboy_instance.save_state(altered_state)
        actual_hex = pyboy_instance.get_memory_value(56765)
        altered_state.close()

        self.assertEqual(actual_hex, 144)

    def test_change_player_first_pokemon_to_mewtwo(self):
        pyboy_instance = PyBoy('../ROMs/gamerom.gbc')

        altered_state = open("altered_save_state.state", "r+b")
        pokemon_editor = PokemonEditor(pyboy_instance)
        pokemon_editor.edit_player_pokemon_species(0, 150)
        pyboy_instance.save_state(altered_state)
        actual_hex = pyboy_instance.get_memory_value(55850)
        altered_state.close()

        self.assertEqual(actual_hex, 150)

    def test_change_opponent_pokemon_first_move_to_ice_beam(self):
        pyboy_instance = PyBoy('../ROMs/gamerom.gbc')

        altered_state = open("altered_save_state.state", "r+b")
        pokemon_editor = PokemonEditor(pyboy_instance)
        pokemon_editor.edit_opponent_pokemon(0, 144)
        pokemon_editor.edit_opponent_pokemon_move(0, 0, 58)
        pyboy_instance.save_state(altered_state)
        actual_hex = pyboy_instance.get_memory_value(56671)
        altered_state.close()

        self.assertEqual(actual_hex, 58)

    def test_change_player_pokemon_first_move_to_psychic(self):
        pyboy_instance = PyBoy('../ROMs/gamerom.gbc')

        altered_state = open("altered_save_state.state", "r+b")
        pokemon_editor = PokemonEditor(pyboy_instance)
        pokemon_editor.edit_player_pokemon_species(0, 150)
        pokemon_editor.edit_player_pokemon_move(0, 0, 94)
        pyboy_instance.save_state(altered_state)
        actual_hex = pyboy_instance.get_memory_value(55852)
        altered_state.close()

        self.assertEqual(actual_hex, 94)
