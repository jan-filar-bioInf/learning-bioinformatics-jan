#dictionary of Fruits , associate key with value
Fruits = [
    {"Fruit": "apple", "Calories": "130"},
    {"Fruit": "avocado California", "Calories": "50"},
    {"Fruit": "banana", "Calories": "110"},
    {"Fruit": "cantaloupe", "Calories": "50"},
    {"Fruit": "grapefruit", "Calories": "60"},
    {"Fruit": "grapes", "Calories": "90"},
    {"Fruit": "honeydew melon", "Calories": "50"},
    {"Fruit": "kiwifruit", "Calories": "90"},
    {"Fruit": "lemon", "Calories": "15"},
    {"Fruit": "lime", "Calories": "20"},
    {"Fruit": "nectarine", "Calories": "60"},
    {"Fruit": "orange", "Calories": "80"},
    {"Fruit": "peach", "Calories": "60"},
    {"Fruit": "pear", "Calories": "100"},
    {"Fruit": "pineapple", "Calories": "50"},
    {"Fruit": "plums", "Calories": "70"},
    {"Fruit": "strawberries", "Calories": "50"},
    {"Fruit": "sweet cherries", "Calories": "100"},
    {"Fruit": "tangerine", "Calories": "50"},
    {"Fruit": "watermelon", "Calories": "80"}
]


#ask after item
item = input("Item: ").lower()

#if the input item matches a Key/Fruit print Key Calories
for fruit in Fruits:
    if fruit["Fruit"] == item:
        print("Calories: ", fruit["Calories"])
    if fruit["Calories"] == item:
        print("Fruit: ", fruit["Fruit"])



