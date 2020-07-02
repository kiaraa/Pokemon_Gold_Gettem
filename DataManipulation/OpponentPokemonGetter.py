import io
from pyboy.pyboy import PyBoy

class OpponentPokemonGetter:

    def __init__(self, pyboy_instance, state_file_name="altered_save_state.state"):

        self.pyboy_instance = pyboy_instance
        self.state_name = state_file_name
        self.pyboy_instance.load_state(open(self.state_name, "rb"))

    def read_opponent_pokemon_species_hex(self):
        pokemon_hex = self.pyboy_instance.get_memory_value(56662)
        return pokemon_hex

