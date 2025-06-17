from lib.person import Person

def test_person_instantiates():
    person = Person("Anamarie", 33)

    assert person.name == "Anamarie"
    assert person.age == 33

def test_person_can_try_open_door_with_success():
    person = Person("Anamarie", 33)

    assert person.try_open_door() == True

def test_person_fails_to_open_door_if_less_than_3_years_old():
    person = Person("Alex", 2)

    assert person.try_open_door() == False