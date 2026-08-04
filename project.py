import re
import time
import sys
import questionary
import random
from termcolor import cprint, colored


game_over = False
reload_text = colored("Reload","blue")
block_text = colored("Block", "cyan")
shoot_text = colored("Shoot", "red")

class Player:
    def __init__(self):
        self.bullets = 0
    
    def player_choice(self):
        if self.bullets > 0:
            choice = questionary.select(
                "What do you want to do?",
                choices=[
                    "Reload",
                    "Block",
                    "Shoot",
                    "Quit Game"
            ]).ask()  # returns value of selection
        else:
            choice = questionary.select(
                "What do you want to do?",
                choices=[
                    "Reload",
                    "Block",
                    "Quit Game"
            ]).ask()  # returns value of selection
        return choice

    def computer_choice(self):
        if self.bullets == 0:
            return random.choice(["Reload", "Block"])
        if self.bullets > 0:
            return random.choice(["Reload", "Block", "Shoot"])

def main():
    equation = input("Equation: ").strip()
    equation_match = re.search(r"^([-+]?\d*.?\d+)\s*([+*/-])\s*([-+]?\d*.?\d+)$", equation)
    if equation == "007":
        cprint("You've entered the Game mode", "green")
        game_mode()
    elif equation_match:
        calculate(equation_match)

def game_mode():
    user_player = Player()
    cpu_player = Player()
    time.sleep(1)
    preamble()
    time.sleep(0.5)
    
    while game_over != True:
        player_choice = user_player.player_choice()
        computer_choice =cpu_player.computer_choice()
        
        if player_choice == "Quit Game":
            sys.exit(f"{colored("You quit the game", "red")}")
        
        print(f"You choose to {colored(player_choice, "blue")}")
        time.sleep(0.5)
        print(f"The computer chooses to {colored(computer_choice, "red")}")
        
        check_choices(player_choice, computer_choice, user_player, cpu_player)
        print(f"The Player has {colored(user_player.bullets, "yellow")} bullet(s) and the Computer has {colored(cpu_player.bullets, "yellow")} bullet(s)")
        

def calculate(equation):
    num1, operator, num2 = equation.groups()
    num1 = int(num1)
    num2 = int(num2)
    match operator:
        case "+":
            print(num1 + num2)
        case "-":
            print(num1 - num2)
        case "*":
            print(num1 * num2)
        case "/":
            try:
                print(num1 / num2)
            except ZeroDivisionError:
                print("Can't divide by zero")
    
def check_choices(pc, cc, player, cpu):
    if pc == "Reload" and cc == "Reload":
        player.bullets += 1
        cpu.bullets += 1
    elif pc == "Reload" and cc == "Block":
        player.bullets += 1
    elif pc == "Reload" and cc == "Shoot":
        Game_Complete("CPU")
    
    elif pc == "Block" and cc == "Reload":
        cpu.bullets += 1
    elif pc == "Block" and cc == "Block":
        pass
    elif pc == "Block" and cc == "Shoot":
        cpu.bullets -= 1
    
    elif pc == "Shoot" and cc == "Reload":
        Game_Complete("Player")
    elif pc == "Shoot" and cc == "Block":
        player.bullets -= 1
    elif pc == "Shoot" and cc == "Shoot":
        pass
def Game_Complete(winner):
    game_over == True
    if winner == "Player":
        sys.exit("The Player has won")
    elif winner == "CPU":
        sys.exit("The Computer has won")

def preamble():
        print(f"""Welcome to 007,
A game about {colored("strategy", "yellow")}, {colored("planning", "yellow")}, and {colored("feeling like James Bond", "yellow")}.
You and a computer have 3 options every turn:
1. {colored("Reload", "blue")}
2. {colored("Block", "blue")}
3. {colored("Shoot", "red")}
Your mission is to take out the computer by shooting when the computer is reloading.
You can't shoot if you don't have any bullets, and you and the computer can store bullets. Good Luck!""")

if __name__ == "__main__":
    main()