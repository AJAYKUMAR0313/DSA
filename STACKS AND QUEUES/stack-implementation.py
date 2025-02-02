class Stack:
    def __init__(self, capacity=10):
        """Initialize stack with given capacity (default 10)"""
        self.capacity = capacity
        self.array = [None] * capacity
        self.top = -1  # Stack is empty when top is -1
    
    def push(self, item):
        """Push an item onto the stack"""
        if self.is_full():
            # Double the capacity if stack is full
            self._resize(2 * self.capacity)
        
        self.top += 1
        self.array[self.top] = item
    
    def pop(self):
        """Remove and return the top item from the stack"""
        if self.is_empty():
            raise IndexError("Stack is empty")
        
        item = self.array[self.top]
        self.array[self.top] = None  # Clean up reference
        self.top -= 1
        
        # Shrink array if it's too sparse
        if self.size() < self.capacity // 4:
            self._resize(self.capacity // 2)
        
        return item
    
    def peek(self):
        """Return the top item without removing it"""
        if self.is_empty():
            raise IndexError("Stack is empty")
        return self.array[self.top]
    
    def is_empty(self):
        """Check if the stack is empty"""
        return self.top == -1
    
    def is_full(self):
        """Check if the stack is full"""
        return self.top == self.capacity - 1
    
    def size(self):
        """Return the number of items in the stack"""
        return self.top + 1
    
    def _resize(self, new_capacity):
        """Resize the underlying array to the new capacity"""
        new_array = [None] * new_capacity
        # Copy existing elements
        for i in range(self.size()):
            new_array[i] = self.array[i]
        self.array = new_array
        self.capacity = new_capacity

    def __str__(self):
        """Return string representation of the stack"""
        if self.is_empty():
            return "Stack: []"
        items = [str(self.array[i]) for i in range(self.top + 1)]
        return "Stack: [" + ", ".join(items) + "]"
