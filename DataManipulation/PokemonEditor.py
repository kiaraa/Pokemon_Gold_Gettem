import csv

from pyboy.pyboy import PyBoy, WindowEvent


class PokemonEditor:

    def __init__(self, pyboy_instance):
        self.pyboy_instance = pyboy_instance
        self.state_name = "altered_save_state.state"
        # self.state_name = "../ROMs/gamerom.gbc.state"
        self.pyboy_instance.load_state(open(self.state_name, "rb"))
        self.opponent_pokemon_species_slot_addresses = {
            0: 56662,
            1: 56717,
            2: 56765,
            3: 56813,
            4: 56861,
            5: 56909
        }

        self.player_slot_info_dict = {
            0: {
                'species': int('DA2A', 16),
                'max hp': int('DA4F', 16),
                'attack': int('DA51', 16),
                'defense': int('DA53', 16),
                'sp attack': int('DA57', 16),
                'sp defense': int('DA59', 16),
                'speed': int('DA55', 16),
                'move 1': int('DA2C', 16),
                'move 2': int('DA2D', 16),
                'move 3': int('DA2E', 16),
                'move 4': int('DA2F', 16),
                'move 1 pp': int('DA41', 16),
                'move 2 pp': int('DA42', 16),
                'move 3 pp': int('DA43', 16),
                'move 4 pp': int('DA44', 16),
                'current hp': int('DA4D', 16),
                'level': int('DA49', 16),
                'experience': int('DA34', 16)
            },
            1: {
                'species': int('DA5A', 16),
                'max hp': int('DA7F', 16),
                'attack': int('DA81', 16),
                'defense': int('DA83', 16),
                'sp attack': int('DA87', 16),
                'sp defense': int('DA89', 16),
                'speed': int('DA85', 16),
                'move 1': int('DA5C', 16),
                'move 2': int('DA5D', 16),
                'move 3': int('DA5E', 16),
                'move 4': int('DA5F', 16),
                'move 1 pp': int('DA71', 16),
                'move 2 pp': int('DA72', 16),
                'move 3 pp': int('DA73', 16),
                'move 4 pp': int('DA74', 16),
                'current hp': int('DA7D', 16),
                'level': int('DA79', 16),
                'experience': int('DA64', 16)
            },
            2: {
                'species': int('DA8A', 16),
                'max hp': int('DAAF', 16),
                'attack': int('DAB1', 16),
                'defense': int('DAB3', 16),
                'sp attack': int('DAB7', 16),
                'sp defense': int('DAB9', 16),
                'speed': int('DAB5', 16),
                'move 1': int('DA8C', 16),
                'move 2': int('DA8D', 16),
                'move 3': int('DA8E', 16),
                'move 4': int('DA8F', 16),
                'move 1 pp': int('DAA1', 16),
                'move 2 pp': int('DAA2', 16),
                'move 3 pp': int('DAA3', 16),
                'move 4 pp': int('DAA4', 16),
                'current hp': int('DAAD', 16),
                'level': int('DAA9', 16),
                'experience': int('DA94', 16)
            },
            3: {
                'species': int('DABA', 16),
                'max hp': int('DADF', 16),
                'attack': int('DAE1', 16),
                'defense': int('DAE3', 16),
                'sp attack': int('DAE7', 16),
                'sp defense': int('DAE9', 16),
                'speed': int('DAE5', 16),
                'move 1': int('DABC', 16),
                'move 2': int('DABD', 16),
                'move 3': int('DABE', 16),
                'move 4': int('DABF', 16),
                'move 1 pp': int('DAD1', 16),
                'move 2 pp': int('DAD2', 16),
                'move 3 pp': int('DAD3', 16),
                'move 4 pp': int('DAD4', 16),
                'current hp': int('DADD', 16),
                'level': int('DAD9', 16),
                'experience': int('DAC4', 16)
            },
            4: {
                'species': int('DAEA', 16),
                'max hp': int('DB0F', 16),
                'attack': int('DB11', 16),
                'defense': int('DB13', 16),
                'sp attack': int('DB17', 16),
                'sp defense': int('DB19', 16),
                'speed': int('DB15', 16),
                'move 1': int('DAEC', 16),
                'move 2': int('DAED', 16),
                'move 3': int('DAEE', 16),
                'move 4': int('DAEF', 16),
                'move 1 pp': int('DB01', 16),
                'move 2 pp': int('DB02', 16),
                'move 3 pp': int('DB03', 16),
                'move 4 pp': int('DB04', 16),
                'current hp': int('DB0D', 16),
                'level': int('DB09', 16),
                'experience': int('DAF4', 16)
            },
            5: {
                'species': int('DB1A', 16),
                'max hp': int('DB3F', 16),
                'attack': int('DB41', 16),
                'defense': int('DB43', 16),
                'sp attack': int('DB47', 16),
                'sp defense': int('DB49', 16),
                'speed': int('DB45', 16),
                'move 1': int('DB1C', 16),
                'move 2': int('DB1D', 16),
                'move 3': int('DB1E', 16),
                'move 4': int('DB1F', 16),
                'move 1 pp': int('DB31', 16),
                'move 2 pp': int('DB32', 16),
                'move 3 pp': int('DB33', 16),
                'move 4 pp': int('DB34', 16),
                'current hp': int('DB3D', 16),
                'level': int('DB39', 16),
                'experience': int('DB24', 16)
            }
        }

        self.pokemon_data_dict = {}
        with open('../res/pokemon_hex_values.csv', 'r') as pkmn_data:
            csv_reader = csv.reader(pkmn_data)
            for row in csv_reader:
                info_dict = {'hex' : row[1], 'hp': row[2], 'atk': row[3], 'def': row[4], 'spatk': row[5], 'spdef': row[6],
                             'spd': row[7]}

                self.pokemon_data_dict[row[0]] = info_dict

         #TODO -- add pp to csv and to this dict
        self.move_data_dict = {}
        with open('../res/move_hex_values.csv', 'r') as move_data:
            csv_reader = csv.reader(move_data)
            for row in csv_reader:
                info_dict = {'hex': row[1]}

                self.move_data_dict[row[0]] = info_dict

    def edit_opponent_pokemon(self, party_slot, species_name):
        species_hex = str(self.pokemon_data_dict[species_name]['hex'])
        species_dec = int(species_hex, 16)

        self.pyboy_instance.set_memory_value(self.opponent_pokemon_species_slot_addresses[party_slot], species_dec)

    #TODO -- Change name to species name as well
    def edit_player_pokemon_species(self, party_slot, species_name):
        species_hex = str(self.pokemon_data_dict[species_name]['hex'])
        species_dec = int(species_hex, 16)

        self.pyboy_instance.set_memory_value(self.player_slot_info_dict[party_slot]['species'], species_dec)

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

    def edit_player_pokemon_move(self, party_slot, move_slot, move_name):
        move_hex = str(self.move_data_dict[move_name]['hex'])
        move_dec = int(move_hex, 16)

        move_key = "move " + str((move_slot + 1))

        self.pyboy_instance.set_memory_value(self.player_slot_info_dict[party_slot][move_key], move_dec)

