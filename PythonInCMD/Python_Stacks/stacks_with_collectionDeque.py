from collections import deque  # To use this class make sure you import it.

def main():
    stack = deque()
    stack.append(33)
    stack.append(45)
    stack.append(23)

    popped = stack.pop()
    print(popped)

"""
    The collection.deque class in python provides an efficient way to implement a stack. It supports both append and pop
    operations. It also runs on the time complexity of Big-O 'O(1)'.
    
    The code description is as from the using_list.py    
"""