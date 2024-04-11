def Add_matrix(A):
    total_sum = 0;
    for row in A:
        for element in row:
            total_sum += element
    return total_sum

""" SO in this loop we first define the function 'Add_matrix' and put an argument 'A' into it.
    THe second thing we do, we initialise our identifier 'total_sum'to '0' as its starting value
    
    Them we create a for loop that is goiung to iterate through the wto dimesional array & 
    inside that loop we create another for loop that is goinmg to iterate inside all the elements of both arrays
    as well as add them to the 'total_sum' per iteration.

    Lastly at the end we return the total_sum that will have all the values it was adding in each iteration as a 
    result.
"""

examplar_loop = [[1,2,3,4,5],
                 [6,7,8,9,10],
                 [11,12,13,14,15]]

print(Add_matrix(examplar_loop))