status = "Nonvalid"

print("Welcome to Cards Against Humanity!")

#Classes



#Level 1: Play, Settings, or Exit
level1 = int(input("Type 1 to play, type 2 for settings, or type 3 to exit: "))
while level1 != 1 or level1 != 2 or level1 != 3:
    level1 = int(input("Invalid Input: Type 1 to play, type 2 for settings, or type 3 to exit: ")) 

#Level 2: Player Number Selection
if level1 == 1:
    player_num = int(input("Input the number of players playing (3 to 6) or type x to go back: "))
    while player_num < 3 or player_num > 6:
        player_num = input("Invalid number of players. Input the number of players playing (3 to 6 players) or type x to go back: ")
    status = "Valid"

"""
elif level1 == 2:
    settings_choice = input("Type 1 edit a preset theme, type 2 to add a custom theme, or type x to go back to main menu: ")
    while settings_choice != "1" or settings_choice != "2" or settings_choice != "x":
        settings_choice = input("Invalid Input. Type 1 edit a preset theme, type 2 to add a custom theme, or type x to go back to main menu: ")

        if settings_choice == "1":
        
        elif settings_choice == "2":

        elif settings_choice == "x":

"""

else:
    exit()

#Level 3: Theme Selection
if status == "Valid":
    print()
    input("Type 1 to out the theme you want: ")





