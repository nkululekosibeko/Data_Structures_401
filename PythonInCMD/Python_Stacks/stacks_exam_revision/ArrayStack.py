from Data_Structures_401.PythonInCMD.Python_Stacks.stacks_exam_revision.Empty import Empty


class ArrayStack:
    def __init__(self):
        self._data = []

    def __len__(self):
        return len(self._data)

    def is_empty(self):
        return len(self._data) == 0

    def push(self, e):
        self._data.append(e)

    def top(self):

        if self.is_empty():
            raise Empty('Stack is empty')
        return self._data[-1]

    def pop(self):
        if self.is_empty():
            raise Empty('Stack is empty')
        return self._data.pop()

"""
    The code fragment below shows how a stack can be used to reverse a data sequence. 
    
    In this code fragment we print lines of a file in reverse order in order to display a data set in decreasing order 
    rather than increasing order.
    
     🤯 - This can be accomplished by reading each line and pushing it onto a stack, and then writing the lines in they 
            popped.    
"""

def reversed_file(filename):
    S = ArrayStack()
    original = open(filename)
    for line in original:
        S.push(line.rstrip('\n'))
    original.close()

    output = open(filename, 'w')
    while not S.is_empty():
        output.write(S.pop() + '\n')
    output.close()


"""
    We can also match Delimiters using stacks, this is how we do it.
    
    🤯 - We assume the input is a sequence of characters, such as '[(5 + X) - (Y + Z)]'.
    🤯 - We perform a left-to-right scan of the original sequence, using a stack S to facilitate the matching of 
            grouping symbols.
    🤯 - Each time we encounter an opening symbol, we push that symbol onto S, and each time we encounter a closing
            symbol, we pop a symbol from the stack (assuming S is not empty), and check that these two symbols for a 
            valid pair.
    🤯 - If we reach the end of the expression and the stack is empty, then the original expression was properly 
            matched.
    🤯 - Otherwise, the must be an opening delimiter on the stack without a matching symbol.
    
    If the length  of the original expression is n, the algorithm will make at most n calls to push and n calls to pop.
    These calls run in a total of O(n) time, even considering the amortized nature of the O(1) time bound for those 
    methods.
    
    Given that our selection of possible delimiters, "({[", has constant size, auxiliary tests such as e in lefty & 
    righty.index(c) each run in O(1) time. Combining these operations, the matching algorithm on a sequence of length
    n is O(n) time. 
"""

def is_matched(expr):
    lefty = '({['
    righty = ')}]'
    S = ArrayStack()

    for c in expr:
        if c in lefty:
            S.push(c)
        elif c in righty:
            if S.is_empty():
                return False
            if righty.index(c) != lefty.index(S.pop()):
                return False
            return S.is_empty()