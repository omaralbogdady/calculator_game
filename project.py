import re
import time
import sys

class Player:
    def __init__(self, health=20, rta=2, type="Random"):
        self.health = health
        self.rta = rta
        self.type = type

    @classmethod
    def get_player_type(cls):
        print("""There are 4 classes of players:
              1. Light: fights every turn, has 20 hp, and hits between 5-10 hp
              2. Medium: Fights every 2 turns, has 27 hp, and hits between 7-15 hp
              3. Heavy: Fights every 3 turns, has 35 hp, and hits between 13-20 hp
              4. Random (If you're feeling lucky!): Fights every 1-3 turns, has 15-40 hp and hits between 1-22 hp
              """)
        try:
            choice = int(input("please input the class you would like based on their number (1 for light, 2 for medium...) or 0 if you would like to quit the game: "))
            match choice:
                case 0:
                    sys.exit("You have quit the game")
                case 1:
                    return cls(20, 1, "light")
                case 2:
                    return cls(27, 2, "Medium")
                case 3:
                    return cls(35, 3, "Heavy")
                case 4:
                    return cls(type="Random")
                case _:
                    print("Please Pick a class from the available options")
                    time.sleep(1.5)
                    cls.get_player_type()
        except ValueError:
            print("Please Pick a class from the available options")
            time.sleep(1.5)
            cls.get_player_type()

def main():
    equation = input("Equation: ").strip()
    equation_match = re.search(r"^([-+]?\d*.?\d+)\s*([+*/-])\s*([-+]?\d*.?\d+)$", equation)
    if equation == "8008":
        print("You've entered the Game mode")
        game_mode()
    elif equation_match:
        calculate(equation_match)

def game_mode():
    time.sleep(1)
    player = Player.get_player_type()

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
    
if __name__ == "__main__":
    main()