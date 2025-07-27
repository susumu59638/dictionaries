countries = {"UK":"London","Japan":"Tokyo","Australia":"Canberra",}
Location = countries["UK"]
print(f"I live in {Location}!")


my_keys = list(countries.keys())
print(my_keys)

my_values = list(countries.values())
print(my_values)


if "Australia" in countries:
    print(countries["Australia"])
else:
    print("THAT ISNT A KEY")

countries["Australia"] = "Canberra"
print(countries)