"""
   NotaTomagotchi
   A clone of Tamagotchi
   11/24/15
   Evan Wilt
"""

from tkinter import *
from tkinter import messagebox
import random

content_tamagotchi = """.^._.^.
| . . |
(  ---  )
.'     '.
|/     \|
\ /-\ /
V   V"""

happy_tamagotchi = """.^._.^.
| 0 0 |
(  \-/  )
.'     '.
|/     \|
\ /-\ /
V   V"""

sad_tamagotchi = """.^._.^.
| - - |
(  /-\  )
.'     '.
|/     \|
\ /-\ /
V   V"""

dead_tamagotchi = """____
//  +  \\
||  RIP  |
||       |
      ||       |      
\||/\/\//\|/"""



class App(Tk):
    def __init__(self):
        Tk.__init__(self)
        
        self.hunger = 8
        self.happiness = 8
        
        self.avatar_font = ("Courier", "16")
        self.title("NotaTomagotchi")
        self.ask_name()
        self.name_label()
        self.avatar()
        self.buttons()
        self.status_output()
        self.health_status()
        self.happiness_status()
        self.hunger_status()
        self.dec_happiness()
        self.dec_hunger()

# Opens a box asking for the tamagotchi's name and outputs it in a label

    def ask_name(self):
        self.name = simpledialog.askstring("", "What is your Tamagotchi's name?")
        

    def name_label(self):
        Label(self, text = "Name: ").grid(row = 1, column = 0)
        self.happiness_label = Label(self, text = self.name)
        self.happiness_label.grid(row = 1, column = 1, sticky = "we")

# Creates the avatar for the tamagotchi using a label

    def avatar(self):
        self.avatar = Label(self, text = content_tamagotchi, font = self.avatar_font, anchor = "center")
        self.avatar.grid(row = 5, column = 0)

# Creates buttons to feed and play which calls add_hunger/happiness and hunger/happiness_status

    def buttons(self):
        self.feed = Button(self, text = "Feed")
        self.feed.grid(row=15, column=0)
        self.feed["command"] = self.add_hunger_and_status

        self.play = Button(self, text = "Play")
        self.play.grid(row=15, column=1)
        self.play["command"] = self.add_happiness_and_status

# Combines both add_hunger/happiness into one method for use with the buttons

    def add_hunger_and_status(self):
        self.add_hunger()
        self.hunger_status()
        
    def add_happiness_and_status(self):
        self.add_happiness()
        self.happiness_status()
 
# Add 1 to happiness/hunger

    def add_hunger(self):
        self.hunger += 1

    def add_happiness(self):
        self.happiness += 1

# Decreases happiness/hunger by one

    def dec_hunger(self):
        if self.hunger < 11:
            if self.hunger > 0:
                self.hunger -= 1
                
            else:
                self.after_cancel(self.dec_happiness)
                self.after_cancel(self.dec_hunger)
                self.after_cancel(self.happiness_status)
                self.after_cancel(self.hunger_status)
                
        else:
            self.after_cancel(self.dec_happiness)
            self.after_cancel(self.dec_hunger)
            self.after_cancel(self.happiness_status)
            self.after_cancel(self.hunger_status)
            
    def dec_happiness(self):
        if self.happiness > 1:
            if self.hunger < 11:
                self.happiness -= 1
                
            else:
                self.after_cancel(self.dec_happiness)
                self.after_cancel(self.dec_hunger)
                self.after_cancel(self.happiness_status)
                self.after_cancel(self.hunger_status)
                
        else:
            self.after_cancel(self.dec_happiness)
            self.after_cancel(self.dec_hunger)
            self.after_cancel(self.happiness_status)
            self.after_cancel(self.hunger_status)
            
# Creates labels which will output the status of the tamagotchi

    def status_output(self):
        Label(self, text = "Hunger").grid(row = 25, column = 0)
        self.hunger_label = Label(self, bg = "#fff", anchor = "w", relief = "groove")
        self.hunger_label.grid(row = 25, column = 1, sticky = "we")
        
        Label(self, text = "Happiness").grid(row = 20, column = 0)
        self.happiness_label = Label(self, bg = "#fff", anchor = "w", relief = "groove")
        self.happiness_label.grid(row = 20, column = 1, sticky = "we")
        
        Label(self, text = "Health").grid(row = 30, column = 0)
        self.health_label = Label(self, bg = "#fff", anchor = "w", relief = "groove")
        self.health_label.grid(row = 30, column = 1, sticky = "we")
        
