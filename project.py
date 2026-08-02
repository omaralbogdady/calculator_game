import re

def main():
    equation = input("Equation: ")
    equation_match = re.search(r"^([-+]?\d+)\s*([+*/-])\s*([-+]?\d+)$", equation)
    if equation == "8008":
        print("You've entered the Game mode")
        game_mode()
    elif equation_match:
        num1, operator, num2 = equation_match.groups()
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

def game_mode():
    pass
    
    
if __name__ == "__main__":
    main()