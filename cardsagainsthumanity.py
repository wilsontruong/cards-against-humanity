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
    


            



Custom_Theme = Theme(3)
Custom_Theme.set_theme_name()
Custom_Theme.set_prompt()
Custom_Theme.set_answers()



    


            
            

            
