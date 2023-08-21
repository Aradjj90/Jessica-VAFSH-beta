import requests
import datetime
from math import floor
import Answer_Dictionary

city = "Ivano-Frankivsk"
lat = 48.9215
lon = 24.7097
open_weather_tokin = "your tokin"

def get_weather_now(tokin=open_weather_tokin):
    try:
        r = requests.get(
            f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={tokin}&units=metric"
        )
        date = r.json()
        temp = floor(date["main"]["temp"])
        weather = date["weather"][0]["description"]
        wind = date["wind"]["speed"]
        restitution = f"temperature: {temp} degrees \n weather: {weather}"
        if wind > 4:
            wind_plus = "it is a bit windy now"
            restitution = restitution + wind_plus
        if wind > 7:
            wind_plus = "now is very windy. be careful"
            restitution = restitution + wind_plus
        Answer_Dictionary.set_temp(restitution)
        return "temp"
    except:
        print("error")


def get_weather_5day(tokin=open_weather_tokin):
    try:
        r = requests.get(
            f"https://api.openweathermap.org/data/2.5/forecast?lat={lat}&lon={lon}&appid={tokin}&units=metric"
        )
        date = r.json()
        # pprint(date)
        # date_time = datetime.datetime.fromtimestamp(date["list"][39]["dt"])
        # temp = date["list"][0]["main"]["temp"]
        # weather = date ["list"][0]["weather"][0]["description"]
        # wind = date["list"][0]["wind"]["speed"]
        return date
    except:
        print("error_5day")


def find_day(date, day):
    counter = 0
    morning_index = None
    dinner_index = None
    eventide_index = None
    for data in date["list"]:
        if str(datetime.datetime.now().date() + datetime.timedelta(days=day)) in data["dt_txt"]:
            if "06:00:00" in data["dt_txt"]:
                morning_index = counter
                print("write morning")
            elif "12:00:00" in data["dt_txt"]:
                dinner_index = counter
                print("write dinner")
            elif "18:00:00" in data["dt_txt"]:
                eventide_index = counter
                print("write eventide")
        counter = counter + 1

    return morning_index, dinner_index, eventide_index


def forecast(date, index_time_day):
    morning_index, afternoon_index, eventide_index = index_time_day
    if eventide_index is None:
        restitution = get_weather_now()
        return restitution

    elif afternoon_index is None and morning_index is None:
        eventide_weather = date["list"][eventide_index]["weather"][0]["description"]
        temp_even = floor(date["list"][eventide_index]["main"]["temp"])
        wind_even = date["list"][eventide_index]["wind"]["speed"]
        restitution = f"In the evening it will be {eventide_weather} and {temp_even} degrees"
        print("evening")
        if wind_even > 4:
            wind_plus = "it is a bit windy today"
            restitution = restitution + wind_plus
        elif wind_even > 7:
            wind_plus = "today is very windy. be careful"
            restitution = restitution + wind_plus
        return restitution

    if morning_index is None:
        afternoon_weather = date["list"][afternoon_index]["weather"][0]["description"]
        eventide_weather = date["list"][eventide_index]["weather"][0]["description"]
        temp_after = floor(date["list"][afternoon_index]["main"]["temp"])
        temp_even = floor(date["list"][eventide_index]["main"]["temp"])
        wind_after = date["list"][afternoon_index]["wind"]["speed"]
        wind_even = date["list"][eventide_index]["wind"]["speed"]
        average_wind_speed = (wind_after + wind_even) / 2
        if afternoon_weather == eventide_weather:
            restitution = f"The weather will be {eventide_weather} all day \n temperature at the afternoon {temp_after}"\
                          f"degrees \n in the evening {temp_even} degrees"
        else:
            restitution = f"In the afternoon it will be {afternoon_weather} and {temp_after} degrees \n" \
                          f" in the evening {eventide_weather} and {temp_even} degrees"

        if average_wind_speed > 4:
            wind_plus = "it is a bit windy today"
            restitution = restitution + wind_plus
        elif average_wind_speed > 7:
            wind_plus = "today is very windy. be careful"
            restitution = restitution + wind_plus
        return restitution
    else:
        morning_weather = date["list"][morning_index]["weather"][0]["description"]
        afternoon_weather = date["list"][afternoon_index]["weather"][0]["description"]
        eventide_weather = date["list"][eventide_index]["weather"][0]["description"]
        temp_morn = floor(date["list"][morning_index]["main"]["temp"])
        temp_after = floor(date["list"][afternoon_index]["main"]["temp"])
        temp_even = floor(date["list"][eventide_index]["main"]["temp"])
        wind_morn = date["list"][morning_index]["wind"]["speed"]
        wind_after = date["list"][afternoon_index]["wind"]["speed"]
        wind_even = date["list"][eventide_index]["wind"]["speed"]
        average_wind_speed = (wind_morn + wind_after + wind_even) / 3

        if morning_weather == afternoon_weather == eventide_weather:
            restitution = f"The weather will be {morning_weather} all day \n temperature at the morning {temp_morn}"\
                        f" degrees \n at the afternoon {temp_after} degrees \n in the evening {temp_even} degrees"
        else:
            restitution = f"In the morning it will be {morning_weather} and {temp_morn} degrees \n" \
                        f" at the afternoon {afternoon_weather} and {temp_after} degrees \n" \
                        f" in the evening {eventide_weather} and {temp_even} degrees"

        if average_wind_speed > 4:
            wind_plus = "it is a bit windy today"
            restitution = restitution + wind_plus
        elif average_wind_speed > 7:
            wind_plus = "today is very windy. be careful"
            restitution = restitution + wind_plus

        return restitution


def call_forecast(day):
    date_json = get_weather_5day()
    Answer_Dictionary.set_temp(forecast(date_json, find_day(date_json, day)))
    return 'temp'

if __name__ == "__main__":
    pass

    #date_json = get_weather_5day()
    # print(forecast(date_json, find_day(date_json, 0)))
    #print (forecast(date_json, find_day(date_json, 0)))
    # print(get_weather_now(open_weather_tokin))