#TODO -- assign player name
    def assign_player_pokemon(self, party_slot, species_name, level, move_1, move_2, move_3, move_4):
        self.edit_player_pokemon_species(party_slot, species_name)
        self.assign_player_stats(party_slot, species_name, level)
        self.assign_player_current_hp(party_slot, species_name, level)
        self.assign_player_level(party_slot, level)
        self.assign_player_moves(party_slot, move_1, move_2, move_3, move_4)

    def calculate_hp_stat(self, species_name, level):
        base_hp = self.pokemon_data_dict[species_name]['hp']

        numerator = int(base_hp) * 2 * int(level)
        fraction = numerator / 100
        calculated_hp = fraction + level + 10
        return int(calculated_hp)

    def calculate_non_hp_stat(self, species_name, level, stat):
        base_stat = self.pokemon_data_dict[species_name][stat]

        numerator = int(base_stat) * 2 * int(level)
        fraction = numerator / 100
        calculated_stat = fraction + 5

        return int(calculated_stat)

#TODO -- account for stat values over 255
    def assign_player_stats(self, party_slot, species_name, level):
        hp = self.calculate_hp_stat(species_name, level)
        atk = self.calculate_non_hp_stat(species_name, level, 'atk')
        defense = self.calculate_non_hp_stat(species_name, level, 'def')
        spatk = self.calculate_non_hp_stat(species_name, level, 'spatk')
        sdef = self.calculate_non_hp_stat(species_name, level, 'spdef')
        spd = self.calculate_non_hp_stat(species_name, level, 'spd')

        self.pyboy_instance.set_memory_value(self.player_slot_info_dict[party_slot]['max hp'], hp)
        self.pyboy_instance.set_memory_value(self.player_slot_info_dict[party_slot]['attack'], atk)
        self.pyboy_instance.set_memory_value(self.player_slot_info_dict[party_slot]['defense'], defense)
        self.pyboy_instance.set_memory_value(self.player_slot_info_dict[party_slot]['sp attack'], spatk)
        self.pyboy_instance.set_memory_value(self.player_slot_info_dict[party_slot]['sp defense'], sdef)
        self.pyboy_instance.set_memory_value(self.player_slot_info_dict[party_slot]['speed'], spd)

    def assign_player_current_hp(self, party_slot, species_name, level):
        current_hp = self.calculate_hp_stat(species_name, level)
        self.pyboy_instance.set_memory_value(self.player_slot_info_dict[party_slot]['current hp'], current_hp)

    def assign_player_level(self, party_slot, level):
        self.pyboy_instance.set_memory_value(self.player_slot_info_dict[party_slot]['level'], level)

    def assign_player_moves(self, party_slot, move_1, move_2, move_3, move_4):
        slot_1_address = self.player_slot_info_dict[party_slot]['move 1']
        slot_2_address = self.player_slot_info_dict[party_slot]['move 2']
        slot_3_address = self.player_slot_info_dict[party_slot]['move 3']
        slot_4_address = self.player_slot_info_dict[party_slot]['move 4']

        move_1_hex = self.move_data_dict[move_1]['hex']
        move_2_hex = self.move_data_dict[move_2]['hex']
        move_3_hex = self.move_data_dict[move_3]['hex']
        move_4_hex = self.move_data_dict[move_4]['hex']

        self.pyboy_instance.set_memory_value(slot_1_address, int(str(move_1_hex), 16))
        self.pyboy_instance.set_memory_value(slot_2_address, int(str(move_2_hex), 16))
        self.pyboy_instance.set_memory_value(slot_3_address, int(str(move_3_hex), 16))
        self.pyboy_instance.set_memory_value(slot_4_address, int(str(move_4_hex), 16))


