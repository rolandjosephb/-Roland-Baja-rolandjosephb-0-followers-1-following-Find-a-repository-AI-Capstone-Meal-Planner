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
       "put a short title here: for example: Meal plan for chicken, beef, and salad."
       "I always want this on this output to show weight, height inputed, and show bmi amount. calculate BMI per person using weight and height. The imnput from the user will be seperated by comma. for example weight is 88, 87, 86 or height is 5'6, 5'7, or 5,8\n"   


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
        f"Based on the above information, please create a **1-course recipe** that is easy to follow:\n\n"
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

# def construct_nutrient_and_calorie_query(bmi, meal_details, calories, nutrients, goals):
#     # Create a feedback message based on the input data
#     query = (
#         f"### Nutrient and Calorie Tracking\n\n"
#         f"User's BMI: {bmi}\n"
#         f"Meal Details: {meal_details}\n"
#         f"Calories in the meal: {calories}\n"
#         f"Nutrients present in the meal: {nutrients}\n"
#         f"User's fitness goal: {goals}\n"
        
#         "Feedback:\n"
#         "Based on the provided meal details, we will assess if the meal aligns with the user's fitness goals and give feedback.\n"
#         "The meal contains a total of {calories} calories, which should be considered in relation to the user's goals.\n"
#         "We will also evaluate the nutrients mentioned and provide suggestions to optimize the meal for the specified fitness goal.\n"
        
#         "If the meal exceeds the calorie goal, we will recommend cutting back on certain ingredients. "
#         "If it falls short, we will suggest adding more nutrient-dense items to meet the user's needs."
#         "In general, the key is to strike a balance between all the macronutrients—proteins, carbs, and fats—as well as ensuring you're meeting your micronutrient needs like vitamins and minerals.\n\n"
        
#         "Remember, nutrition isn't about strict rules but finding what works best for you. Small adjustments to meals can make a big difference over time, helping you stay on course toward achieving your fitness goals.\n\n"
        
#         "Remember to keep in mind the importance of balance in macronutrients (carbs, proteins, fats) and micronutrients (vitamins, minerals)."
#     )

#     return query

def construct_nutrient_and_calorie_query(user_info, meal_details, calories, nutrients, goals):
    """
    Generates a feedback query to evaluate a 7-day meal plan based on User Info, calorie intake, nutrients, and fitness goals.
    
    Args:
        User Info (str): Height, Sex, Age, BMI, Activity level.
        meal_details (str): 7-day meal plan with the number of people and detailed meal information.
        calories (int): Caloric value of the meal.
        nutrients (dict): Nutrients present in the meal with their values.
        goals (str): User's fitness goals (e.g., weight loss, muscle gain, maintenance).
    
    Returns:
        str: A detailed feedback query.
    """
    query = (
        f"### Nutrient and Calorie Evaluation\n\n"
        f"User's Info: {user_info}\n"
        f"Meal Plan Details:\n{meal_details}\n\n"
        f"Caloric Value: {calories} kcal\n"
        f"Nutrient Composition: {nutrients}\n"
        f"Fitness Goals: {goals}\n\n"
        
        "### Feedback Analysis:\n"
        "1. **Calories vs Fitness Goals**:\n"
        f"- The provided User Info of {user_info} is compared to the caloric intake ({calories} kcal). "
        "This helps determine whether the meal supports the user's goal (e.g., weight loss, muscle gain, maintenance).\n"
        "- Example: A high BMI aiming for weight loss might require fewer calories, while muscle gain goals might demand a caloric surplus.\n\n"
        
        "2. **Nutrient Alignment with Goals**:\n"
        f"- The nutrient profile ({nutrients}) is evaluated. For instance:\n"
        "  - High protein supports muscle gain.\n"
        "  - Balanced macros align with maintenance.\n"
        "  - Reduced carbs/fats may better suit weight loss.\n\n"
        
        "3. **Meal Plan Suggestions**:\n"
        "- If calories exceed daily requirements, reduce portions or replace high-calorie items.\n"
        "- Add nutrient-dense foods if lacking specific vitamins/minerals.\n"
        "- Tailor macros to better align with the fitness goals.\n\n"


        "### Conclusion:\n"
        "This analysis evaluates the meal plan for alignment with the user's BMI, nutrient needs, and fitness goals, providing actionable suggestions to optimize health outcomes."
    )
    return query