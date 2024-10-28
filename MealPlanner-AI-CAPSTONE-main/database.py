import psycopg2
from psycopg2 import sql
import os

# Connect to the PostgreSQL
def connect_db():
    conn = psycopg2.connect(
        dbname="postgres",
        user="team1",
        password="mypassword",
        host="134.231.46.151",
        port="5432"
    )
    return conn

# Create a table in postgress named meal_plans..just check below
def create_table():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS meal_plans (
            id SERIAL PRIMARY KEY,
            fitness_goal TEXT,
            food_preference TEXT,
            allergies TEXT,
            weight INT,
            height TEXT,
            daily_calories INT,
            meal_plan TEXT
        )
    """)
    conn.commit()
    cursor.close()
    conn.close()

# Save meal plan to the database
def save_meal_plan(fitness_goal, food_preference, allergies, weight, height, daily_calories, meal_plan):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO meal_plans (fitness_goal, food_preference, allergies, weight, height, daily_calories, meal_plan)
        VALUES (%s, %s, %s, %s, %s, %s, %s)
    """, (fitness_goal, food_preference, allergies, weight, height, daily_calories, meal_plan))
    conn.commit()
    cursor.close()
    conn.close()

# Get all meal plans from the database
def get_meal_plans():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM meal_plans")
    meal_plans = cursor.fetchall()
    cursor.close()
    conn.close()
    return meal_plans

# Delete a meal plan from the database
def delete_meal_plan(meal_plan_id):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM meal_plans WHERE id = %s", (meal_plan_id,))
    conn.commit()
    cursor.close()
    conn.close()
