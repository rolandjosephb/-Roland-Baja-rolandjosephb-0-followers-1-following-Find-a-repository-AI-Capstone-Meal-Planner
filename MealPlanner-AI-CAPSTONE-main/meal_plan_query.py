import random

def construct_meal_plan_query(fitness_goal, food_preference, allergies, weight, height, daily_calories):
    query = (
        f"My fitness goal is {fitness_goal}.\n"
        f"I prefer {food_preference} food.\n"
        f"I have allergies to {allergies}.\n"
        f"My weight is {weight} kg and my height is {height}.\n"
        f"My daily calorie requirement is {daily_calories} calories.\n"
        "Please create a 7-day meal plan with specific meals formatted like:\n"
        "Day 1:\n\n"
        "Breakfast (# calories):** Example meal description.\n"
        "Lunch (# calories):** Example meal description.\n"
        "Dinner (# calories):** Example meal description.\n"
        "Snacks (# calories):** Example snack description.\n"
        
        "**Important Tips:\n"
        "Portion control is key: Use measuring cups and spoons to ensure you're staying within your calorie goals.\n"
        "Choose lean protein: Include lean protein sources like chicken breast, tofu, fish, and lean beef.\n"
        "Prioritize vegetables: Load up on vegetables for fiber and nutrients.\n"
        "Choose whole grains: Opt for whole-wheat pasta, brown rice, and quinoa for sustained energy and fiber.\n"
        "Stay hydrated: Drink plenty of water throughout the day.\n"
        "Be mindful of cheese: Parmesan cheese can be high in calories. Use it in moderation.\n"
        "Use olive oil sparingly: Olive oil is a healthy fat, but it's still high in calories. Use it in moderation.\n"
        
        "Remember: This is just a starting point. You can adjust the meal plan to suit your preferences and needs. "
        "Don't hesitate to experiment with different recipes and flavors to make it enjoyable.\n"
        "Remember: A registered dietitian can provide more customized guidance, taking into account your individual needs and health status."
    )
    return query

def generate_random_form_data():
    fitness_goals = ["weight loss", "muscle gain", "maintenance"]
    
    # food options
    food_options = [
        "vegetarian", 
        "vegan", 
        "gluten-free", 
        "paleo", 
        "Mediterranean", 
        "keto", 
        "low-carb", 
        "high-protein"
    ]
    
    # autogenerate query
    selected_food_preferences = random.sample(food_options, k=random.randint(1, 3))  # Randomly choose 1 to 3 unique options
    food_preference_sentence = f"I prefer {', '.join(selected_food_preferences)} food."

    allergies_list = ["none", "nuts", "dairy", "gluten", "shellfish"]

    generated_data = {
        "fitness_goal": random.choice(fitness_goals),
        "food_preference": food_preference_sentence,
        "allergies": random.choice(allergies_list),
        "weight": random.randint(50, 100),  # Random weight between 50 and 100 kg
        "height": f"{random.randint(5, 6)}'{random.randint(0, 11)}",  # Random height between 5'0" and 6'11"
        "daily_calories": random.randint(1500, 3000)  # Random daily calories between 1500 and 3000
    }

    return generated_data
