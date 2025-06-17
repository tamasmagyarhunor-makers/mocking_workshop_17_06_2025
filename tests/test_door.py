from lib.door import Door
# from lib.person import Person
from unittest.mock import Mock


def test_door_instantiates():
    door = Door()

    assert door.people == []

def test_door_opens_if_attempted_to_open():
    door = Door()
    person = Mock()
    person.try_open_door.return_value = True

    assert door.open(person) == True

def test_door_opens_if_attempted_to_open_2():
    door = Door()
    person = Mock()
    person.try_open_door.return_value = False

    assert door.open(person) == False