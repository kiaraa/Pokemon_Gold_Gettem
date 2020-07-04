from collections import namedtuple


class Trainer:

    def __init__(self, name: object, category: object, id: object, location: object, party_size: object, party: object) -> object:
        self.name = name
        self.category = category
        self.id = id
        self.location = location
        self.party_size = party_size
        self.party = party

    def get_name(self):
        return self.name

    def get_category(self):
        return self.category

    def get_id(self):
        return self.id

    def get_location(self):
        return self.location

    def get_party_size(self):
        return self.party_size

    def get_party(self):
        return self.party
