from unittest import TestCase

from pyboy.pyboy import PyBoy

from DataManipulation.OpponentPokemonGetter import OpponentPokemonGetter
from DataManipulation.PokemonEditor import PokemonEditor


class TestPokemonEditor(TestCase):
    def test_change_enemy_pokemon_to_mew(self):
        pyboy_instance = PyBoy('../ROMs/gamerom.gbc')

        altered_state = open("altered_save_state.state", "r+b")
        pokemon_editor = PokemonEditor(pyboy_instance)
        pokemon_editor.edit_opponent_pokemon(0, 'MEW')
        pyboy_instance.save_state(altered_state)
        opponent_pokemon_getter = OpponentPokemonGetter(pyboy_instance)
        actual_hex = opponent_pokemon_getter.read_opponent_pokemon_species_hex()
        altered_state.close()

        self.assertEqual(actual_hex, 151)

    def test_change_enemy_second_pokemon_to_chansey(self):
        pyboy_instance = PyBoy('../ROMs/gamerom.gbc')

        altered_state = open("altered_save_state.state", "r+b")
        pokemon_editor = PokemonEditor(pyboy_instance)
        pokemon_editor.edit_opponent_pokemon(1, 'CHANSEY')
        pyboy_instance.save_state(altered_state)
        actual_hex = pyboy_instance.get_memory_value(56717)
        altered_state.close()

        self.assertEqual(actual_hex, 113)

    def test_change_enemy_third_pokemon_to_articuno(self):
        pyboy_instance = PyBoy('../ROMs/gamerom.gbc')

        altered_state = open("altered_save_state.state", "r+b")
        pokemon_editor = PokemonEditor(pyboy_instance)
        pokemon_editor.edit_opponent_pokemon(2, 'ARTICUNO')
        pyboy_instance.save_state(altered_state)
        actual_hex = pyboy_instance.get_memory_value(56765)
        altered_state.close()

        self.assertEqual(actual_hex, 144)

    def test_change_player_first_pokemon_to_mewtwo(self):
        pyboy_instance = PyBoy('../ROMs/gamerom.gbc')

        altered_state = open("altered_save_state.state", "r+b")
        pokemon_editor = PokemonEditor(pyboy_instance)
        pokemon_editor.edit_player_pokemon_species(0, 'MEWTWO')
        pyboy_instance.save_state(altered_state)
        actual_hex = pyboy_instance.get_memory_value(55850)
        altered_state.close()

        self.assertEqual(actual_hex, 150)

    def test_change_opponent_pokemon_first_move_to_ice_beam(self):
        pyboy_instance = PyBoy('../ROMs/gamerom.gbc')

        altered_state = open("altered_save_state.state", "r+b")
        pokemon_editor = PokemonEditor(pyboy_instance)
        pokemon_editor.edit_opponent_pokemon(0, 'ARTICUNO')
        pokemon_editor.edit_opponent_pokemon_move(0, 0, 58)
        pyboy_instance.save_state(altered_state)
        actual_hex = pyboy_instance.get_memory_value(56671)
        altered_state.close()

        self.assertEqual(actual_hex, 58)

    def test_change_player_pokemon_first_move_to_psychic(self):
        pyboy_instance = PyBoy('../ROMs/gamerom.gbc')

        altered_state = open("altered_save_state.state", "r+b")
        pokemon_editor = PokemonEditor(pyboy_instance)
        pokemon_editor.edit_player_pokemon_species(0, 'MEWTWO')
        pokemon_editor.edit_player_pokemon_move(0, 0, 'PSYCHIC')
        pyboy_instance.save_state(altered_state)
        actual_hex = pyboy_instance.get_memory_value(55852)
        altered_state.close()

        self.assertEqual(actual_hex, 94)

    def test_assign_player_pokemon_correct_stats_level_20_bulbasaur(self):
        pyboy_instance = PyBoy('../ROMs/gamerom.gbc')

        altered_state = open("altered_save_state.state", "r+b")
        pokemon_editor = PokemonEditor(pyboy_instance)
        pokemon_editor.assign_player_pokemon(0, 'BULBASAUR', 20, 'VINE_WHIP', 'ICE_BEAM', 'GROWL', "WING_ATTACK")
        pyboy_instance.save_state(altered_state)
        hp_hex = pyboy_instance.get_memory_value(55887)
        atk_hex = pyboy_instance.get_memory_value(55889)
        def_hex = pyboy_instance.get_memory_value(55891)
        satk_hex = pyboy_instance.get_memory_value(55895)
        sdef_hex = pyboy_instance.get_memory_value(55897)
        spd_hex = pyboy_instance.get_memory_value(55893)
        altered_state.close()

        self.assertEqual(hp_hex, 48)
        self.assertEqual(atk_hex, 24)
        self.assertEqual(def_hex, 24)
        self.assertEqual(satk_hex, 31)
        self.assertEqual(sdef_hex, 31)
        self.assertEqual(spd_hex, 23)
