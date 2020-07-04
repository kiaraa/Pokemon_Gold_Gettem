import io

from pyboy.pyboy import PyBoy


class PokemonEditor:

    def __init__(self, pyboy_instance):
        self.pyboy_instance = pyboy_instance
        self.state_name = "altered_save_state.state"
        self.pyboy_instance.load_state(open(self.state_name, "rb"))

    #TODO -- Once opponent party slots are editable, finish this method
    def edit_opponent_pokemon(self, party_slot, species_hex):
        if party_slot == 0:
            self.pyboy_instance.set_memory_value(56662, species_hex)
        else:
            self.pyboy_instance.set_memory_value(56663, species_hex)


