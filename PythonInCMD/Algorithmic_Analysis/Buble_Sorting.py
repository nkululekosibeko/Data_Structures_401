"""
    Buble sorting is a simple sorting algorithm that repeatedly steps through the list,
     compares adjacent elements, and swaps them if they are in the wrong order.
    The pass through the list is repeated until the list is sorted.

    🤯 - Start with the first element (index 0) and compares it with the next element (index 1).
    🤯 - If the first element is greater than the second element, swap them.
    🤯 - Move to the next pair of elements and repeat the comparison and swap process
            until you reach the end of the list.
    🤯 - After the first pass, the largest element will be at the end of the list.
    🤯 - Repeat step (1 - 4) for the remaining elements, excluding the last element in each pass
            (Since it's already in its correct position).
"""
def __buble_Sort__(my_array):
    n = len(my_array)

    for x in range(n):
        for y in range(0, n-x-1):
            if my_array[y] > my_array[y + 1]:
                my_array[y], my_array[y + 1] = my_array[y + 1], my_array[y]

my_array = [3, 1, -7, 8, -9, 0, 0 ,23]
__buble_Sort__(my_array)
print("__buble_sort__ sorted list Printout")
for x in range(len(my_array)):
    print("%d" % my_array[x])


def buble_sort_gbt(arr):
    n = len(arr)

    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

arr = [64, 34, 25, 12, 22, 11, 90]
buble_sort_gbt(arr)

print("Sorted array: ")
for i in range(len(arr)):
    print("%d" % arr[i])


'''
    The time complexity of this algorithm is (Big-Oh of) O(n^2).
    
        Outer Loop: It runs n times, where n is the number of elements in the array. This gives us 
                    O(n) complexity for the outer loop.
        Inner Loop: Also runs n times in the worst case scenario, for each iteration of the outer loop.
                    However, as the outer loop progresses, the number of iterations in the inner loop decrease
                    by one (n - 1). This gives us an average of approximately n/2 iterations for the inner loop.
                    In Big-O notation, we drop the constant factor, so we still have O(n) complexity for the inner loop.
        Total Comlexity: Since the inner loop is nested within the outer loop, the total time complexity is 
                        O(n) * O(n) = O(n^2)
'''

'''
    As you can see the results are printed in Ascending Order, This is due to the > sign in the if-statement 
        that compares whether the value at index j is greater than the element at index j + 1. Hence performing the 
        swap of the two adjacent elements. 
        
     for j in range(0, n-i-1) : The inner loop iterates from index 0 to n-i-1, where n is the number of elements in 
                                the array and i is the current iteration of the outer loop.
                                The reason for for the range n-i-1 is that after each pass through the array, the 
                                largest element is bubbled up to its correct position position at the end of the array.
                                Therefore, in each subsequent pass, we can ignore the last elements because they are
                                already in their correct positions.                         
'''


def buble_sort(elements):
    n = len(elements)

    for x in range(n):
        for y in range(0, n-x-1):
            if elements[y] > elements[y + 1]:
                elements[y], elements[y + 1] = elements[y + 1], elements[y]


elements = [34,5,7,23,-89, 34,3,44,0,98,-300]
buble_sort(elements)

print("My sorted array")
for t in range(len(arr)):
    print("%d" % elements[t])

def regular_buble_sort(n):
    n = len(arr)

    for x in range(n):
        for y in range(0, n-x-1):
            if arr[y] > arr[y + 1]:
                arr[y], arr[y + 1] = arr[y + 1], arr[y]

arr = [9, -9, 3, 4.0, 2.989, 0, 44]
regular_buble_sort(arr)
print("Regular Buble Sort")
for x in range(len(arr)):
    print("%d" % arr[x])

'''
    Optimized buble sort, is a variation of the traditional buble sort algorithm that includes an optimization to reduce
    the number of unnecessary comparisons and swaps. The optimization involves introducing a flag to track whether any 
    swaps were made during a pass through the array. If no swaps are made during the swap, it indicates that the array 
    is already sorted, and the algorithm can terminate early.
    
    🤯 - initialize a boolean flag variable to indicate whether a swap has been made during a pass through the array.
            Initially set the flag to true.
    🤯 - Start with the outer loop, which iterates over each element  in the array.
    🤯 - Within the outer loop, start the inner loop, which iterates over the unsorted portion of the array.
    🤯 - Compare adjacent elements in the inner loop and swap them if they are in the wrong order.
    🤯 - If a swap is made during the inner loop, set the flag true, indicating that the array is not yet fully sorted.
    🤯 - After completing the inner loop, check the flag. If the flag is still true, it means at least on swap was made
            during the pass, indicating that the array may not be fully sorted yet. Repeat the process.
    🤯 - If the flag is false after completing the inner loop, it means no swaps were made during the pass, indicating
            that the array is already sorted. In this case, terminate the algorithm early.
            
    By introducing the flag and checking it after each pass through the array, the optimized buble sort avoids
    unnecessary iterations when the array is sorted or nearly sorted. This results in improved performance, especially
    for partially sorted datasets.
    
'''

