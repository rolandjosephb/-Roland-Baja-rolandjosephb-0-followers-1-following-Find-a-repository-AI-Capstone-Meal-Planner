document.getElementById('meal-plan-form').addEventListener('submit', async (e) => {
    e.preventDefault();

    const formData = new FormData(e.target);
    const data = Object.fromEntries(formData);

    const response = await fetch('/generate_meal_plan', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify(data),
    });

    const result = await response.json();
    document.getElementById('meal-plan-result').innerText = result.meal_plan;
});

// Autogenerate button
document.getElementById('autogenerate').addEventListener('click', async () => {
    const response = await fetch('/autogenerate_form', {
        method: 'GET',
    });

    const formData = await response.json();

    document.getElementById('fitness_goal').value = formData.fitness_goal;
    document.getElementById('food_preference').value = formData.food_preference;
    document.getElementById('allergies').value = formData.allergies;
    document.getElementById('weight').value = formData.weight;
    document.getElementById('height').value = formData.height;
    document.getElementById('age').value = formData.age;
    document.getElementById('number_of_people').value = formData.number_of_people;
    document.getElementById('sex').value = formData.sex;
    document.getElementById('food_available').value = formData.food_available;
});
