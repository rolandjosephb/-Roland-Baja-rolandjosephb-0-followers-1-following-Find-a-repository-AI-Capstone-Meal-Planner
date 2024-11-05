import psycopg2
from psycopg2 import sql

def connect_db():
    conn = psycopg2.connect(dbname="postgres", user="postgres", password="206v15ALdw", host="localhost", port="5432")
    return conn

def create_table():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS meal_plans (
        id SERIAL PRIMARY KEY,
        food_available TEXT,
        food_preference TEXT,
        allergies TEXT,
        weight INTEGER,
        height TEXT,
        age INTEGER,
        number_of_people INTEGER,
        sex TEXT,
        fitness_goal TEXT,
        meal_plan TEXT
    );
    """)
    
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS recipe_generated (
        id SERIAL PRIMARY KEY,
        ingredients TEXT,
        number_of_servings INTEGER,
        food_preferences TEXT,
        allergies TEXT,
        special_requests TEXT,
        recipe TEXT
    );
    """)
    
    conn.commit()
    cursor.close()
    conn.close()

def save_meal_plan(food_available, food_preference, allergies, weight, height, age, number_of_people, sex, fitness_goal, meal_plan):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("""
    INSERT INTO meal_plans (food_available, food_preference, allergies, weight, height, age, number_of_people, sex, fitness_goal, meal_plan)
    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s);
    """, (food_available, food_preference, allergies, weight, height, age, number_of_people, sex, fitness_goal, meal_plan))
    
    conn.commit()
    cursor.close()
    conn.close()

def save_generated_recipe(ingredients,number_of_servings, food_preferences, allergies, special_requests, recipe):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("""
    INSERT INTO recipe_generated (ingredients, number_of_servings, food_preferences, allergies, special_requests, recipe)
    VALUES (%s, %s,  %s, %s, %s, %s);
    """, (ingredients, number_of_servings, food_preferences, allergies, special_requests, recipe))
    
    conn.commit()
    cursor.close()
    conn.close()

def get_recipes():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM recipe_generated;")
    meal_plans = cursor.fetchall()
    cursor.close()
    conn.close()
    return meal_plans

def get_meal_plans():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM meal_plans;")
    meal_plans = cursor.fetchall()
    cursor.close()
    conn.close()
    return meal_plans





def delete_meal_plan(meal_plan_id):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM meal_plans WHERE id = %s;", (meal_plan_id,))
    conn.commit()
    cursor.close()
    conn.close()
