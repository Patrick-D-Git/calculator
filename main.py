# A simple calculator

first_number = int(input("Please provide first number: "))

chosen_operator = input("Please choose what type of operator to use '+, -, *, /' : ")

second_number = int(input("Please provide second number: "))

if chosen_operator == "+":
    answer = first_number + second_number
    print(f"The answer is {answer}.")
elif chosen_operator == "-":
    answer = first_number - second_number
    print(f"The answer is {answer}.")
elif chosen_operator == "*":
    answer = first_number * second_number
    print(f"The answer is {answer}.")
elif chosen_operator == "/":
    answer = first_number / second_number
    print(f"The answer is {answer}.")
else:
    print("Please only choose operator provided")
