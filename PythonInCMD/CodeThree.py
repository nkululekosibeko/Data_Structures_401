def printMax(arr):
    max_value = float('-inf')
    max_row = 0
    max_col = 0
    
    for i, row in enumarate(arr):
        for j, val in enumarate(row):
            if val > max_value:
                max_value = val
                max_row = i
                max_col = j
                
    print("Maximum value: ", max_value)
    print("Row: ", max_row)
    print("Column: ", max_col)


    array = [[1,2,3],
             [4,5,6],
             [7,8,9]]

    printMax(array)


    """
        max_value = float('-inf')
        
        First we start by initializing 'max_value' to negative infinity.
        Initializing max_value to float('-inf') ensures that any integer value encountered 
        in the array will be greater than max_value, regardless of its actual value.
        This ensures correctness and robustness of the algorithm across different input scenarios.
         
        max_row = 0 & max_col = 0
        
        Initializing max_row and max_col to None is a common practice in Python when you don't yet have a 
        valid value to assign to these variables, but you still want to declare them before using them.
        
        In the loops
        
        for i, row in enumarate(arr):
        This loop iterate trough each row in the 2D array 'arr'.
        The 'enumerator(arr)' will return both the index 'i' and the corresponding row 'row' of the array 'arr'
        inside this loop 'i' represents the row index and 'row' represents the actual row (A list of elemnts) from the array.
        
        for j, val in enumarate(row):
        This loop iterate through each element 'val' in the current row 'row'
        enumarate(row) returns both the index 'j' and the corresponding value 'val' of each element in the row 'row'.
        inside this loop, 'j' represent the column index, and 'val' represents the actual value of the element in the array.
        
            Condition         
            if val > max_value:
                max_value = val
                max_row = i
                max_col = j
            
            This condition checks if the current element 'val' is grater than the current maximum value 'max_value'
            if 'val' is greater than 'max_value', it updates 'max_value' to 'val' and updates 'max_row' & 'max_col' to the current row index 'i' 
                column index 'j', respectively.
        
         """