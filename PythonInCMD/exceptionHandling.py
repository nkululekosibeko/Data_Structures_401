# age = -1  # an initially invalid choice
# while age <= 0:
#     try:
#         age = int(input("Enter your age in years: "))
#         if age <= 0:
#             print("Your age must be positive")
#     except (ValueError, EOFError):
#         print("Invalid response")

apples = -1  # initially, an invalid choice

# Keep prompting the user until they enter a valid positive integer
while apples <= 0:
    try:
        apples = int(input("Enter the number of apples you have: "))
        if apples <= 0:
            print("You must have at least one apple!")
    except (ValueError, EOFError):
        print("Invalid response. Please enter a valid positive integer.")
