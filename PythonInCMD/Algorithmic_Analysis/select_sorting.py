"""
    Selection sort is another simple comparison-based sorting algorithm. It works by dividing the input list
    into two parts: A sorted sublist and an unsorted sublist. Initially, the sorted sublist is empty, and the unsorted
    sublist contains all the elements of the input list. The algorithm repeatedly finds the minimum (or maximum)
    elements from the unsorted sublist and moves it to the end of the sorted sublist. This process is repeated until
    the entire the list is sorted.

    🤯 - Initialization: Start with the entire list as the unsorted sublist (inner loop) and an empty list
            (outer loop) as the sorted sublist.
    🤯 - Finding the minimum Element: Iterate through the unsorted sublist to find the minimum element.
    🤯 - Swapping: Swap the minimum element with the first element of the unsorted sublist. This effectively moves the
            minimum element to its correct position at the end of the sorted sublist.
    🤯 - Expanding the Sorted Sublist: Expand the sorted sublist by moving its end on position to the right.
    🤯 - Repeat: Steps 2 - 4 until the unsorted sublist becomes empty and the entire list becomes sorted.

    Selection Sort is not vey efficient compared to other sorting algorithms like merge sort or quicksort, especially of
    large datasets, Because it performs a lot of unnecessary swaps. However, it has the advantage of being simple to
    implement and easy to understand.
"""

def selection_sort_gbt(arr):
    n = len(arr)
    for i in range(n):
        min_index = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j

        arr[i], arr[min_index] = arr[min_index], arr[i]

arr = [64, 34, 25, 12, 22, 11, 90]
selection_sort_gbt(arr)

print("Sorted array: ")
for i in range(len(arr)):
    print("%d" % arr[i])

"""
    What is happening on this code  ?
    
    🤯 - Function Definition: The code begins with the definition of the selection_sort_gbt function, which takes an
            array 'arr' as input.
    🤯 - Initialization: Inside the function, the length of the array 'arr' is stored in the variable 'n'.
    🤯 - Outer Loop: It iterates over each element of the array, from index '0' to index 'n - 1'. This loop represents
            the process of expanding the sorted sublist by moving its end one position to the right.
    🤯 - Inner Loop: Within the outer loop, there is another loop (inner loop) that iterates over the unsorted part of
            the array, starting from index 'i + 1'. This loop searches for the minimum element in the unsorted part.
    🤯 - Minimum Element Search: Inside the inner loop, the algorithm compares the current element 'arr[j]' with the 
            assumed minimum element 'arr[min_index]'. If 'arr[j]' is smaller than arr[min_index], it updates min_index
            of 'arr[j]'.
    🤯 - Swap: After finding the minimum element in the unsorted part, the algorithm swaps it with the first element of 
            the unsorted part 'arr[i]'. This effectively moves the minimum element to its correct position in the sorted
            sublist.
"""

def my_selection_sort(elem):
    n = len(elem)

    for x in range(n):
        mid_index = x
        for y in range(x + 1, n):
            if elem[y] < elem[mid_index]:
                mid_index = y

        elem[x], elem[mid_index] = elem[mid_index], elem[x]

elem = [23, 34, -3, 45, 1, 5, 2, 5, 6, 8, 23, 45, 77, 4, -23, 22, 55]
print("My selection Sort Printout: ")
my_selection_sort(elem)
for q in range(len(elem)):
    print("%d" % elem[q])


def sorted(data):
    n = len(data)

    for x in range(n):
        middle = x
        for y in range(x + 1, n):
            if data[y] < data[middle]:
                middle = y

        data[x], data[middle] = data[middle], data[x]

data = [3, 1, -4, 5, 6, 9.0, 0]
sorted(data)
print("My sorted data")
for p in range(len(data)):
    print("%d" % data[p])

def least_selection_sort(arr):
    n = len(arr)

    for x in range(n):
        mid_index = x
        for y in range(x + 1, n):
            if arr[y] < arr[mid_index]:
                mid_index = y

        arr[x], arr[mid_index] = arr[mid_index], arr[x]

arr = [3, 5 , 1 ,-45 , 0, 6,3 ]
least_selection_sort(arr)
print("lest select printout")
for x in range(len(arr)):
    print("%d" % arr[x])


def selection_sort_one(arr):
    n = len(arr)

    for x in range(n):
        mid_index = x
        for y in range(x + 1, n):
            if arr[y] < arr[mid_index]:
                mid_index = y

        arr[x], arr[mid_index] = arr[mid_index], arr[x]

arr = [12, 4, 1, -4, 0, 13, 0]
selection_sort_one(arr)

print('Selection Sort Print-Out')
for x in range(len(arr)):
    print('%d' % arr[x])

def __selection_sort__(unsorted_list):
    n = len(unsorted_list)

    for x in range(n):
        middle_value = x
        for y in range(x + 1, n):
            if unsorted_list[y] < unsorted_list[middle_value]:
                middle_value = y

        unsorted_list[x], unsorted_list[middle_value] = unsorted_list[middle_value], unsorted_list[x]

unsorted_list = [23, -43, 2, -4, 98, 0.09, 0, 5 ]
__selection_sort__(unsorted_list)
print("__selection_sort__ print out: ")
for x in range(len(unsorted_list)):
    print("%d" % unsorted_list[x])

def __selection_sort_two__(unsorted):
    n = len(unsorted)

    for x in range(n):
        middle_v = x
        for y in range(x + 1, n):
            if middle_v[y] < middle_v[middle_v]:
                middle_v = y

        unsorted[x], unsorted_list[middle_v] = unsorted[middle_v], unsorted[x]

unsorted = [4, -3, 9, 0, 8, -3, 1, 4, 3]
__selection_sort_two__(unsorted)
print("__selection_sort_two__ print out")
for a in range(len(unsorted)):
    print("%d" % unsorted[a])
