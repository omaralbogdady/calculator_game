def main():
    equation = input("Equation: ")
    if equation == "8008":
        game_mode()
    else:
        num1, operator, num2 = equation.split(" ")
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
                if num2 != "0":
                    print(num1 / num2)
                else:
                    print("Can't divide by zero")
            case "**":
                print(num1 ** num2)
            case "//":
                if num2 != "0":
                    print(num1 / num2)
                else:
                    print("Can't divide by zero")

def game_mode():
    print("GAME MODE ENABLED")
    
if __name__ == "__main__":
    main()