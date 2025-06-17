class Door():
    def __init__(self):
        self.people = []

    def open(self, person):
        return person.try_open_door()