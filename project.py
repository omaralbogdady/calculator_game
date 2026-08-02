import re

def main():
    equation = input("Equation: ").strip()
    equation_match = re.search(r"^([-+]?\d*.?\d+)\s*([+*/-])\s*([-+]?\d*.?\d+)$", equation)
    if equation == "8008":
        print("You've entered the Game mode")
        game_mode()
    elif equation_match:
        calculate(equation_match)
        

def game_mode():
    pass

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