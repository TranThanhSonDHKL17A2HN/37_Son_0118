def menu_is_boring(meals):
    for i in range(len(meals)-1):
        if meals[i] == meals[i+1]:
            return True
    return False
meals_1 = ['Redneck Ribs', 'Prawn Star', 'San Quentin Squid', 'Fist Full of Pizza', 'Honky Tonk Chicken']
meals_2 = ['Redneck Ribs', 'Prawn Star', 'Running Bear Salmon', 'Running Bear Salmon', 'Honky Tonk Chicken']
print(menu_is_boring(meals_1))
print(menu_is_boring(meals_2))