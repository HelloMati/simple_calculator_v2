def add(x, y):
    """Add two fabulous numbers and return the result."""
    return x + y

def subtract(x, y):
    """Subtract the second number from the first and return the result."""
    return x - y

def multiply(x, y):
    """Multiply two numbers and return the result!"""
    return x * y

def divide(x, y):
    """Divide the first number by the second. Just make sure Ken isn't trying to divide by zero!"""
    if y == 0:
        raise ValueError("Oops! Even in Malibu, you can’t divide by zero, Ken!")
    return x / y

def barbie_calculator():
    """Start your glamorous calculations! Malibu maths, here we come!"""
    print("Welcome to Barbie's Malibu Calculator! 🌴💖")
    while True:
        try:
            num1 = int(input("Enter your first fabulous number: "))
            operator = input("Choose your operation ('+', '-', '*', '/'): ")
            num2 = int(input("Enter your second sparkling number: "))
        except ValueError:
            print("Uh-oh! Only totally valid numbers, please! Let's try again 💅")
            continue

        if operator == '+':
            result = add(num1, num2)
        elif operator == '-':
            result = subtract(num1, num2)
        elif operator == '*':
            result = multiply(num1, num2)
        elif operator == '/':
            try:
                result = divide(num1, num2)
            except ValueError as e:
                print(e)
                continue
        else:
            print("Ken, that's not a valid operator! Stick to '+', '-', '*', or '/'.")
            continue

        print(f"✨ The result is: {result}! Totally Malibu, right? ✨")

        exit_choice = input("Press 'q' to say goodbye to Malibu or hit enter to keep calculating in style: ")

        if exit_choice.lower() == 'q':
            print("Bye-bye, Barbie! Malibu waves are calling! 🌊💖")
            break

        print()  

if __name__ == "__main__":
    barbie_calculator()
