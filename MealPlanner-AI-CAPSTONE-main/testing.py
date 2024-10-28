import os
import google.generativeai as genai
from dotenv import load_dotenv



load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

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

chat_session = model.start_chat(
  history=[
    {
      "role": "user",
      "parts": [
        "Make me a meal plan depending on the fitness goal like weight gain and muscle gain. I also want food preference and allergies. and make the food depending on the bmi\n",
      ],
    },
    {
      "role": "model",
      "parts": [
        "I can definitely help you with a meal plan!  To give you the most accurate and personalized plan, I need a bit more information from you. Please tell me:\n\n**1. Your Fitness Goal:**\n\n* **Weight Gain:** Are you looking to gain overall weight, or specifically muscle? \n* **Muscle Gain:** How much muscle do you aim to gain per week? \n* **Other Goals:** Are you targeting any specific body fat percentage or other fitness goals? \n\n**2. Your Food Preferences:**\n\n* **Cuisine:** Do you prefer any specific type of cuisine (e.g., Mediterranean, Indian, Mexican)?\n* **Flavors:** Do you have any strong flavor preferences (e.g., spicy, savory, sweet)?\n* **Dietary Restrictions:** Do you follow any dietary restrictions (e.g., vegetarian, vegan, gluten-free)? \n\n**3. Allergies:**\n\n* **Food Allergies:** Do you have any food allergies (e.g., nuts, dairy, shellfish)? \n\n**4. Your BMI:**\n\n* **Current BMI:** Please share your current Body Mass Index (BMI). You can calculate it using a BMI calculator online. \n\n**5. Daily Calorie Needs:**\n\n* **Estimated Calorie Intake:**  Knowing your BMI and activity level will help me estimate your daily calorie needs.\n\n**Once you provide this information, I can create a detailed meal plan tailored to your needs. This plan will include:**\n\n* **Calorie and Macro Targets:**  A breakdown of your daily calories, protein, carbohydrates, and fat.\n* **Sample Meal Ideas:**  Delicious and nutritious meal suggestions for each day of the week. \n* **Snack Options:**  Healthy and satisfying snacks to help you reach your calorie and macro goals.\n* **Recipe Ideas:**  Easy and tasty recipes to incorporate into your meal plan.\n\nI'm here to help you achieve your fitness goals through healthy and enjoyable eating! \n",
      ],
    },
    {
      "role": "user",
      "parts": [
        "make me the meal plan\n",
      ],
    },
    {
      "role": "model",
      "parts": [
        "I need a little more information from you to create a personalized meal plan!  Please tell me:\n\n**1. Your Fitness Goal:**\n\n* **Weight Gain:** Are you looking to gain overall weight, or specifically muscle? \n* **Muscle Gain:** How much muscle do you aim to gain per week? \n* **Other Goals:** Are you targeting any specific body fat percentage or other fitness goals? \n\n**2. Your Food Preferences:**\n\n* **Cuisine:** Do you prefer any specific type of cuisine (e.g., Mediterranean, Indian, Mexican)?\n* **Flavors:** Do you have any strong flavor preferences (e.g., spicy, savory, sweet)?\n* **Dietary Restrictions:** Do you follow any dietary restrictions (e.g., vegetarian, vegan, gluten-free)? \n\n**3. Allergies:**\n\n* **Food Allergies:** Do you have any food allergies (e.g., nuts, dairy, shellfish)? \n\n**4. Your BMI:**\n\n* **Current BMI:** Please share your current Body Mass Index (BMI). You can calculate it using a BMI calculator online. \n\n**5. Daily Calorie Needs:**\n\n* **Estimated Calorie Intake:**  Knowing your BMI and activity level will help me estimate your daily calorie needs.\n\n**Once you provide this information, I can create a detailed meal plan tailored to your needs. This plan will include:**\n\n* **Calorie and Macro Targets:**  A breakdown of your daily calories, protein, carbohydrates, and fat.\n* **Sample Meal Ideas:**  Delicious and nutritious meal suggestions for each day of the week. \n* **Snack Options:**  Healthy and satisfying snacks to help you reach your calorie and macro goals.\n* **Recipe Ideas:**  Easy and tasty recipes to incorporate into your meal plan.\n\nI'm here to help you achieve your fitness goals through healthy and enjoyable eating! \n",
      ],
    },
    {
      "role": "user",
      "parts": [
        "Fitness goal =weight loss\nFood preference is asian\nallergies is nuts\nI dont know my BMI but my weight is 80 kilogram and 5'6 height\nDaily calorie need is 1700\n",
      ],
    },
    {
      "role": "model",
      "parts": [
        "Okay, I can help you create a sample Asian-inspired meal plan for weight loss, keeping in mind your nut allergy and a daily calorie goal of 1700. \n\n**Important Note:** This is just a sample plan. It's crucial to consult with a registered dietitian or nutritionist for personalized guidance based on your individual needs and health conditions. \n\n**Here's a possible 7-day meal plan:**\n\n**Day 1:**\n\n* **Breakfast (300 calories):**  1 cup Oatmeal with berries and a drizzle of honey, 1 hard-boiled egg\n* **Lunch (400 calories):**  1 cup Chicken Stir-Fry with brown rice (choose lean chicken breast) and mixed vegetables, served with a light soy sauce dressing. \n* **Dinner (500 calories):**  Lentil Soup (with vegetables and spices like turmeric and ginger), a small portion of steamed rice.\n* **Snacks (2 x 100 calories):**  Apple slices with 1 tablespoon of peanut-free nut butter (look for sunflower seed butter, tahini, etc.), 1 cup unsweetened almond milk\n\n**Day 2:**\n\n* **Breakfast (300 calories):**  1 cup Tofu Scramble with soy sauce, vegetables (onions, peppers), and a sprinkle of nutritional yeast.\n* **Lunch (400 calories):**  2 cups Vegetable Sushi Rolls (avoid any rolls containing nuts or nut-based sauces) with a side of edamame. \n* **Dinner (500 calories):**  Salmon Teriyaki with 1/2 cup brown rice and steamed broccoli.\n* **Snacks (2 x 100 calories):**  1 cup plain yogurt with berries, 1/4 cup trail mix (choose a nut-free blend)\n\n**Day 3:**\n\n* **Breakfast (300 calories):**  2 cups of overnight oats with almond milk, chia seeds, and fruits.\n* **Lunch (400 calories):**  1 cup Chicken Noodle Soup (choose lean chicken breast) with a side of mixed greens salad.\n* **Dinner (500 calories):**  Shrimp Pad Thai with 1/2 cup brown rice noodles, tofu, and plenty of veggies.\n* **Snacks (2 x 100 calories):**  1 cup fruit salad, 1/2 cup edamame\n\n**Day 4:**\n\n* **Breakfast (300 calories):**  1 cup  Japanese-style rice porridge (okayu) with a poached egg and nori seaweed.\n* **Lunch (400 calories):**  Vegetable spring rolls with a light dipping sauce and a side of cucumber salad.\n* **Dinner (500 calories):**  2 cups Vegetarian Curry with brown rice and naan bread (choose a smaller naan).\n* **Snacks (2 x 100 calories):**  1/4 cup mixed nuts (choose a nut-free blend), 1 cup unsweetened green tea\n\n**Day 5:**\n\n* **Breakfast (300 calories):**  2 cups of  Greek yogurt with chia seeds and berries.\n* **Lunch (400 calories):**  1 cup Tofu Stir-fry with rice noodles and vegetables.\n* **Dinner (500 calories):**  Chicken or Tofu Pho with vegetables and a side of salad.\n* **Snacks (2 x 100 calories):**  2 rice cakes with hummus, 1 cup low-fat milk\n\n**Day 6:**\n\n* **Breakfast (300 calories):**  1 cup of whole-wheat toast with avocado and a sprinkle of cumin.\n* **Lunch (400 calories):**  2 cups of  Korean Bibimbap (with brown rice, veggies, and a protein of your choice - choose lean beef or tofu) \n* **Dinner (500 calories):**  Vegetable dumplings with a light soy sauce and ginger dipping sauce.\n* **Snacks (2 x 100 calories):**  1 cup edamame, 1/2 cup mixed fruit\n\n**Day 7:**\n\n* **Breakfast (300 calories):**  1 cup  Japanese-style rice porridge (okayu) with a poached egg and nori seaweed.\n* **Lunch (400 calories):**  2 cups of  Cold Soba Noodles with a light soy sauce and ginger dressing.\n* **Dinner (500 calories):**  Salmon with a side of roasted vegetables.\n* **Snacks (2 x 100 calories):**  1/4 cup trail mix (choose a nut-free blend), 1/2 cup low-fat milk\n\n**Important Tips:**\n\n* **Portion control is key:**  Use measuring cups and spoons to ensure you're staying within your calorie goals.\n* **Choose lean protein:**  Include lean protein sources like chicken breast, tofu, fish, and lean beef.\n* **Prioritize vegetables:** Load up on vegetables for fiber and nutrients.\n* **Choose whole grains:** Opt for brown rice, quinoa, and whole-wheat bread for sustained energy and fiber.\n* **Stay hydrated:**  Drink plenty of water throughout the day. \n* **Be mindful of sauces:** Some Asian sauces can be high in sodium and calories. Choose lighter options like soy sauce or ginger-based sauces.\n\n**Remember:** This is just a starting point. You can adjust the meal plan to suit your preferences and needs.  Don't hesitate to experiment with different recipes and flavors to make it enjoyable.\n\n**Remember:  A registered dietitian can provide more customized guidance, taking into account your individual needs and health status.** \n",
      ],
    },
  ]
)

#response = chat_session.send_message("I want muscle gain meal plan and only fish and 200 calories only for 12 days no repeating recipe")
response = chat_session.send_message("I want meal plan with italy dish")

print(response.text)