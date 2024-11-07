import random

def construct_meal_plan_query(food_available, food_preference, allergies, weight, height, age, number_of_people, sex, fitness_goal ):
    # Calculate total meals based on the number of people
    meal_suffix = f" for {number_of_people} people"
    
    query = (
        f"The available food includes: {food_available}.\n"
        f"Only serve available food; if you don't have, tell them.\n"
        f"I prefer {food_preference} food.\n"
        f"I have allergies to {allergies}.\n"
    )

    # Add weight and height if provided
    if weight is not None:
        query += f"My weight is {weight} kg.\n"
    if height is not None:
        query += f"My height is {height} cm.\n"

    # Add age if provided
    if age is not None:
        query += f"I am {age} years old.\n"

    query += (
        f"I have {number_of_people} people to feed.\n"
        f"My sex is {sex}.\n"
        f"My fitness goal is {fitness_goal}.\n"
       
       "I always want this on this output to show weight, height inputed, and show bmi amount. calculate BMI per person using weight and height. for missing info, put missing info The format is below:\n" 
       f"The BMI for {meal_suffix} is:\n Person Number: weight, height, BMI \n"

      


        "Please create a 7-day meal plan with specific meals formatted like:\n"
        "Day 1:\n\n"
        f"Breakfast (# calories):** Example meal description{meal_suffix}.\n"
        f"Lunch (# calories):** Example meal description{meal_suffix}.\n"
        f"Dinner (# calories):** Example meal description{meal_suffix}.\n"
        f"Snacks (# calories):** Example snack description{meal_suffix}.\n"
        
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


def construct_recipe(ingredients,number_of_servings , food_preferences, allergies, special_requests):

    query = (
        f"### Recipe Request\n\n"
        f"Only make 1 recipe\n\n"
        f"Only make 1 course\n\n"
        f"I have the following ingredients available: **{ingredients}**.\n\n"
        f"The recipe is good for amount of {number_of_servings} people"
        f"I prefer **{food_preferences}** cuisine.\n\n"
        f"I am allergic to: **{allergies}**. Please ensure these are not included in the recipe.\n\n"
        f"Special requests: **{special_requests}**. \n\n"
        f"Based on the above information, please create a **3-course recipe** that is easy to follow:\n\n"
        f"**Recipe Name:**\n\n"
        f"**Cooking Time:** Approximately 1 hour\n\n"
        
        f"### Important Tips:\n"
        f"- **Portion Control:** Use measuring cups and spoons to ensure accuracy in your servings.\n"
        f"- **Adjust to Taste:** This is a starting point! Feel free to modify the recipe to suit your taste preferences.\n"
        f"- **Experiment:** Don’t hesitate to try different flavors and ingredients to make the dish enjoyable.\n"
        f"- **Consult a Professional:** A registered dietitian can offer tailored advice based on your health needs and goals.\n"
        
        f"Thank you for considering my dietary needs. I look forward to your creative recipe!"
    )
    
    return query














def generate_random_form_data():
    fitness_goals = ["weight loss", "muscle gain", "maintenance"]
    
    # Food options
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
    
    # Autogenerate query
    selected_food_preferences = random.sample(food_options, k=random.randint(1, 3))  # Randomly choose 1 to 3 unique options
    food_preference_sentence = f"I prefer {', '.join(selected_food_preferences)} food."

    allergies_list = ["none", "nuts", "dairy", "gluten", "shellfish"]

    generated_data = {
        "fitness_goal": random.choice(fitness_goals),
        "food_preference": food_preference_sentence,
        "allergies": random.choice(allergies_list),
        "weight": random.randint(50, 100),  # Random weight between 50 and 100 kg
        "height": f"{random.randint(5, 6)}'{random.randint(0, 11)}",  # Random height between 5'0" and 6'11"
        "age": random.randint(18, 60),  # Random age between 18 and 60
        "number_of_people": random.randint(1, 8),  # Random number of people to feed
        "sex": random.choice(["male", "female"]),  # Randomly assign sex
        "food_available": "chicken, rice, vegetables, fruits"  # Example of available food
    }

    return generated_data
