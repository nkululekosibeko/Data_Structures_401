def main():
    # Prompt the user to enter their age in years
    age = int(input('Enter your age in years: '))

    # Calculate the maximum heart rate
    max_heart_rate = 206.9 - (0.67 * age)

    # Calculate the target fat-burning heart rate
    target = 0.65 * max_heart_rate

    # Print the target fat-burning heart rate
    print('Your target fat-burning heart rate is:', target)


# Call the main function to execute the program
if __name__ == "__main__":
    main()
