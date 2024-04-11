# Define a function to count occurrences of a target value in a dataset
def count(data, target):
    n = 0
    for item in data:
        if item == target:
            n += 1
    return n

# Example usage
def main():
    # Define a list of grades
    grades = ['A', 'B', 'A', 'C', 'A', 'A', 'B', 'C', 'A']

    # Call the count function to count occurrences of 'A' in grades
    # Here, 'grades' is the actual parameter passed as 'data', and 'A' is passed as 'target'
    count_of_A = count(grades, 'A')

    # Print the result
    print(f"The number of 'A's in grades is: {count_of_A}")

# Call the main function to run the example
main()
