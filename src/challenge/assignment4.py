# "Choose a number:"
# 15
# "Choose another one:"
# 15
# "Choose an operation:"
#     "Options are: +, -, * or /."
#     "Write 'exit' to finish."
# "+"
# "Result: 30"

# BLUEPRINT | DONT EDIT
playing = True

a = int(input("Choose a number:\n"))
b = int(input("Choose another one:\n"))
operation = input(
    "Choose an operation:\n    Options are: + , - , * or /.\n    Write 'exit' to finish.\n"
)
# /BLUEPRINT

# 👇🏻 YOUR CODE 👇🏻:
def calculator(number, another, operation):
    if operation == "+":
        return number + another
    elif operation == "-":
        return number - another
    elif operation == "*":
        return number * another
    elif operation == "/":
        return number / another
    else:
        return "Not a valid number"
    
while playing:
    if operation == "exit":
        break
    print(f"Result: {calculator(a, b, operation)}")
    a = int(input("Choose a number:\n"))
    b = int(input("Choose another one:\n"))
    operation = input(
        "Choose an operation:\n    Options are: + , - , * or /.\n    Write 'exit' to finish.\n"
    )

# /YOUR CODE

# def calculator(number, another, operation):
#     if operation == "+":
#         return number + another
#     elif operation == "-":
#         return number - another
#     elif operation == "*":
#         return number * another
#     elif operation == "/":
#         return number / another
#     else:
#         return "Not a valid number"

# while True:
#     try:
#         number = int(input("Choose a number:\n"))
#         another = int(input("Choose another one:\n"))
#         operation = input("Choose an operation:\
#                         \n\tOptions are: +, -, * or /.\
#                         \n\tWrite 'exit to finish.\n")
#         if operation in ["exit", "Exit", "EXIT"]:
#             break
#         print(f"Result: {calculator(number, another, operation)}")
#     except Exception as e:
#         print(e)