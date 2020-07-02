from unittest import TestCase

from pyboy.pyboy import PyBoy

from DataManipulation.OpponentPokemonGetter import OpponentPokemonGetter


class TestOpponentPokemonGetter(TestCase):
    def test_read_opponent_pokemon_species_hex(self):
        pyboy_instance = PyBoy('../ROMs/gamerom.gbc')
        opponent_pokemon_getter = OpponentPokemonGetter(pyboy_instance, "base_save_state.state")
        opponent_pokemon_species = opponent_pokemon_getter.read_opponent_pokemon_species_hex()

        self.assertEqual(opponent_pokemon_species, 158, "That is not a Totodile! Expected 158, got {}".format(opponent_pokemon_species))
