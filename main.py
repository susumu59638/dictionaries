#create a dictionary
names = {"Son":"Susumu","Mother":"Ayumi","Father":"Satoshi","Daughter":"Akira"}
print(names)

#access a value from dictionary
my_name = names["Son"]
print(f"My name is {my_name}")

#get the list of keys
my_keys = list(names.keys())
print(my_keys)

#get the list of values
my_values = list(names.values())
print(my_values)

#access each key from the dictionary
for key in names:
    print(key)

#access each value from the dictionary
for key in names:
    print(names[key])

#check if a key exists in the dictionary
if "Grandmother" in names:
    print(names["Grandmother"])
else:
    print("This is not a key in here")

#adding a key-value pair in the dictionary
names["Grandmother"] = "Toshiko"
names["Grandfather"] = "Otani"
print(names)

#deleting a key value pair from the dictionary
del names["Daughter"]
print(names)

#changing a value in the dictionary
names["Son"] = "BOB"
print(names)

#add a list of values to the dictionary
names["age"] = [12,46,46,78,82]
print(names)

#access a value from the list in the dictionary
my_age = names["age"][0]
print(f"My age is {my_age}") 