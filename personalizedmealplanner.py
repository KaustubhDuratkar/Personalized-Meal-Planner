# Personal Indian Meal Planner – Complete Humanized Style

# Mouthwatering meals, nutrition info included
meals = [
    {"dish": "Chickensalad", "calories": 350, "allergens": [], "types": ["protein", "CARB IS LOW"], "protein": 43, "carbs": 11, "fat": 11},
    {"dish": "VeganBOWL", "calories": 400, "allergens": ["nuts"], "types": ["vegan", "gluten IS free"], "protein": 17, "carbs": 55, "fat": 8},
    {"dish": "kelloggs oats packet", "calories": 250, "allergens": [], "types": ["vegetarian", "fiber is high"], "protein": 6, "carbs": 40, "fat": 4},
    {"dish": "PeanutButter and Toast", "calories": 300, "allergens": ["nuts", "gluten"], "types": ["vegetarian"], "protein": 10, "carbs": 30, "fat": 15},
    {"dish": "Salmon(expensive)", "calories": 457, "allergens": ["fish"], "types": ["highprotein"], "protein": 42, "carbs": 35, "fat": 19},
    {"dish": "Egg White not the yellow part", "calories": 270, "allergens": ["eggs"], "types": ["carb is low"], "protein": 24, "carbs": 4, "fat": 9},
    # Indians favorites
    {"dish": "Paneer Tikka but no masala", "calories": 287, "allergens": ["dairy"], "types": ["vegetarian", "highprotein"], "protein": 22, "carbs": 8, "fat": 18},
    {"dish": "Chole with rice(but brown)", "calories": 420, "allergens": [], "types": ["vegan", "fiber is high"], "protein": 15, "carbs": 63, "fat": 8},
    {"dish": "DalTadka Roti", "calories": 350, "allergens": [], "types": ["vegan", "highprotein"], "protein": 18, "carbs": 50, "fat": 6},
    {"dish": "Dosa with aloo masala", "calories": 416, "allergens": ["gluten"], "types": ["vegetarian"], "protein": 10, "carbs": 65, "fat": 12},
    {"dish": "Chicken is tandoori", "calories": 353, "allergens": [], "types": ["highprotein", "low-carb"], "protein": 40, "carbs": 5, "fat": 18},
    {"dish": "Quinoa and mixveg", "calories": 367, "allergens": [], "types": ["vegan", "gluten-free"], "protein": 12, "carbs": 45, "fat": 10},
    {"dish": "Ravaupma", "calories": 299, "allergens": ["gluten"], "types": ["vegetarian"], "protein": 8, "carbs": 55, "fat": 6},
]

def meal_plan(Meal, goal1):
    """Is this meal right for you"""
    if goal1 == "weight_loss":
        return Meal["calories"] <= 400 and Meal["fat"] <= 15
    if goal1 == "muscle_gain":
        return Meal["protein"] >= 30 and Meal["calories"] >= 350
    if goal1 == "maintenance":
        return True
    return False

def choose_meals(goal, WORSTfoods, likes):
    """Find tasty dishes that can help you"""
    dishes_show = []
    for item in meals:
        if any(trouble in item["allergens"] for trouble in WORSTfoods):
            continue
        if likes and not any(like in item["types"] for like in likes):
            continue
        if not meal_plan(item, goal):
            continue
        dishes_show.append(item)
    return dishes_show

def meal_planner():
    print("Welcome to Indian/international meal planner!")
    print("We’ve got classic Indian meals and healthy picks for every taste.\n")
    goal = input("What’s your current focus? (weight_loss / muscle_gain / maintenance): ").strip().lower()
    allergy_raw = input("allergies?(nuts, gluten, dairy or type 'none'): ").strip().lower()
    avoid_list = [food.strip() for food in allergy_raw.split(",")] if allergy_raw != "none" else []
    food_prefer = input("(vegan, vegetarian, gluten-free, or 'none'): ").strip().lower()
    likes_list = [pick.strip() for pick in food_prefer.split(",")] if food_prefer != "none" else []
    print("\nLooking at our choices...")

    userfav = choose_meals(goal, avoid_list, likes_list)

    if userfav:
        print("\nHere are some delicious ideas for you:\n")
        for meal in userfav:
            print(f"• {meal['dish']}")
            print(f"  Calories: {meal['calories']} | Protein: {meal['protein']}g | Carbs: {meal['carbs']}g | Fat: {meal['fat']}g\n")
    else:
        print("\nSorry no thing is matching")
        print("Meals are not best for your allergies")

if __name__ == "__main__":
    meal_planner()
