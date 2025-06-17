from lib.weather import Weather

def test_weather_instantiates():
    weather = Weather()

    assert weather.statuses == ['rainy', 'sunny']

# def test_weather_is_rainy():
#     weather = Weather()

#     assert weather.how_is_the_weather() == "It's rainy, lets bring umbrella!"

# def test_weather_is_sunny():
#     weather = Weather()

#     assert weather.how_is_the_weather() == "It's sunny, lets take sunglasses!"
















    from unittest.mock import patch

    def test_weather_is_rainy():
        weather = Weather()
        with patch('random.choice', return_value='rainy'):
            actual = weather.how_is_the_weather()

        assert actual == "It's rainy, lets bring umbrella!"

    def test_weather_is_sunny():
        weather = Weather()

        with patch('random.choice', return_value='sunny'):
            actual = weather.how_is_the_weather()

        assert actual == "It's sunny, lets take sunglasses!"