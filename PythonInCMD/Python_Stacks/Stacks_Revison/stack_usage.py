from Data_Structures_401.PythonInCMD.Python_Stacks.Stacks_Revison.array_stack import ArrayStack

if __name__ == '__main__':
    my_stack = ArrayStack()
    my_stack.push(5)
    my_stack.push(10)
    my_stack.push(15)
    my_stack.push(30)
    print('The size of the stack is: ',len(my_stack))
    my_stack.pop()

