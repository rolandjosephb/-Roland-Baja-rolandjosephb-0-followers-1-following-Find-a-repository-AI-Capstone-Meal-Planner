import os
from flask import Flask, request, jsonify, render_template, redirect, url_for
import google.generativeai as genai
from dotenv import load_dotenv
from meal_plan_query import construct_meal_plan_query, generate_random_form_data
from database import create_table, save_meal_plan, get_meal_plans, delete_meal_plan  # Import delete function

# API
load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

# Openai model
generation_config = {
    "temperature": 1,
    "top_p": 0.95,
    "top_k": 64,
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

# Recipe generator page
@app.route('/recipe_generator')
def recipe_generator():
    return render_template('recipe_generator.html')

@app.route('/generate_meal_plan', methods=['POST'])
def generate_meal_plan():
    data = request.json
    food_available = data.get("food_available")
    food_preference = data.get("food_preference")
    allergies = data.get("allergies")
    weight = data.get("weight")
    height = data.get("height")
    age = data.get("age")
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
@app.route('/view_meal_plans', methods=['GET'])
def view_meal_plans():
    meal_plans = get_meal_plans()
    return render_template('view_meal_plans.html', meal_plans=meal_plans)

@app.route('/delete_meal_plan/<int:meal_plan_id>', methods=['POST'])
def delete_meal_plan_route(meal_plan_id):
    delete_meal_plan(meal_plan_id) 
    return redirect(url_for('view_meal_plans'))  

# Route for generating recipes
@app.route('/generate_recipe', methods=['POST'])
def generate_recipe():
    data = request.json
    recipe_input = data.get("recipe_input")
    dietary_restrictions = data.get("dietary_restrictions")

    # Construct the query based on the input
    query = f"Generate a recipe using the following ingredients: {recipe_input}. Dietary restrictions: {dietary_restrictions}."
    
    chat_session = model.start_chat(history=[])
    response = chat_session.send_message(query)
    formatted_response = response.text.strip()

    return jsonify({"recipe": formatted_response})

if __name__ == '__main__':
    app.run(debug=True)