#TODO -- make pokemon start with their max hp

#testing
if __name__ == '__main__':

    pyboy = PyBoy('../ROMs/gamerom.gbc')
    poke_editor = PokemonEditor(pyboy)
    # state = open("../DataManipulation/base_save_state.state", "rb")
    state = open("../DataManipulation/altered_save_state.state", "rb")
    pyboy.load_state(state)

    for i in range(31):
        pyboy.tick()

#TODO -- account for null attack values
    poke_editor.assign_player_pokemon(0, 'DRAGONITE', 20, 'FIRE_PUNCH', 'BLIZZARD', 'THUNDER_WAVE', 'TOXIC')

    pyboy.send_input(WindowEvent.PRESS_BUTTON_A)
    for i in range(31):
        pyboy.tick()

    pyboy.send_input(WindowEvent.RELEASE_BUTTON_A)

    #enemy stats are altered on species and level, player are not

    for i in range(250):
        pyboy.tick()

    poke_editor.edit_opponent_pokemon(0, 'SENTRET')
    poke_editor.edit_opponent_pokemon_move(0, 0, 45)
    poke_editor.edit_opponent_pokemon_move(0, 0, 45)
    poke_editor.edit_opponent_pokemon_move(0, 0, 45)
    poke_editor.edit_opponent_pokemon_move(0, 0, 45)
    pyboy.set_memory_value(56700, 100)
    print("written")

    while not pyboy.tick():
        pass
