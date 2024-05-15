from queue import Empty

class ArrayStack:
    def __init__(self):
        self._data = []

    def __len__(self):
        return len(self._data)

    def is_empty(self):
        return len(self._data) == 0

    def push(self, a):
        self._data.append(a)

    def top(self):
        if self.is_empty():
            raise Empty('Stack is Empty')
        return self._data[-1]

    def pop(self):
        if self.is_empty():
            raise Empty('Stack is empty')
        return self._data.pop()

    def is_matched(expr):
        """Return True if all delimiters are properly match; False otherwise."""
        lefty = '({['  # opening delimiters
        righty = ')}]'  # respective closing delims
        S = ArrayStack()
        for c in expr:
            if c in lefty:
                S.push(c)  # push left delimiter on stack
            elif c in righty:
                if S.is_empty():
                    return False  # nothing to match with
                if righty.index(c) != lefty.index(S.pop()):
                    return False  # mismatched
        return S.is_empty()  # were all symbols matched?

    exp = "x+y -(3x5)}"
    print(is_matched(exp))