status = "Unvalid"
play_again = "yes"

print("Welcome to Cards Against Humanity!")

default_prompts = [
                "Attention students! Principal Butthead is at home recovering from ___. We hope he'll be back soon."
                ,"Coming soon! Batman vs. ___"
                ,"This is gonna be the best sleepover ever. Once Mom goes to bed, it's time for ___!"
                ,"My dad and I enjoy ___ together."
                ,"Never fear, Captain ___ is here!"
                ,"Kids, Dad is trying something new this week. It's called ___."
                ,"CCN breaking news! Over half of Americans are now ___."
                ,"Outback Steakhouse: No rules. Just ___."
                ,"All I want for Christmas is ___."
                ,"My favourite dinosaur is ___asaurus."
                ]  

default_prompt_answers = [
                "A cloud that rains diarrhea","Batman in a skirt","George Washington eating an apple","A big wet kiss from Great Aunt Sharon","Eight hours of video games.","Hanging out with Zendaya","Eating a lightbulb","A burrito smoothie","Covid 19","Eating Jelly"
                ,"The police","Blowing up the moon","Turning into a super saiyan","Canada","Australia","United States","A hot cup of tea","Dirty upperware","Phineas and Ferb","Michael Jordan's Auntie"
                ,"Cheeto fingers","TikTok","An iPhone with a broken screen","Polar Bears","Bob the builder dancing","Dora fighting Diego","A talking lion","A Democrat","A Republican","Idiots"
                ,"The Magic School Bus","Ramen Noodles","Spaghetti Tacos","Pizza Hat","Climate Change","Box Fort","Chevy Truck","Honda Civic","Laptop","The loose skin at the joint of the elbow called a weenus"
                ,"Pikachu","Politics","Crying in the bathroom","A bathtub of cottage cheese","JoJo Siwa","Ninjas","Happiness","Doing Karate","A lot of money","Being a good programmer"
                ,"A hot air balloon powered by burps","The best game ever. Fortnite.","Darth Vader","Bacon strips","The government","Ice cream","The Harlem Shake","Youtube Rewind","Eating waffles","Ariana Grande"
                ,"A dancing toddler","BBQ chips","C++","Python","IDK IDC ANYMORE","Random Prompt answer","Chicken nuggets","This is tedious","Read if you are not cool","1980's Music"
                ]

#Classes



#Level 1: Play, Settings, or Exit
level1 = int(input("Type 1 to play, type 2 for settings, or type 3 to exit: "))
while level1 != 1 or level1 != 2 or level1 != 3:
    level1 = int(input("Invalid Input: Type 1 to play, type 2 for settings, or type 3 to exit: ")) 

#Level 2: Player Number Selection
if level1 == 1:
    player_num = int(input("Input the number of players playing (3 to 6)"))
    while player_num < 3 or player_num > 6:
        player_num = input("Invalid number of players. Input the number of players playing (3 to 6 players): ") 
    status = "Valid"

#Level 2: Settings Selection
elif level1 == 2:
    print("Hi")

else:
    exit()

#Level 3: Theme and number of rounds selection. 
if status == "Valid":
    status = "Unvalid"
    themes_list = []
    print("Theme options are" + themes_list)
    themes_choice = input("Type out the name of the theme you want: ")
    while themes_choice not in themes_list:
        print("Invalid Theme. Theme options are " + themes_list)
        themes_choice = input("Invalid theme. Type out the name of the theme you want: ")
    
    rounds_choice = int(input("Enter the number of rounds you would like to play (1 to 5): "))
    while rounds_choice < 0 or rounds_choice > 5: 
        rounds_choice = int(input("Invalid number of rounds. Enter the number of rounds you would like to play (1 to 5): "))



#Game Function
def actual_game(pn,rn):
    players = []

    for i in range(rn):
        for j in range(pn):

while play_again.lower() == "yes":
    actual_game(player_num,rounds_choice)
    play_again = input("Would you like to play again? Enter (yes or no)")

#Finish Game
if play_again == "no":
    print("Thanks for playing Cards Against Humanity!")
    exit()









