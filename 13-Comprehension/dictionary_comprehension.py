import random

names = ["Bruce", "Loki", "Peter", "Steve", "Tony", "Thor"]

hero_scores = {hero: random.randint(1, 100) for hero in names}
print(hero_scores)

strong_heroes = {hero: score for (hero, score) in hero_scores.items() if score > 50}
print(strong_heroes)

sentence = "What is the Airspeed Velocity of an Unladen Swallow?"
result = {word: len(word) for word in sentence.split()}
print(result)

weather_c = {
    "Monday": 12,
    "Tuesday": 14,
    "Wednesday": 15,
    "Thursday": 14,
    "Friday": 21,
    "Saturday": 22,
    "Sunday": 24,
}

weather_f = {day: (temp_c * 9/5) + 32 for (day, temp_c) in weather_c.items()}
print(weather_f)
