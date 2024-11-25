import pytest
from app import app
import google.generativeai as genai
from unittest.mock import MagicMock

@pytest.fixture
def client():
    """Set up a test client for the Flask app."""
    app.config['TESTING'] = True
    client = app.test_client()
    yield client

def test_index_page(client):
    """Test the index page."""
    response = client.get('/')
    assert response.status_code == 200
    assert b"Meal Planner" in response.data  

def test_recipe_generator_page(client):
    """Test the recipe generator page."""
    response = client.get('/recipe_generator')
    assert response.status_code == 200
    assert b"Recipe Generator" in response.data

def test_view_meal_plans_page(client):
    """Test the view meal plans page."""
    response = client.get('/view_meal_plans')
    assert response.status_code == 200
    assert b"View Meal Plans" in response.data

def test_generate_meal_plan(client):
    """Test the generate_meal_plan endpoint."""
    data = {
        "food_available": "rice, chicken, vegetables",
        "food_preference": "non-vegetarian",
        "allergies": "nuts",
        "weight": 70,
        "height": 170,
        "age": 30,
        "number_of_people": 2,
        "sex": "male",
        "fitness_goal": "weight loss"
    }
    response = client.post('/generate_meal_plan', json=data)
    assert response.status_code == 200
    assert "meal_plan" in response.json


def test_view_meal_plans(client):
    """Test the view meal plans functionality."""
    response = client.get('/view_meal_plans')
    assert response.status_code == 200
    assert b"Meal Plans" in response.data  # Check for a keyword in the response content

def test_generate_recipe(client):
    """Test the generate_recipe endpoint."""
    # Create a mock for the start_chat method
    mock_genai = MagicMock()
    mock_genai.start_chat.return_value = {
        "text": "This is a sample recipe.",
        "generation_id": "gen-id-2"
    }

    # Assign the mock to the actual method
    genai.GenerativeModel = mock_genai

    data = {
        "ingredients": "tomatoes, pasta, cheese",
        "number_of_servings": 2,
        "food_preferences": "vegetarian",
        "allergies": "gluten",
        "special_requests": "low carb"
    }
    response = client.post('/generate_recipe', json=data)
    assert response.status_code == 200
    assert "recipe" in response.json

def test_save_favorite_recipe(client):
    """Test saving a favorite recipe."""
    data = {
        "name": "My Favorite Pasta",
        "recipe": "Pasta with tomato sauce and cheese."
    }
    response = client.post('/save_favorite_recipe', json=data)
    assert response.status_code == 200
    assert response.json['success'] is True

def test_view_favourite_recipes(client):
    """Test the view favourite recipes page."""
    response = client.get('/view_favourite_recipes')
    assert response.status_code == 200
    assert b"Favorite Recipes" in response.data

