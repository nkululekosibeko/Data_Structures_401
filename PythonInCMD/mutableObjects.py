# Define a function to scale all entries of a numeric dataset by a given factor
def scale(data, factor):
    for j in range(len(data)):
        data[j] = data[j] * factor

# Example usage
def main():
    # Define a list of numbers
    numbers = [1, 2, 3, 4, 5]

    # Call the scale function to scale the numbers by a factor of 2
    scale(numbers, 2)

    # Print the scaled numbers
    print("Scaled numbers:", numbers)

# Call the main function to run the example
main()
