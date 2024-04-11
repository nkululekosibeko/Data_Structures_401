def find_sum(Arr, n):
    # Base case: if the length of the sequence is 0, return 0
    if n == 0:
        return 0
    # Recursive case: add the first element to the sum and recursively call find_sum on the rest of the sequence
    else:
        return Arr[n - 1] + find_sum(Arr, n - 1)

# Example usage:
sequence = [1, 2, 3, 4, 5]
length = len(sequence)
print("Sum of all elements:", find_sum(sequence, length))  # Output will be the sum of all elements in the sequence

"""
    The function find_sum takes two parameters: Arr, which is the sequence, and n, which is the length of the sequence.
    
    In the base case, if n is 0 (indicating an empty sequence), the function returns 0.
    
    In the recursive case, the function adds the last element of the sequence (Arr[n - 1]) to the sum of the rest of the sequence
    (computed by recursively calling find_sum with n - 1).
     
    This process continues until the base case is reached (when n becomes 0), at which point the sum is computed recursively by 
    adding each element of the sequence one by one.
    
    Finally, the function returns the total sum of all elements in the sequence.
"""