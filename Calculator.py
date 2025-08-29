HISTORY = "HISTORY.txt"

def show_history():
    file = open(HISTORY, "r")
    lines = file.readlines()
    if len(lines) == 0:
        print("NO HISTORY FOUND !")
    else:
        for line in reversed(lines):
            print(line, end="")
    file.close()

def clear_history():
    file = open(HISTORY, "w")
    file.close()
    print("HISTORY CLEARED.")

def save_history(equation , result):
    file = open(HISTORY, "a")
    file.write(equation + " = " + str(result) + "\n")
    file.close()

def calculate(user_input):
    parts = user_input.split()
    
    if len(parts) != 3:
        print("INVALID INPUT. Use formet: Number Operator Number (e.g. 8 + 8)")
        return
    num1 = float(parts[0])
    op = parts[1]
    num2 = float(parts[2])

    if op == "+":
        result = num1 + num2
    elif op == "-":
        result = num1 - num2
    elif op == "*":
        result = num1 * num2
    elif op == "/":
        if num2 == 0:
            print("Can't Divide With 0")
            return
        result = num2 / num2
    else:
        print("Invalid Operator")
        return
    if int(result) == result:
        result = int(result)
    print("Result : ",result)
    save_history(user_input, result)

def main():
    print("--- WELCOME TO SIMPLE CALCULATOR ---")
    while True:
        user_input = input("Enter Calculation ( + - * / ) or Command (history, clear, exit) = ").lower()
        if user_input == "exit":
            print("THANKYOU \U0001F607 Goodbye...")
            break
        elif user_input == "history":
            show_history()
        elif user_input == "clear":
            clear_history()
        else:
            calculate(user_input)

main()

    