def optimized_buble_sort_gbt(arr):
    n = len(arr)
    swapped = True

    while swapped:
        swapped = False
        for i in range(1, n):
            if arr[i - 1] > arr[i]:
                arr[i - 1], arr[i] = arr[i], arr[i - 1]
                swapped = True
        n -= 1

arr = [64, 34, 25, 12, 22, 11, 90]
optimized_buble_sort_gbt(arr)
print("Sorted array: ")
for i in range(len(arr)):
    print("%d" % arr[i])

"""
    What is happening inside the code.
    🤯 - Function Definition: The code starts with the definition of the  optimized_buble_sort_gbt function, which takes
            an arr as input.
    🤯 - Initialization: Inside the definition, n is initialized to the length of the array arr, and swapped is set to 
            True to indicate that at least one swap has occurred.
    🤯 - Main Loop: The algorithm enters a while loop, which continues until no swaps are made during a pass through 
            the array. This loop ensures that the sorting process continues until the array is fully sorted.
    🤯 - Reset Flag: At the beginning of each pass through the array, the swapped flag is reset to False. This will be
            reset to True is any swaps occur during the pass.
    🤯 - Inner Loop: Within the while loop, there is a for loop that iterates over the array starting from the second
            element (i starts from 1). This loop compares adjacent elements and swaps them if they are in the wrong 
            order.
    🤯 - Swap and Flag Update: If a swap is made during the iteration, the swapped flag is set to True to indicate that 
            the array is not yet fully sorted.
    🤯 - Outer Loop Adjustment: After completing the inner loop, the variable n is decremented by one. This reduces the
            range of the inner loop for the next pass through the array, as the grater element is already placed at the
            end of the array.
"""

def __optimized_buble_sort__(myArray):
    n = len(myArray)
    changed = True

    while changed:
        changed = False
        for x in range(1, n):
            if myArray[x - 1] > myArray[x]:
                myArray[x - 1], myArray[x] = myArray[x], myArray[x - 1]
                changed = True
        n -= 1

myArray = [0, -9, 99, 34, 87, -234, 65]
__optimized_buble_sort__(myArray)
print("__optimized_buble_sort__ Printout")
for t in range(len(myArray)):
    print("%d" % myArray[t])

def optimized_bubble_Sort(elem):
    n = len(elem)
    swapped = True

    while swapped:
        swapped = False
        for a in range(1, n):
            if elem[a - 1] > elem[a]:
                elem[a - 1], elem[a] = elem[a], elem[a - 1]
                swapped = True
        n -= 1

elem = [13, 4, 5, 56, -78, 65, -8, 23, 56, 57]
optimized_bubble_Sort(elem)
print("Optimized loop Print Out")
for t in range(len(elem)):
    print("%d" % elem[t])

def my_optimised_buble_sort(data):
    n = len(data)
    swapped = True

    while swapped:
        swapped = False
        for b in range(1, n):
            if data[b - 1] > data[b]:
                data[b - 1], data[b] = data[b], data[b - 1]
                swapped = True
        n -= 1

data = [1, -3, 45, 56, -65, 44, 642, -100, 89]
my_optimised_buble_sort(data)
print("My buble sort Printout")
for z in range(len(data)):
    print("%d" % data[z])


def pro_optimized_buble_sort(arr):
    n =  len(arr)
    swapped = True

    while swapped:
        swapped = False
        for x in range(1, n):
            if arr[x - 1] > arr[x]:
                arr[x - 1], arr[x] = arr[x], arr[x - 1]
                swapped = True

        n -= 1

arr = [2, 4, 1, 4, 2, -4.4, 0.0, 1]
pro_optimized_buble_sort(arr)
print('Pro Optimized Buble Sort Print-Out')
for x in range(len(arr)):
    print("%d" % arr[x])