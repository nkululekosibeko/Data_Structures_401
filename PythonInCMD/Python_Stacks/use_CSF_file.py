# import the class that will be used by the
from Data_Structures_401.PythonInCMD.Python_Stacks.customized_stack_functionality import Stack


def my_function():
    stack = Stack()
    stack.push(10)
    stack.push(43)
    stack.push(43)
    stack.push(43)
    stack.push(34)
    popped_element = stack.pop()
    print(popped_element)


if __name__ == "__main__":
    my_function()
