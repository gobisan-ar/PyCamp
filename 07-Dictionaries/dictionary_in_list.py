travel_log = [
    {
      "country": "France",
      "visits": 12,
      "cities": ["Paris", "Lille", "Dijon"]
    },
    {
      "country": "Germany",
      "visits": 5,
      "cities": ["Berlin", "Hamburg", "Stuttgart"]
    },
]

def add_new_country(country, visits, cities):
    new_travel_record = {}
    new_travel_record["country"] = country
    new_travel_record["visits"] = visits
    new_travel_record["cities"] = cities

    travel_log.append(new_travel_record)

add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])
print(travel_log)