# Personalized-Meal-Planner
##Project Title
##Personal Indian Meal Planner

##Overview
The Personal Indian Meal Planner is a Python-based application that helps users discover delicious Indian and international meals tailored to their specific dietary goals, allergies, and food preferences. The program filters through a curated collection of meals to provide personalized meal suggestions that align with weight loss, muscle gain, or maintenance objectives while considering allergens and dietary restrictions.

##Features
Personalized Meal Recommendations: Get meal suggestions based on your fitness goals (weight loss, muscle gain, or maintenance)

Allergy Awareness: Automatically filters out meals containing common allergens like nuts, gluten, dairy, eggs, and fish

Dietary Preference Support: Accommodates various dietary preferences including vegan, vegetarian, and gluten-free options

Nutritional Information: Displays comprehensive nutritional data including calories, protein, carbs, and fat for each meal

Indian Cuisine Focus: Features authentic Indian dishes alongside healthy international options

User-Friendly Interface: Simple command-line interface that guides users through the selection process

##Technologies/Tools Used
Programming Language: Python 3

Data Structures: Lists and Dictionaries for meal storage and filtering

Core Python Features: Functions, conditional statements, loops, string manipulation

Development Environment: Any Python-compatible IDE or text editor

##Steps to Install & Run the Project
Prerequisites
Python 3.6 or higher installed on your system

Basic command-line/terminal knowledge

##Installation Steps
Download the Code

Save the provided Python code as meal_planner.py

Verify Python Installation

Open terminal/command prompt

Type python --version or python3 --version to ensure Python is installed

Run the Application

text
python meal_planner.py
or

text
python3 meal_planner.py
Instructions for Testing
Test Case 1: Weight Loss Goal
Run the program

Enter weight_loss as your goal

Enter none for allergies

Enter none for preferences

Verify that only meals with ≤400 calories and ≤15g fat are shown

Test Case 2: Muscle Gain with Allergies
Run the program

Enter muscle_gain as your goal

Enter nuts,dairy for allergies

Enter none for preferences

Verify that meals with ≥30g protein and ≥350 calories are shown, excluding nut and dairy-containing meals

Test Case 3: Vegan Preference
Run the program

Enter maintenance as your goal

Enter none for allergies

Enter vegan for preferences

Verify that only vegan meals are displayed

Test Case 4: No Matching Meals
Run the program

Enter muscle_gain as your goal

Enter nuts,gluten,dairy,eggs,fish for allergies

Enter any preference

Verify the "Sorry no thing is matching" message appears

##Screenshots (Example Output)
text
Welcome to Indian/international meal planner!
We've got classic Indian meals and healthy picks for every taste.

What's your current focus? (weight_loss / muscle_gain / maintenance): weight_loss
allergies?(nuts, gluten, dairy or type 'none'): nuts,gluten
(vegan, vegetarian, gluten-free, or 'none'): none

Looking at our choices...

Here are some delicious ideas for you:

• Chickensalad
  Calories: 350 | Protein: 43g | Carbs: 11g | Fat: 11g

• kelloggs oats packet
  Calories: 250 | Protein: 6g | Carbs: 40g | Fat: 4g

• Egg White not the yellow part
  Calories: 270 | Protein: 24g | Carbs: 4g | Fat: 9g

• Paneer Tikka but no masala
  Calories: 287 | Protein: 22g | Carbs: 8g | Fat: 18g

• Chole with rice(but brown)
  Calories: 420 | Protein: 15g | Carbs: 63g | Fat: 8g

• DalTadka Roti
  Calories: 350 | Protein: 18g | Carbs: 50g | Fat: 6g

• Chicken is tandoori
  Calories: 353 | Protein: 40g | Carbs: 5g | Fat: 18g

• Quinoa and mixveg
  Calories: 367 | Protein: 12g | Carbs: 45g | Fat: 10g

• Ravaupma
  Calories: 299 | Protein: 8g | Carbs: 55g | Fat: 6g
