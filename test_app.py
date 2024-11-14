import os
import pytest
from unittest.mock import patch, MagicMock

os.environ['GEMINI_API_KEY'] = 'test_api_key'

with patch('database.create_table', MagicMock()):
    from app import app


@pytest.fixture
def client():
    with app.test_client() as client:
        yield client


def test_index(client):
    """Test the index page loads correctly."""
    response = client.get('/')
    assert response.status_code == 200
    assert b"<title>Meal Planner</title>" in response.data


@patch('app.construct_meal_plan_query')
@patch('app.model.start_chat')
@patch('app.save_meal_plan')
def test_generate_meal_plan(mock_save_meal_plan, mock_start_chat, mock_construct_query, client):
    """Test the meal plan generation route."""
    mock_start_chat.return_value.send_message.return_value.text = "Sample Meal Plan"
    mock_construct_query.return_value = "Generated Query"

    response = client.post('/generate_meal_plan', json={
        "food_available": "rice",
        "food_preference": "vegetarian",
        "allergies": ["peanut"],
        "weight": 70,
        "height": 175,
        "age": 30,
        "number_of_people": 2,
        "sex": "male",
        "fitness_goal": "weight loss"
    })

    assert response.status_code == 200
    assert response.json["meal_plan"] == "Sample Meal Plan"
    mock_save_meal_plan.assert_called_once()


@patch('app.generate_random_form_data')
def test_autogenerate_form(mock_generate_random_form_data, client):
    """Test the autogenerate form route."""
    mock_generate_random_form_data.return_value = {"sample_key": "sample_value"}
    response = client.get('/autogenerate_form')

    assert response.status_code == 200
    assert response.json == {"sample_key": "sample_value"}


@patch('app.get_meal_plans')
def test_view_meal_plans(mock_get_meal_plans, client):
    """Test the meal plan history page."""
    # Mock data as a list of tuples to match the indexing in the template
    mock_get_meal_plans.return_value = [
        (1, "rice", "vegetarian", "peanut", 70, 175, 30, 2, "male", "weight loss", "Sample Meal Plan Content")
    ]
    response = client.get('/view_meal_plans')

    assert response.status_code == 200
    assert b"Sample Meal Plan Content" in response.data
    assert b"rice" in response.data
    assert b"Delete" in response.data


@patch('app.delete_meal_plan')
def test_delete_meal_plan_route(mock_delete_meal_plan, client):
    """Test deleting a meal plan."""
    response = client.post('/delete_meal_plan/1')

    assert response.status_code == 302  # Redirect
    mock_delete_meal_plan.assert_called_once_with(1)


def test_recipe_generator(client):
    """Test the recipe generator page loads."""
    response = client.get('/recipe_generator')
    assert response.status_code == 200
    assert b"<title>Recipe Generator</title>" in response.data  # Replace with actual title or unique content


@patch('app.construct_recipe')
@patch('app.model.start_chat')
@patch('app.save_generated_recipe')
def test_generate_recipe(mock_save_generated_recipe, mock_start_chat, mock_construct_recipe, client):
    """Test generating a recipe."""
    mock_start_chat.return_value.send_message.return_value.text = "Sample Recipe"
    mock_construct_recipe.return_value = "Generated Recipe Query"

    response = client.post('/generate_recipe', json={
        "ingredients": "tomatoes",
        "number_of_servings": 2,
        "food_preferences": "vegan",
        "allergies": ["gluten"],
        "special_requests": "low salt"
    })

    assert response.status_code == 200
    assert response.json["recipe"] == "Sample Recipe"
    mock_save_generated_recipe.assert_called_once()


@patch('app.save_recipe')
def test_save_favorite_recipe(mock_save_recipe, client):
    """Test saving a favorite recipe."""
    response = client.post('/save_favorite_recipe', json={
        "recipe": "Sample Recipe",
        "name": "Favorite Recipe"
    })

    assert response.status_code == 200
    assert response.json["success"] is True
    mock_save_recipe.assert_called_once_with("Favorite Recipe", "Sample Recipe")


@patch('app.get_favorite_recipes')
def test_view_favourite_recipes(mock_get_favorite_recipes, client):
    """Test viewing favorite recipes."""
    # Mock data as a list of tuples to match the indexing in the template
    mock_get_favorite_recipes.return_value = [
        (1, "Favorite Recipe", "Sample Recipe Content")
    ]
    response = client.get('/view_favourite_recipes')

    assert response.status_code == 200
    assert b"Favorite Recipe" in response.data
    assert b"Sample Recipe Content" in response.data
    assert b"Delete" in response.data


@patch('app.delete_favorite_recipe_from_db')
def test_delete_favorite_recipe(mock_delete_favorite_recipe_from_db, client):
    """Test deleting a favorite recipe."""
    response = client.post('/delete_favorite_recipe/1')

    assert response.status_code == 302  # Redirect
    mock_delete_favorite_recipe_from_db.assert_called_once_with(1)


@patch('app.construct_nutrient_and_calorie_query')
@patch('app.model.start_chat')
def test_track_nutrient_and_calorie(mock_start_chat, mock_construct_nutrient_query, client):
    """Test tracking nutrients and calories."""
    mock_start_chat.return_value.send_message.return_value.text = "Sample Nutrient Info"
    mock_construct_nutrient_query.return_value = "Generated Nutrient Query"

    response = client.post('/track_nutrient_and_calorie', data={
        "bmi": "22.5",
        "meal_details": "Pasta",
        "calories": "500",
        "nutrients": "Carbs",
        "goals": "Weight gain"
    })

    assert response.status_code == 200
    assert b"Sample Nutrient Info" in response.data
