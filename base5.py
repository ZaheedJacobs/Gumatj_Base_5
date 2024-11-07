# Test program for Gumatj (base 5) calculations

import gumatj
import re

def convert(user_choice: str):
    action: str = user_choice[:1]
    # Conversion between gumatj(base 5) and decimal(base 10)
    num = int(user_choice[2:])
    if action == "g":
        answer = gumatj.gumatj_to_decimal(num)
        return answer

    else:
        answer = gumatj.decimal_to_gumatj(num)
        return answer

def add_or_multiply(user_choice: str):
    action: str = user_choice[:1]
    num_1, num_2 = map(int, user_choice[2:].split(" "))
    
    if action.lower() == "a":
        answer = gumatj.gumatj_add(num_1, num_2)
        return answer
        
    else:
        answer = gumatj.gumatj_multiply(num_1, num_2)
        return answer

def print_instructions():
    instructions = """Gumatj/Base 5 is a numbering system with numbers from 0 to 4 used to represent any real number
    
For this program, you will choose 1 of 4 tests:
    
1) \"d (number)\"-> converts a number from gumatj into decimal
2) \"g (number)\"-> converts a number from decimal(base 10) into gumatj(base 5)
3) \"a (number_1) (number_2)\"-> adds 2 numbers together in base 5
4) \"m (number_1) (number_2)\"-> multiplies 2 numbers together in base 5"""
    
    print(instructions)

def main():
    print_instructions()
    print()
    choice = input("Choose test:\n")
    
    if re.match(r"(g|d) \d+", choice):
        print("calling function")
        result = convert(choice)
        print("called function")
        print(f"answer: {result}")
    
    elif re.match(r"(a|m) \d+ \d+", choice):
        print("calling function")
        result = add_or_multiply(choice)
        print("called function")
        print(f"answer: {result}")
    
    else:
        print("Invalid choice. Please try again")
        choice = input("Choose test:\n")

if __name__ == "__main__":
    main()