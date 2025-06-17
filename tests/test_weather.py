from lib.weather import Weather

def xtest_weather_instantiates():
    weather = Weather()

    assert weather.statuses == ['rainy', 'sunny']

def xtest_weather_is_rainy():
    weather = Weather()

    assert weather.how_is_the_weather() == "rainy"

def xtest_weather_is_sunny():
    weather = Weather()

    assert weather.how_is_the_weather() == "sunny"
















    # from unittest.mock import patch

    # def test_weather_is_rainy():
    #     weather = Weather()
    #     with patch('random.choice', return_value='rainy'):
    #         actual = weather.how_is_the_weather()

    #     assert actual == "rainy"

    # def test_weather_is_sunny():
    #     weather = Weather()

    #     with patch('random.choice', return_value='sunny'):
    #         actual = weather.how_is_the_weather()

    #     assert actual == "rainy"