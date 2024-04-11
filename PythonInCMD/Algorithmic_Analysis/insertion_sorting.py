"""
    Insertion Sort is another comparison based sorting algorithm.
    It works by dividing the input list into two parts: a sorted sublist and an unsorted sublist. Initially, the sorted
     sublist contains only the first element of the input list, and the unsorted sublist contains the remaining
      elements. The algorithm repeatedly takes the first element from the unsorted sublist and inserts it into its
      correct position in the sorted sublist. This process is repeated until the entire list is sorted.

      Here's how it Works:

    🤯 - Initialization: Start with the first element of the list as the sorted sublist and the remaining elements as
            the unsorted sublist.
    🤯 - Iterative Insertion: Iterate through the elements of the unsorted sublist one by one.
    🤯 - Insertion into Sorted Sublist: For each element in the unsorted sublist, compare it with the elements in the
            sorted sublist from right to left. Find the correct position for the current element in the sorted sublist
            by shifting larger elements to the right.
    🤯 - Expansion of the Sorted Sublist: After finding the correct position for the current element, insert it into the
            sorted sublist at that position.
    🤯 - Repeat: Steps 2 - 4 until all elements in the unsorted sublist have been inserted into their correct positions
            in the sorted sublist.

    Insertion Sort is efficient for small datasets or nearly sorted arrays because it performs well when the input list
    already partially sorted. However, it becomes less efficient for larger datasets compared to more advanced sorting
    algorithms like merge sort or quicksort.
"""

def insertion_sort_gbt(arr):

    for i in range(1, len(arr)):    # Deals with the unsorted list.
        key = arr[i]                # Assigned to the current element to be inserted in the sorted array.
        j = i - 1                   # A pointer that points to the last element of the sorted list.

        while j >= 0 and key < arr[j]:      # Deals with the sorted sublist.
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

arr = [64, 34, 25, 12, 22, 11, 90]
insertion_sort_gbt(arr)

print("Insertion Sorted List Printout ")
for i in range(len(arr)):
    print("%d" % arr[i])

"""
    What exactly is happening here? Here is the explanation with the code below.
    
    🤯 - Function Definition: The code begins with the definition of the insertion_sort function, which takes and array
            'arr' as input.
    🤯 - Outer Loop: The outer loop iterates over each element of the array, starting from the second element '(i = 1)'
            , this loop represents the process of iterating through the unsorted sublist.
    🤯 - Key Element Selection: Inside the outer loop, the current element to be inserted into the sorted sublist is 
            stored in the variable key.
    🤯 - Pointer Initialization: The variable j is initialized to 'i - 1', which points to the last element of the
            sorted sublist.
    🤯 - Inner Loop (shifting): The algorithm enters a while loop that iterates as long as 'J' is >= 0 (ensuring that 
            we don't go out of bounds) and the key is less than the element at position arr[j] (indicating that the 
            current element needs to be shifted to the right). Inside this loop, elements of the sorted sublist that 
            are greater than the key are shifted on position to the right.
    🤯 - Insertion: Once the correct position for the key element is found (either because 'j' reached -1 or key is not
            less than arr[j]), the key is inserted into its correct position in the sorted sublist at index 'j + 1'
"""