# Changes the labels every second of the status_output based upon what int hunger, happiness are
# If hunger or happiness is too high/low, the tamagotchi dies and a messagebox notifies the user, then closes the app

    def hunger_status(self):
        if 9 <= self.hunger <= 10:
            self.hunger_label["text"] = "Stuffed"

        elif 5 <= self.hunger <= 8:
            self.hunger_label["text"] = "Full"

        elif 3 <= self.hunger <= 4:
            self.hunger_label["text"] = "Hungry"

        elif 1 <= self.hunger <= 2:
            self.hunger_label["text"] = "Starved"

        elif self.hunger > 10:
            self.after_cancel(self.dec_happiness)
            self.after_cancel(self.dec_hunger)
            self.after_cancel(self.happiness_status)
            self.after_cancel(self.hunger_status)
            self.after_cancel(self.health_status)
            self.happiness_label["text"] = "Dead"
            self.hunger_label["text"] = "Dead"
            self.health_label["text"] = "Dead"
            self.avatar["text"] = dead_tamagotchi
            messagebox.showinfo(title = "Your Tamagotchi Died!", message = "Your tamagotchi has died from overfeeding. The game will now close.")
            App.destroy(self)

            
        elif self.hunger == 0:
            self.after_cancel(self.dec_happiness)
            self.after_cancel(self.dec_hunger)
            self.after_cancel(self.happiness_status)
            self.after_cancel(self.hunger_status)
            self.after_cancel(self.health_status)
            self.happiness_label["text"] = "Dead"
            self.hunger_label["text"] = "Dead"
            self.health_label["text"] = "Dead"
            self.avatar["text"] = dead_tamagotchi            
            messagebox.showinfo(title = "Your Tamagotchi Died!", message = "Your tamagotchi has died from starvation. The game will now close.")
            App.destroy(self)

        self.after(1000, self.hunger_status)

    def happiness_status(self):
        self.avatar_status()

        if 7 <= self.happiness <= 9:
            self.happiness_label["text"] = "Happy"

        elif 4 <= self.happiness <= 6:
            self.happiness_label["text"] = "Content"


        elif 2 <= self.happiness <= 3:
            self.happiness_label["text"] = "Depressed"

        elif self.happiness == 1:
            self.after_cancel(self.dec_happiness)
            self.after_cancel(self.dec_hunger)
            self.after_cancel(self.happiness_status)
            self.after_cancel(self.hunger_status)
            self.after_cancel(self.health_status)
            self.happiness_label["text"] = "Dead"
            self.hunger_label["text"] = "Dead"
            self.health_label["text"] = "Dead"
            messagebox.showinfo(title = "Your Tamagotchi Died!", message = "Your tamagotchi has died from heartache. The game will now close.")
            App.destroy(self)
            
        self.after(1000, self.happiness_status)

# Assigns a random int to health and updates the status every 10 seconds. If it's 5, it is sick and happiness/hunger deplete faster
# Also repeats dec_happiness/hunger every 8/10 seconds if healthy

    def health_status(self):
        self.health = random.randint(1, 10)
        self.health = int(self.health)

        if self.health == 5:
            self.health_label["text"] = "Sick"
            self.after_cancel(self.dec_happiness)
            self.after_cancel(self.dec_hunger)
            self.after(6000, self.dec_happiness)
            self.after(4000, self.dec_hunger)

        else:
            self.health_label["text"] = "Healthy"
            self.after_cancel(self.dec_happiness)
            self.after_cancel(self.dec_hunger)
            self.after(8000, self.dec_hunger)
            self.after(12000, self.dec_happiness)

        self.after(10000, self.health_status)
        
# Changes avatar based upon what int happiness is

    def avatar_status(self):
        if 6 <= self.happiness <= 9:
            self.avatar["text"] = happy_tamagotchi

        elif 4 <= self.happiness <= 5:
            self.avatar["text"] = content_tamagotchi

        elif 2 <= self.happiness <= 3:
            self.avatar["text"] = sad_tamagotchi
            
        else:
            self.avatar["text"] = dead_tamagotchi            
            
def main():
  app = App()
  app.mainloop()

if __name__ == "__main__":
  main()
  
