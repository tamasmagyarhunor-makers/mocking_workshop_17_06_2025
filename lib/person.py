class Person():
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def try_open_door(self):
        if self.age > 2:
            return True
        return False