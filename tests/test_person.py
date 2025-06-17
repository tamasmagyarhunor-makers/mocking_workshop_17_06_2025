def test_person_instantiates():
    person = Person("Anamarie", 33)

    assert person.name == "Anamarie"
    assert person.age == 33