from flask import Flask
from example_helper import pets

app = Flask(__name__)

# Página inicial com links para cada tipo de animal
@app.route('/')
def index():
    return '''<h1>Adopt a Pet!</h1>
              <p>Browse through the links below to find your new friend:</p>
              <ul>
                  <li><a href="/animals/dogs">Dogs</a></li>
                  <li><a href="/animals/cats">Cats</a></li>
                  <li><a href="/animals/rabbits">Rabbits</a></li>
              </ul>'''

# Rota dinâmica que recebe o tipo de animal
@app.route('/animals/<pet_type>/<int:pet_id>')
def pet(pet_type, pet_id):
    pet = pets[pet_type][pet_id]

    html = f"<h1>{pet['name']}</h1>"
    html += f"<img src='{pet['url']}' alt='Photo of {pet['name']}' width='300'><br>"
    html += f"<p>{pet['description']}</p>"
    html += "<ul>"
    html += f"<li><strong>Breed:</strong> {pet['breed']}</li>"
    html += f"<li><strong>Age:</strong> {pet['age']} years old</li>"
    html += "</ul>"

    return html  

@app.route('/animals/<pet_type>')
def animals(pet_type):
    html = f"<h1>List of {pet_type.capitalize()}</h1><ul>"

    for index, pet in enumerate(pets[pet_type]):
        html += f'<li><a href="/animals/{pet_type}/{index}">{pet["name"]}</a></li>'

    html += "</ul>"
    return html


if __name__ == '__main__':
    app.run(debug=True)

