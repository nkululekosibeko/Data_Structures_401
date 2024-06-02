from Data_Structures_401.PythonInCMD.Python_Stacks.stacks_exam_revision.Empty import Empty


class ArrayQueue:
    DEFAULT_CAPACITY = 10
    """🤯 - Here i am defining a moderate capacity for all new Queues """

    def __init__(self):
        self._data = [None] * ArrayQueue.DEFAULT_CAPACITY
        self._size = 0
        self._front = 0

        """🤯 - Above i have just created an empty Queue """

    def __len__(self):
        return self._size

        """🤯 - Above i have just created a function that will return the number 
        of elements in the Queue """

    def is_empty(self):
        return self._size == 0

        """🤯 - Above i have just created a function that will check if the 
        Queue is empty or not and return 'True' if the Queue is Empty"""

    def first(self):
        if self.is_empty():
            raise Empty("Queue is empty")
        return self._data[self._front]

    """🤯 - Above i have just created a function that will  return the element
    that is at the front of the queue. It will also raise an exception when 
    it is found that the queue is empty."""

    def dequeue(self):
        if self.is_empty():
            raise Empty("Queue is empty")
        answer =  self._data[self._front]
        self._data[self._front] = None
        self._front = (self._front + 1) % len(self._data)
        self._size -= 1
        return answer

    """ 🤯 - Above i have just created a function that will remove and return the first 
    element from the queue. It will also raise an exception when the queue is empty.
    
    How it works ?.
    
    Line (37 - 38) Check if the Queue is empty.
    🤯 - The method first checks if the queue is empty by calling the 'is_empty()' method.
    🤯 - If the Queue is empty, it raises an 'Empty' exception, indicating that the are no elements to dequeue.
    
    Line (39) Retrieve and Remove the front element.
    🤯 - If the queue is not empty, it retrieves the front element from the Queue, which is located at the index 
        'self._front' int the internal array '_data'.
    🤯 - This element is stored in the variable 'answer'.
    
    Line (40) Clear the front position
    🤯 - The front position is then set to 'None'.
    🤯 - This step helps to avoid loitering, which is the retention of references to objects that are no longer needed,
            Potentially leading to memory leaks.
            
    Line (41) Update the front index.
    🤯 - The front index is is updated to the next position.
    🤯 - This is done using modular arithmetic to ensure that the front index wraps around to the beginning of the array
            if it reaches the end.
    🤯 - The expression '(Self._front + 1) % len(self._data) ensures that 'self._front' stays within the bounds of the
        array.
        
    Line (42) Decrease the size
    🤯 - The size of the queue is decremented by 1 to reflect the removal of an element.    
    """

    def enqueue(self, e):
        if self._size == len(self._data):
            self._resize(2 * len(self._data))
        avail = (self._front + self._size) % len(self._data)
        self._data[avail] = e
        self._size += 1

    """ 🤯 - Above I have created an enqueue function that is designed to add elements at to the rear (Back) of a 
            circular queue.
            
            How it Works in detail.
            
        Line (76 - 77) Check if the queue is full.
        🤯 - The method first if the queue is full by comparing the current size 'self._size' to the length of the 
                internal array 'len(self._data).
        🤯 - If the queue is full, it calls the '_resize' method to double the size of the internal array.
        🤯 - This ensures that there is always space available for the new element.
        
        Line (78) Calculate the available position.
        🤯 - The position where the new element will be added (avail) is calculated using the formula 
                '(self._front + self._size) % len(self._data)'.
        🤯 - This ensures that the new element is placed at the correct position, taking into account the circular 
                nature of the queue.
        🤯 - If the end of the array is reached, the position wraps around to the beginning.
        
        Line (79) Add the new element.
        🤯 - The new element e is placed at the calculated position (avail) in the internal array (_data).
        
        Line (80) Increase the size.
        🤯 - The size of the queue is incremented by 1 to reflect the addition of the new element.    
    """

    def _resize(self, cap):
        old = self._data
        self._data = [None] * cap
        walk = self._front
        for k in range(self._size):
            self._data[k] = old[walk]
            walk = (1 + walk) % len(old)
        self._front = 0

    """ Above I have created a resize method that resizes the internal array (list) used to store the elements of the 
        queue.
        
        Arguments and Local variables:
        🤯 - 'cap', The new capacity (size) for the resized array.
        🤯 - 'old', A temporary reference to the current array (before resizing)
        🤯 - 'walk', A variable used to track the current position in the old array while copying elements.
        
        Steps explained:
        🤯 - Store the old Array: 'old = self._data', Saves the current array to a temporary variable 'old'.
        🤯 - Create new array: 'Creates a new array with the specified capacity 'cap', initialized with 'None'.
        🤯 - Initialize walk variable: 'walk = self._front', Initializes the walk variable to the index of the 'front'
                elements currently in the queue 'self._size'.
        🤯 - Assign Elements: 'self._data[k] = old[walk]', copies each element from the old array to the new array.
        🤯 - Updates walk: 'Walk = (1 + cap) % len(old)', updates the walk variable to the next index, wrapping around
                to the beginning of the array if necessary (circular behaviour)
        🤯 - Reset front index: 'self._front = 0', Resets the front index to 0, since the elements are now stored 
                starting from the beginning of the array.    
    """

