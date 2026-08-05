import re
import time
import sys
import questionary
import random
from termcolor import cprint, colored

game_over = False

wave = 1


class Player:
    def __init__(self):
        self.bullets = 0

    def player_choice(self):
        if self.bullets > 0:
            choice = questionary.select(
                "What do you want to do?",
                choices=["Reload", "Block", "Shoot", "Quit Game"],
            ).ask()  # returns value of selection
        else:
            choice = questionary.select(
                "What do you want to do?", choices=["Reload", "Block", "Quit Game"]
            ).ask()  # returns value of selection
        return choice

    def computer_choice(self, player_bullets):
        if self.bullets == 0 and player_bullets > 0:
            result = random.choices(["Reload", "Block"], weights=[0.35, 0.65])
            return result[0]
        elif self.bullets == 0 and player_bullets == 0:
            return "Reload"

        if self.bullets > 0 and player_bullets == 0:
            result = random.choices(["Reload", "Shoot"], weights=[0.2, 0.8])
            return result[0]

        return random.choice(["Reload", "Block", "Shoot"])


def main():
    equation = input("Equation: ").strip()
    parse_input(equation)


def parse_input(equation):
    
    equation_match = re.search(
        r"^([-+]?\d*.?\d+)\s*([+*/-])\s*([-+]?\d*.?\d+)$", equation
    )
    if equation == "007":
        cprint("You've entered the Game mode", "green")
        game_mode()
    elif equation_match:
        answer = calculate(equation_match)
        print(answer)
        return answer
    else:
        return print("Invalid Input")
    
    
def calculate(equation):
    num1, operator, num2 = equation.groups()
    num1 = int(num1)
    num2 = int(num2)
    match operator:
        case "+":
            return num1 + num2
        case "-":
            return num1 - num2
        case "*":
            return num1 * num2
        case "/":
            try:
                return num1 / num2
            except ZeroDivisionError:
                return "Can't divide by zero"


def game_mode():
    user_player = Player()
    cpu_player = Player()
    time.sleep(1)
    preamble()
    time.sleep(0.5)

    while game_over != True:
        global wave
        print(f"{colored(f"Wave {wave}", "green")}")
        player_choice = user_player.player_choice()
        computer_choice = cpu_player.computer_choice(player_bullets=user_player.bullets)
        time.sleep(0.5)

        if player_choice == "Quit Game":
            sys.exit(f"{colored("You quit the game", "red")}")

        print(f"You choose to {colored(player_choice, "blue")}")
        time.sleep(0.25)
        print(f"The computer chooses to {colored(computer_choice, "red")}")
        time.sleep(0.25)

        check_choices(player_choice, computer_choice, user_player, cpu_player)
        print(
            f"The Player has {colored(user_player.bullets, "yellow")} bullet(s) and the Computer has {colored(cpu_player.bullets, "yellow")} bullet(s)"
        )
        wave += 1
        time.sleep(0.5)
        

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
        player.bullets -= 1
        cpu.bullets -= 1


def Game_Complete(winner):
    global wave, game_over
    game_over = True
    if winner == "Player":
        new_highscore(wave)
        return sys.exit(f"You won in {colored(f"{wave} waves", "green")}!")
    elif winner == "CPU":
        return sys.exit(f"The Computer won in {colored(f"{wave} waves", "green")}!")


def new_highscore(wave=100000000):
    try:
        with open("high_score.txt", "r") as file:
            highscore = file.read().strip()
            if highscore and int(highscore) <= wave:
                return highscore
            else:
                print("Highscore Updated!")
                with open("high_score.txt", "w") as file:
                    file.write(str(wave))
                return 0
    except (OSError, ValueError):
        print("Highscore Updated!")
        with open("high_score.txt", "w") as file:
            file.write(str(wave))
        return 0


def preamble():
    print(f"""Welcome to 007,
A game about {colored("strategy", "yellow")}, {colored("planning", "yellow")}, and {colored("feeling like James Bond", "yellow")}.
You and a computer have 3 options every turn:
1. {colored("Reload", "blue")}
2. {colored("Block", "blue")}
3. {colored("Shoot", "red")}
Your mission is to take out the computer by shooting when the computer is reloading.
You can't shoot if you don't have any bullets, and you and the computer can store bullets. Good Luck!
Your Highscore is {colored(new_highscore())} waves.""")
    return True


if __name__ == "__main__":
    main()
