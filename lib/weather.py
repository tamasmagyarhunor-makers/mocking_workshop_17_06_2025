import random

class Weather():
    def __init__(self):
        self.statuses = ['rainy', 'sunny']

    def how_is_the_weather(self):
        if random.choice(self.statuses) == 'rainy':
            return "It's rainy, lets bring umbrella!"
        else:
            return "It's sunny, lets take sunglasses!"