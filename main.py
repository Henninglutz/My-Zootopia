import json

def load_data(file_path):
  """ Loads a JSON file """
  with open(file_path, "r") as handle:
    return json.load(handle)

animals_data = load_data('animals_data.json')
print(animals_data)

for animal in animals_data:
    name = animal.get("name", "(?)")
#    lifespan = animal.get("characteristics", {}).get("lifespan", "(k.A.)")
    diet = animal.get("characteristics", {}).get("diet", {})
    location = animal.get(["locations"][0])
    animal_type = animal.get("characteristics", {}).get("type",{} )

    print(f"Name: {name}\nDiet: {diet}\nLocation: {location}\nType: {animal_type}\n")