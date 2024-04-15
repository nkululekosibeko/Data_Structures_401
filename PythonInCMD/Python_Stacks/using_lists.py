"""
    In Python, a stack is a linear data structure that follows the LIFO principle, meaning that the most recently
    added element is the first element to be removed.
    Python doesn't have a built-in stack data structure, but you can implement on using lists.

    Check out the following example below:
"""

def main():
    stack = []

    stack.append(18)
    stack.append(11)
    stack.append(30)

    popped_element = stack.pop()
    print(popped_element)

if __name__ == "__main__":
    main()

"""
    🤯 - Function definition: The program begins by defining a function name 'main()' that has no parameters.
    🤯 - 'Stack = []': This line initializes an empty list named stack. In this context, the list represents a stack 
            data structure where elements can be added to or removed from the top of the stack. 
    🤯 - stack.append(18): These lines of code they add elements to the top of the stack using the 'append()' method. 
    🤯 - popped_element = stack.pop(): This line of code creates a variable 'popped_element' and assigns it to the
            popped element from the 'stack' list.
    🤯 - print(popped_element): Prints the popped element from the 'stack'.
"""
