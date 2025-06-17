import random

class Weather():
    def __init__(self):
        self.statuses = ['rainy', 'sunny']

    def how_is_the_weather(self):
        return random.choice(self.statuses)