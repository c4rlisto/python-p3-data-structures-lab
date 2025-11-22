def get_names(spicy_foods):
    # Return a list of all names
    return [food["name"] for food in spicy_foods]


def get_spiciest_foods(spicy_foods):
    # Return foods where heat_level > 5
    return [food for food in spicy_foods if food["heat_level"] > 5]


def print_spicy_foods(spicy_foods):
    # Print each food in the required format
    for food in spicy_foods:
        heat = "🌶" * food["heat_level"]
        print(f"{food['name']} ({food['cuisine']}) | Heat Level: {heat}")


def get_spicy_food_by_cuisine(spicy_foods, cuisine):
    # Return the first matching cuisine
    for food in spicy_foods:
        if food["cuisine"] == cuisine:
            return food


def print_spiciest_foods(spicy_foods):
    # Reuse get_spiciest_foods and print_spicy_foods
    spicy_only = get_spiciest_foods(spicy_foods)
    print_spicy_foods(spicy_only)


def get_average_heat_level(spicy_foods):
    # Compute average heat level (integer)
    total = sum(food["heat_level"] for food in spicy_foods)
    return total // len(spicy_foods)


def create_spicy_food(spicy_foods, new_food):
    # Add new food to the list and return list
    spicy_foods.append(new_food)
    return spicy_foods
