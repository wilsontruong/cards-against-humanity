from random import randint
import pickle
status = "Unvalid"
play_again = "yes"


print("Welcome to Cards Against Humanity!")

#Classes
class Theme():
    def __init__(self,theme_name='', prompts=[], answers=[],num_players = 6):
        self.theme_name = theme_name
        self.prompts = prompts
        self.answers = answers
        self.num_players = num_players
    def set_theme_name(self):
        self.theme_name = input("enter your theme name: ")
    def verify_theme_name(self):
        print("Does your theme name look correct?")
        print("Theme Name: ", self.theme_name)
        decision = input("Press 'y' if yes and 'n' if no \n")
        if decision == 'n':
            print("Please recreate your theme name: ")
            self.set_theme_name()

    def set_prompt(self):
        self.prompts = []
        n= int(input("Enter the number of prompts you would like for your theme:\n"))
        k = 0
        while k==0:
            if n < 7:
                print("You must have at least 7 prompts!\n")
                n= int(input("Enter the number of prompts you would like for your theme:\n"))
            else:
                print("Type in the prompts for your custom theme.")
                k = 1
        for i in range(1,n+1):
            self.prompts.append(input("prompt {}: ".format(i)))
    def verify_prompts(self):
        print("Do your prompts looks correct?")
        print("Theme Prompts: ")
        for i in self.prompts:
            print(i)
        decision = input("Press 'y' if yes and 'n' if no \n")
        while decision == 'n':
            print("Please recreate your prompts: ")
            self.set_prompt()
    def set_answers(self):
        self.answers = []
        n= 5*self.num_players
        print("You have a total of {} cards. Add your answers: ".format(n))
        for i in range(1,n+1):
            self.answers.append(input("answer {}: ".format(i)))
    def verify_answers(self):
        print("Do your answers looks correct?")
        print("Theme Answers: ")
        for i in self.answers:
            print(i)
        decision = input("Press 'y' if yes and 'n' if no \n")
        if decision == 'n':
            print("Please recreate your answers: ")
            self.set_answers()
    def set_default_theme():
        pass

