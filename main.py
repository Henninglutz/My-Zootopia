import json
import html
from pathlib import Path

def load_data(file_path):
  """ Loads a JSON file """
  with open(file_path, "r") as fileobj:
    return json.load(fileobj)

animals_data = load_data('animals_data.json')


def serialize_animal(name, diet, location, animal_type):
    output = " "
    output += '<li class = "cards__item">'
    output += f"<strong>Name</strong>: {name}<br/>\n"
    output += f"<strong>Diet:</strong> {diet}<br/>\n"
    output += f"<strong>Location:</strong> {location}<br/>\n"
    output += f"<strong>Type:</strong> {animal_type}<br/>\n"
    output += "\n"
    output += '</li>'
    return output


output = " "
for animal in animals_data:
#    output = serialize_animal(name, diet, location, animal_type)
    name = animal.get("name", "(?)")
    lifespan = animal.get("characteristics", {}).get("lifespan", "(k.A.)")
    diet = animal.get("characteristics", {}).get("diet", {})
    location = ", ".join(animal.get(["locations"][0]))
    animal_type = animal.get("characteristics", {}).get("type",{} )

    output += serialize_animal(name, diet, location, animal_type)
#    output += serialize_animal(name, diet, location, animal_type)

data_animals = Path("animals_data.json")
template_html = Path("animals_template.html")
final_output = Path("animals.html")

#data = json.load(data_animals.read_text(encoding = "utf-8"))

new_template_for_replace = template_html.read_text(encoding="utf-8")

final_html = new_template_for_replace.replace("__REPLACE_ANIMALS_INFO__", output)
final_output.write_text(final_html, encoding = "utf-8")
