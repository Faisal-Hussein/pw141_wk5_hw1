from flask import Flask, request


app = Flask(__name__)

recipes = {
    1:{
        'id' : 1,
        'bread' : '2 slices',
        'turkey' : '4 slices',
        'swiss cheese' : '1 slice',
        'mayonnaise' : '1 teaspoon',
        'recipe' : 'turkey sandwich'
    },
    2:{
        'id' : 2,
        'bread' : '2 slices',
        'peanut butter' : '1 teaspoon',
        'strawberry jam' : '1 teaspoon',
        'recipe' : 'pb & j'
    }
}

@app.route('/')
def land():
    return {
        "you've officially landed the REAL PAGE!" : "Welcome young Padawans to Flask!"
    }

@app.route('/recipes')
def get_recipes():
    return {
        'recipes' : list(recipes.values())
    }

@app.route('/recipe/<int:id>')
def get_ind_recipes(id):
    if id in recipes:
        return{
            'recipe' : recipes[id]
        }
    return{
        'UH OH, something went wrong' :"Invalid recipe id"
    }

@app.route('/recipes', methods=["POST"])
def create_recipe():
    data = request.get_json()
    print(data)
    recipes[data['id']] = data
    return {
        'recipe created successfully': recipes[data['id']]
    }

@app.route('/recipes', methods=["PUT"])
def update_recipes():
    data = request.get_json()
    if data['id'] in recipes:
        recipes[data['id']] = data
        return {
            'recipe updated' : recipes[data['id']]
        }
    return {
        'err' : 'no recipe found with that id'
    }


@app.route('/recipes', methods=["DELETE"])
def del_recipe():
    data = request.get_json()
    if data['id'] in recipes:
        del recipes[data['id']]
        return {
            'recipe gone': f"{data['recipe']} is no more. . . "
        }
    return {
        'err' : "can't delete that recipe, it isn't there "
    }