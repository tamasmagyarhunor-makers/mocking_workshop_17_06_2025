from lib.door import Door
from lib.person import Person

def test_door_instantiates():
    door = Door()

    assert door.people == []

def test_door_opens_if_attempted_to_open():
    door = Door()
    person = Person('Mihai', 55)

    assert door.open(person) == True

def test_door_opens_if_attempted_to_open_2():
    door = Door()
    person = Person('Sarah', 2)

    assert door.open(person) == True