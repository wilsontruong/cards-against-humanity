import time

class Theme():
    def __init__(self,theme_name='', prompts=[], answers=[],num_players = 3):
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
            if n < 5:
                print("You must have at least 5 prompts!\n")
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
    
          

import copy
import pickle
theme_name_list = ['Family Friendly']
theme_list =[]
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

theme_list.append(Default_theme)
print(theme_list)
def save_themes(theme_list):
    print("we are creating a new theme")
    theme_list.append(Theme(6))
    theme_list[-1].set_theme_name()
    theme_name_list.append(theme_list[-1].theme_name)
    theme_list[-1].set_prompt()
    theme_list[-1].set_answers()  
    write_theme_file = open("newtheme.pickle", "wb") 
    pickle.dump(theme_list, write_theme_file)
    write_theme_file.close()


'''Extra code to delete the themes/objects from the pickle file'''
'''may be written.Such as clearing out the theme_list and then saving 
it using pickle. Or converting the file contents into a list and then
deleting themes from that list.
Depends on time available. 
'''



    


            
            

            
