"""
    🤯- def main(): This line defines a function named main.

    🤯- stack = []: This line initializes an empty list named stack. In this context, the list represents a stack data
            structure where elements can be added to or removed from the top.

    🤯- stack.append(18), stack.append(11), stack.append(30): These lines add elements to the stack using the append()
            method. Each element is added to the top of the stack.

    🤯- popped_element = stack.pop(): This line removes and returns the top element from the stack using the pop()
            method. The removed element is assigned to the variable popped_element.

    🤯- if __name__ == "__main__":: This line checks if the script is being run directly (as opposed to being imported
            as a module into another script). If it's being run directly, the main() function is called.

    🤯- main(): This line calls the main() function, which contains the code to manipulate the stack.

"""

class Stack:
    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        if not self.is_empty():
            return self.stack.pop()
        else:
            raise IndexError('I can\'t Pop from an empty stack')

    def is_empty(self):
        return len(self.stack) == 0

    def peek(self):
        if not self.is_empty():
            return self.stack[-1]
        else:
            return None

    def size(self):
        return len(self)