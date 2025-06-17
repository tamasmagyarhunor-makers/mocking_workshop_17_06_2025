from lib.person import Person

def test_person_instantiates():
    person = Person("Anamarie", 33)

    assert person.name == "Anamarie"
    assert person.age == 33

def test_person_can_try_open_door_with_success():
    person = Person("Anamarie", 33)

    assert person.try_open_door() == True