import json

from Beans.Trainer import Trainer


class TrainerEditor:
    # This class is responsible for parsing trainer JSON data and updating the ROM values, mostly by
    # calling PokemonEditor methods

    def __init__(self):
        self.trainer_data_str = "../res/trainer_data.json"

    def get_trainer_object(self, trainer_id):
        file = open(self.trainer_data_str, "rb")
        data = json.load(file)

        trainer_data = data["trainers"][trainer_id]
        trainer = Trainer(name=trainer_data["name"], category=trainer_data["category"], id=trainer_data["id"], location=trainer_data["location"], party_size=trainer_data["party_size"], party=trainer_data["pokemon"])

        return trainer



# for testing
if __name__ == '__main__':
    editor = TrainerEditor()
    print(editor.get_trainer_object(0))
