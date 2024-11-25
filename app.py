import os
from flask import Flask, request, jsonify, render_template, redirect, url_for
import google.generativeai as genai
from dotenv import load_dotenv
from query import construct_meal_plan_query, construct_recipe, generate_random_form_data, construct_nutrient_and_calorie_query
from database import create_table, save_meal_plan, get_meal_plans, delete_meal_plan, save_generated_recipe, save_recipe, get_favorite_recipes,delete_favorite_recipe_from_db, get_all_meals 

load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))


generation_config = {
    "temperature": 1, #creativity/randomness
    "top_p": 0.95,
    # "top_k": 64,
    "top_k": 40,
    "max_output_tokens": 8192,
    "response_mime_type": "text/plain",
}

model = genai.GenerativeModel(
    model_name="gemini-1.5-flash",
    generation_config=generation_config,
)

app = Flask(__name__)

create_table()

# Index/main page
@app.route('/')
def index():
    return render_template('index.html')

# Generate meal plan
@app.route('/generate_meal_plan', methods=['POST'])
def generate_meal_plan():
    data = request.json
    food_available = data.get("food_available")
    food_preference = data.get("food_preference")
    allergies = data.get("allergies")
    weight = data.get("weight") if data.get("weight") else None
    height = data.get("height") if data.get("height") else None
    age = data.get("age")  if data.get("age") else None
    number_of_people = data.get("number_of_people")
    sex = data.get("sex")
    fitness_goal = data.get("fitness_goal")

    # Construct the query based on the input
    query = construct_meal_plan_query(
        food_available, food_preference, allergies, weight, height, age, number_of_people, sex, fitness_goal
    )
    chat_session = model.start_chat(history=[])
    response = chat_session.send_message(query)
    formatted_response = response.text.strip()

    # Saving/uploading meal plan to PostgreSQL or whatever database
    save_meal_plan(
        food_available, food_preference, allergies, weight, height, age, number_of_people, sex, fitness_goal, formatted_response
    )
    return jsonify({"meal_plan": formatted_response})








# Autogenerate answer
@app.route('/autogenerate_form', methods=['GET'])
def autogenerate_form():
    generated_data = generate_random_form_data()
    return jsonify(generated_data)







# Meal plan history
# @app.route('/view_meal_plans', methods=['GET'])
# def view_meal_plans():
#     meal_plans = get_meal_plans()
#     return render_template('view_meal_plans.html', meal_plans=meal_plans)
# Meal plan history
@app.route('/view_meal_plans', methods=['GET'])
def view_meal_plans():
    meal_plans = get_meal_plans()
    return render_template('view_meal_plans.html', meal_plans=meal_plans)




@app.route('/delete_meal_plan/<int:meal_plan_id>', methods=['POST'])
def delete_meal_plan_route(meal_plan_id):
    delete_meal_plan(meal_plan_id) 
    return redirect(url_for('view_meal_plans'))  

# Recipe generation page
@app.route('/recipe_generator')
def recipe_generator():
    return render_template('recipe_generator.html')

@app.route('/generate_recipe', methods=['POST'])
def generate_recipe():
    data = request.json
    ingredients = data.get("ingredients")
    number_of_servings = data.get("number_of_servings")
    food_preferences = data.get("food_preferences")
    allergies = data.get("allergies")
    special_requests = data.get("special_requests")

    # Construct the recipe query based on the input
    query = construct_recipe(ingredients, number_of_servings, food_preferences, allergies, special_requests)
    
    chat_session = model.start_chat(history=[])
    response = chat_session.send_message(query)
    formatted_response = response.text.strip()
    
    # Save the generated recipe to the database
    save_generated_recipe(ingredients, number_of_servings, food_preferences, allergies, special_requests, formatted_response)
    
    return jsonify({"recipe": formatted_response})

# Save favorite recipe with a name
@app.route('/save_favorite_recipe', methods=['POST'])
def save_favorite_recipe():
    data = request.get_json()
    recipe = data.get('recipe')
    name = data.get('name')  # Get the recipe name from the request
    save_recipe(name, recipe)  # Save the recipe to the database with the name
    return jsonify(success=True)

# View favorite recipes
@app.route('/view_favourite_recipes')
def view_favourite_recipes():
    favorite_recipes = get_favorite_recipes()  # Fetch the favorite recipes
    return render_template('view_favourite_recipe.html', favorite_recipes=favorite_recipes)

# Delete favorite recipe
@app.route('/delete_favorite_recipe/<int:recipe_id>', methods=['POST'])
def delete_favorite_recipe(recipe_id):
    # Call the database function to delete the recipe by ID
    delete_favorite_recipe_from_db(recipe_id)
    return redirect(url_for('view_favourite_recipes'))  # Redirect back to the favorite recipes page

@app.route('/nutrient_and_calorie')
def nutrient_and_calorie():
    return render_template('nutrient_and_calorie.html')

@app.route('/track_nutrient_and_calorie', methods=['POST'])
def track_nutrient_and_calorie():
    # Extract form data
    user_info = request.form['user_info']
    meal_details = request.form['meal_details']
    calories = request.form['calories']
    nutrients = request.form['nutrients']
    goals = request.form['goals']

    # Construct the query using the provided data
    query = construct_nutrient_and_calorie_query(user_info, meal_details, calories, nutrients, goals)

    # Send the query to the AI model
    chat_session = model.start_chat(history=[])
    response = chat_session.send_message(query)
    formatted_response = response.text.strip()

    # Render the response with feedback on the nutrient and calorie tracking page
    return render_template('nutrient_and_calorie.html', feedback=formatted_response)





@app.route('/get_meals', methods=['GET'])
def get_meals():
            """
            Fetch meals from the database and return them as JSON.
            """
            try:
                meals = get_all_meals()
                return jsonify(meals)
            except Exception as e:
                print(f"Error fetching meals: {e}")
                return jsonify({"error": "Failed to fetch meals"}), 500










if __name__ == '__main__':
    app.run(debug=True)

#from waitress import serve


#if __name__ == "__main__":
    #serve(app.run(debug=True, use_reloader=False), host='0.0.0.0', port=5000)
    #http://127.0.0.1:5000
