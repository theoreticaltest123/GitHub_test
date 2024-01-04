from random import choice

# create a list of restaurants
restaurants = [['The Observatory', 'American', 'Tabor', 'moderate', 'sitdown'],
               ['Lucky Lab Brew Pub', 'Pub food', 'Inner SE', 'cheap', 'sitdown'],
               ['The Chomp', 'Thai', 'Inner SE', 'moderate', 'sitdown'],
               ['Horse Brass Pub', 'Pub food', 'Tabor', 'moderate', 'sitdown'],
               ['NEPO42', 'Pub food', 'North Portland', 'cheap', 'sitdown'],
               ['Taste of Afghan', 'Middle Eastern', 'East Side', 'cheap', 'food truck']]

# input food type preference
print('What type of food do you want?')
food_type = input()

# loop through restaurants in list
for item in restaurants:
    if item[1] == food_type:
        print(food_type + ' Restaurant: ' + item[0])


# future tasks: Use Pandas to create dataframes that organize the restaurants
# Use Streamlit to create a webapp