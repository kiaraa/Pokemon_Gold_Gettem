import io

from pyboy.pyboy import PyBoy, WindowEvent


class PokemonEditor:

    def __init__(self, pyboy_instance):
        self.pyboy_instance = pyboy_instance
        self.state_name = "altered_save_state.state"
        # self.state_name = "../ROMs/gamerom.gbc.state"
        self.pyboy_instance.load_state(open(self.state_name, "rb"))


    def edit_opponent_pokemon(self, party_slot, species_hex):
        party_slot_address = {
            0: 56662,
            1: 56717,
            2: 56765,
            3: 56813,
            4: 56861,
            5: 56909
        }
        self.pyboy_instance.set_memory_value(party_slot_address[party_slot], species_hex)

    #TODO -- Change name to species name as well
    def edit_player_pokemon_species(self, party_slot, species_hex):
        party_slot_address = {
            0: 55850,
            1: 55898,
            2: 55946,
            3: 55994,
            4: 56042,
            5: 56090
        }
        self.pyboy_instance.set_memory_value(party_slot_address[party_slot], species_hex)

    def edit_opponent_pokemon_move(self, party_slot, move_slot, move_hex):
        move_slot_address = {
            0: {0: 56671, 1: 56672, 2: 56673, 3: 56674},
            1: {0: 56719, 1: 56720, 2: 56721, 3: 56722},
            2: {0: 56767, 1: 56768, 2: 56769, 3: 56770},
            3: {0: 56815, 1: 56816, 2: 56817, 3: 56818},
            4: {0: 56863, 1: 56864, 2: 56865, 3: 56866},
            5: {0: 56911, 1: 56912, 2: 56913, 3: 56914}
        }
        self.pyboy_instance.set_memory_value(move_slot_address[party_slot][move_slot], move_hex)

    def edit_player_pokemon_move(self, party_slot, move_slot, move_hex):
        move_slot_address = {
            0: {0: 55852, 1: 55853, 2: 55854, 3: 55855},
            1: {0: 55900, 1: 55901, 2: 55902, 3: 55903},
            2: {0: 55948, 1: 55949, 2: 55950, 3: 55951},
            3: {0: 55996, 1: 55997, 2: 55998, 3: 55999},
            4: {0: 56044, 1: 56045, 2: 56046, 3: 56047},
            5: {0: 56092, 1: 56093, 2: 56094, 3: 56095}
        }
        self.pyboy_instance.set_memory_value(move_slot_address[party_slot][move_slot], move_hex)

#testing
if __name__ == '__main__':

    pyboy = PyBoy('../ROMs/gamerom.gbc')
    poke_editor = PokemonEditor(pyboy)
    # state = open("../DataManipulation/base_save_state.state", "rb")
    state = open("../DataManipulation/altered_save_state.state", "rb")
    pyboy.load_state(state)

    for i in range(31):
        pyboy.tick()

    poke_editor.edit_player_pokemon_species(0, 1)
    poke_editor.edit_player_pokemon_move(0, 0, 126)
    poke_editor.edit_player_pokemon_move(0, 1, 86)
    pyboy.set_memory_value(55881, 100)


    pyboy.send_input(WindowEvent.PRESS_BUTTON_A)
    for i in range(31):
        pyboy.tick()

    pyboy.send_input(WindowEvent.RELEASE_BUTTON_A)

    #enemy stats are altered on species and level, player are not

    for i in range(250):
        pyboy.tick()

    poke_editor.edit_opponent_pokemon(0, 161)
    poke_editor.edit_opponent_pokemon_move(0, 0, 45)
    poke_editor.edit_opponent_pokemon_move(0, 0, 45)
    poke_editor.edit_opponent_pokemon_move(0, 0, 45)
    poke_editor.edit_opponent_pokemon_move(0, 0, 45)
    pyboy.set_memory_value(56700, 100)
    print("written")




    while not pyboy.tick():
        pass
