import json
DEFAULT_FILENAME = "data.json"  # Example constant

def get_int(prompt: str) -> int:
    """Safely get an integer from the user."""
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Please enter a valid integer.")

def calculator(a: int, b: int, operation: str) -> float:
    """Perform basic arithmetic operations."""
    if operation == "add":
        return a + b
    elif operation == "sub":
        return a - b
    elif operation == "mul":
        return a * b
    elif operation == "div":
        if b == 0:
            raise ValueError("Cannot divide by zero")
        return a / b
    else:
        raise ValueError("Invalid operation")

def analyze_text(text: str) -> dict:
    words = text.split()
    return {
        "characters": len(text),
        "words": len(words),
        "unique_words": len(set(words))
    }

def save_to_file(filename: str, data):
    with open(filename, "w") as f:
        json.dump(data, f)


def load_from_file(filename: str):
    try:
        with open(filename, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        print("File not found!")
        return None


def bonus_features(*args, **kwargs):
    print("Args:", args)
    print("Kwargs:", kwargs)

def main():
    while True:
        print("\nWelcome to Smart Student Utility System")
        print("1. Enter a safe integer")
        print("2. Calculator")
        print("3. Analyze a text")
        print("4. Save data to file")
        print("5. Load data from file")
        print("6. Bonus features")
        print("7. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            number = get_int("Enter an integer: ")
            print(f"You entered: {number}")

        elif choice == "2":
            a = get_int("Enter first number: ")
            b = get_int("Enter second number: ")
            operation = input("Enter operation (add/sub/mul/div): ").lower()
            try:
                result = calculator(a, b, operation)
                print(f"Result: {result}")
            except ValueError as e:
                print(f"Error: {e}")

        elif choice == "3":
            text = input("Enter text: ")
            stats = analyze_text(text)
            print(f"Characters: {stats['characters']}")
            print(f"Words: {stats['words']}")
            print(f"Unique words: {stats['unique_words']}")

        elif choice == "4":
            filename = input("Enter filename to save: ") or DEFAULT_FILENAME
            data = input("Enter data to save: ")
            save_to_file(filename, data)
            print(f"Data saved to {filename}")

        elif choice == "5":
            filename = input("Enter filename to load: ") or DEFAULT_FILENAME
            data = load_from_file(filename)
            if data:
                print(f"Data loaded: {data}")

        elif choice == "6":
            bonus_features(10, 20, option="demo")  

        elif choice == "7":
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