if __name__ == "__main__":
    #Level 1: Play, Settings, or Exit
    level1 = input("Type 1 to play, type 2 for settings, or type 3 to exit: ")
    #while level1 != '1' or level1 != '2' or level1 != '3':
        #level1 = input("Invalid Input: Type 1 to play, type 2 for settings, or type 3 to exit: ")
    theme_name_list = []
    theme_list =[]
    write_theme_file = open("newtheme.pickle", "wb") 
    pickle.dump(theme_list, write_theme_file)
    write_theme_file.close()
    read_theme_file = open("newtheme.pickle","rb")
    theme_list = pickle.load(read_theme_file)
    Default_theme  = Theme('Family Friendly', [
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
                        ],  [
                        "A cloud that rains diarrhea","Batman in a skirt","George Washington eating an apple","A big wet kiss from Great Aunt Sharon","Eight hours of video games.","Hanging out with Zendaya","Eating a lightbulb","A burrito smoothie","Covid 19","Eating Jelly"
                        ,"The police","Blowing up the moon","Turning into a super saiyan","Canada","Australia","United States","A hot cup of tea","Dirty upperware","Phineas and Ferb","Michael Jordan's Auntie"
                        ,"Cheeto fingers","TikTok","An iPhone with a broken screen","Polar Bears","Bob the builder dancing","Dora fighting Diego","A talking lion","A Democrat","A Republican","Idiots"
                        ,"The Magic School Bus","Ramen Noodles","Spaghetti Tacos","Pizza Hat","Climate Change","Box Fort","Chevy Truck","Honda Civic","Laptop","The loose skin at the joint of the elbow called a weenus"
                        ,"Pikachu","Politics","Crying in the bathroom","A bathtub of cottage cheese","JoJo Siwa","Ninjas","Happiness","Doing Karate","A lot of money","Being a good programmer"
                        ,"A hot air balloon powered by burps","The best game ever. Fortnite.","Darth Vader","Bacon strips","The government","Ice cream","The Harlem Shake","Youtube Rewind","Eating waffles","Ariana Grande"
                        ,"A dancing toddler","BBQ chips","C++","Python","IDK IDC ANYMORE","Random Prompt answer","Chicken nuggets","This is tedious","Read if you are not cool","1980's Music"
                        ],)
    if Default_theme not in theme_list:
        theme_list.append(Default_theme)
    theme_name_list.append(Default_theme.theme_name)
    for i in theme_list:
        if i.theme_name != Default_theme.theme_name:
            theme_name_list.append(i.theme_name)


    #Level 2: Player Number Selection
    if level1 == '1':
        player_num = int(input("Input the number of players playing (3 to 6): "))
        while player_num < 3 or player_num > 6:
            player_num = int(input("Invalid number of players. Input the number of players playing (3 to 6 players): "))
        status = "Valid"

    #Level 2: Settings Selection
    elif level1 == '2':
        decision = input("would you like to add a new custom theme? (yes/no)")
        if decision == 'yes':
            print("we are creating a new theme")
            theme_list.append(Theme())
            theme_list[-1].set_theme_name()
            theme_name_list.append(theme_list[-1].theme_name)
            theme_list[-1].set_prompt()
            theme_list[-1].set_answers()  
            write_theme_file = open("newtheme.pickle", "wb") 
            pickle.dump(theme_list, write_theme_file)
            write_theme_file.close()
            print("New theme created. Exiting the game. Please rerun the program to play the game with recently added theme.")
            exit()

        
    else:
        exit()

    
    #Level 3: Theme and number of rounds selection. 
    if status == "Valid":
        print("Theme options are", theme_name_list)
        themes_choice = input("Type out the name of the theme you want: ")
        while themes_choice not in theme_name_list:
            print("Invalid Theme. Theme options are ", theme_name_list)
            themes_choice = input("Type out the name of the theme you want: ")
        for theme in theme_list:
            if themes_choice == theme.theme_name:
                current_theme = theme
        
        # rounds_choice = int(input("Enter the number of rounds you would like to play (1 to 5): "))
        # while rounds_choice < 0 or rounds_choice > 5: 
        #     rounds_choice = int(input("Invalid number of rounds. Enter the number of rounds you would like to play (1 to 5): "))

#Game Function
def actual_game(pn,prompts,prompt_answers):
    import copy
    players = []
    players_hand = []
    copied_answers = prompt_answers.copy()
    copied_prompts = prompts.copy()
    points = []
    temp_answers = []

    for a in range(0,pn):
        players.append("player_"+str(a))
    
    for b in range(0,pn):
        players_hand.append([])

    for z in range(0,pn):
        points.append(0)

    #Hands out 5 cards to each player
    # print("TESSSST")
    # print(copied_answers)
    # print(players_hand)
    x = len(copied_answers)
    for c in range(0,pn):
        for d in range(5):
            temp = randint(0,x-1)
            x = x - 1
            players_hand[c].append(copied_answers[temp])
            del copied_answers[temp]

    funniest_answer = " "

    y = len(copied_prompts)
    for e in range(0, pn):
        temp_answers = []
        temp2 = randint(0,y-1)
        y = y - 1
        print(copied_prompts[temp2])
        for g in range(0, pn):
            if g != e:
                print(players_hand[g])
                answer_choice = int(input("Player " + str(g) + ", pick which answer you would like to use for this prompt? (0 to 4): "))
                temp_answers.append(players_hand[answer_choice])
                del players_hand[g][answer_choice]
                players_hand[g].append(copied_answers[randint(0,y-1)])
            else:
                continue
            
        funniest_answer = int(input("Which player had the funniest answer. (Note: 0 Correlates to the most left answer and 4 correlates to the most right): "))

    return(points)

while play_again.lower() == "yes":
    final_scores = actual_game(player_num,current_theme.prompts,current_theme.answers)
    print("The final scores are: ", final_scores)
    play_again = input("Would you like to play again? Enter (yes/no): ")

#Finish Game
if play_again.lower() == "no":
    print("Thanks for playing Cards Against Humanity!")
    exit()