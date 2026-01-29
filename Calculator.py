HISTORY_FILE = "history.txt"

def show_history():
    with open(HISTORY_FILE, 'r') as file:
        lines = file.readlines()
        if len(lines) == 0:
            print("No history found!")
        else:
            for line in reversed(lines):
                print(line.strip())

def clear_history():
    open(HISTORY_FILE, 'w').close()
    print('History cleared.')
    
def save_to_history(equation, result):
    with open(HISTORY_FILE, 'a') as file:
        file.write(equation + " = " + str(result) + "\n")

def calculator(user_input):
    parts = user_input.split()
    if len(parts) != 3:
        print('Invalid input. Use format: number operator number')
        return
    try:
        num1 = float(parts[0])
        op = parts[1]
        num2 = float(parts[2])
    except ValueError:
        print("Invalid numbers!")
        return
    
    if op == "+":
        result = num1 + num2
    elif op == "-":
        result = num1 - num2
    elif op == "*":
        result = num1 * num2
    elif op == "/":
        if num2 == 0:
            print('Cannot divide by zero')
            return
        result = num1 / num2
    else:
        print('Invalid operator')
        return
    
    if result.is_integer():
        result = int(result)
    print("Result:", result)
    save_to_history(user_input, result)

def main():
    print('___Simple Calculator___')
    while True:
        user_input = input("Enter calculation (or 'exit', 'history', 'clear'): ")
        if user_input.lower() == 'exit':
            print('Goodbye')
            break
        elif user_input.lower() == 'history':
            show_history()
        elif user_input.lower() == 'clear':
            clear_history()
        else:
            calculator(user_input)

main()