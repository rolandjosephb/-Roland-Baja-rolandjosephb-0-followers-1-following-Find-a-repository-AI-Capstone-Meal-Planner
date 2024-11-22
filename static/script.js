// Recipe Generation
document.getElementById('recipe-generator-form')?.addEventListener('submit', async (e) => {
    e.preventDefault();

    const formData = new FormData(e.target);
    const data = Object.fromEntries(formData);

    const response = await fetch('/generate_recipe', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify(data),
    });

    const result = await response.json();
    document.getElementById('recipe-result').innerText = result.recipe;
});



// // Meal Plan Generation
// document.getElementById('meal-plan-form').addEventListener('submit', async (e) => {
//     e.preventDefault();

//     const formData = new FormData(e.target);
//     const data = Object.fromEntries(formData);

//     const response = await fetch('/generate_meal_plan', {
//         method: 'POST',
//         headers: {
//             'Content-Type': 'application/json',
//         },
//         body: JSON.stringify(data),
//     });

//     const result = await response.json();
//     document.getElementById('meal-plan-result').innerText = result.meal_plan;
// });

document.addEventListener('DOMContentLoaded', () => {
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
});



// Fetch meals and populate the dropdown when the user clicks it
document.addEventListener('DOMContentLoaded', () => {
    const dropdown = document.getElementById('meal_details');
    if (dropdown) {
        dropdown.addEventListener('click', async () => {
 
            // Check if the dropdown is already populated
            if (dropdown.options.length > 1) return;
 
            try {
                const response = await fetch('/get_meals', { method: 'GET' });
 
                if (!response.ok) throw new Error('Failed to fetch meals');
 
                const meals = await response.json();
 
                // Populate the dropdown with fetched meal options
                meals.forEach(meal => {
                    const option = document.createElement('option');
                    option.value = meal.id;
                    option.textContent = meal.name;
                    dropdown.appendChild(option);
                });
            } catch (error) {
                console.error('Error fetching meals:', error);
            }
        });
    } else {
        console.error('Meal details dropdown not found.');
    }
});






// Nutrient and Calorie Tracking
document.getElementById('nutrient-and-calorie-form')?.addEventListener('submit', async (e) => {
    e.preventDefault();
    const formData = new FormData(e.target);
    const data = Object.fromEntries(formData);

    const response = await fetch('/track_nutrient_and_calorie', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify(data),
    });

    const result = await response.json();
    document.getElementById('chatbot-feedback').innerHTML = `
        <h3>Chatbot Feedback:</h3>
        <p>${result.feedback}</p>
    `;
});


// Autogenerate button
document.getElementById('autogenerate')?.addEventListener('click', async () => {
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
