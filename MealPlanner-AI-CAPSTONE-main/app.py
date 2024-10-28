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

@app.route('/generate_meal_plan', methods=['POST'])
def generate_meal_plan():
    data = request.json
    fitness_goal = data.get("fitness_goal")
    food_preference = data.get("food_preference")
    allergies = data.get("allergies")
    weight = data.get("weight")
    height = data.get("height")
    daily_calories = data.get("daily_calories")


    query = construct_meal_plan_query(fitness_goal, food_preference, allergies, weight, height, daily_calories)
    chat_session = model.start_chat(history=[])
    response = chat_session.send_message(query)
    formatted_response = response.text.strip()
    
    # Saving/uploading meal plan to postgress or whatever database
    save_meal_plan(fitness_goal, food_preference, allergies, weight, height, daily_calories, formatted_response)
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

if __name__ == '__main__':
    app.run(debug=True)
