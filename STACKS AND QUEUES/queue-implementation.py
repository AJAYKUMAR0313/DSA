class Queue:
    def __init__(self, capacity=10):
        """Initialize queue with given capacity (default 10)"""
        self.capacity = capacity
        self.array = [None] * capacity
        self.front = 0  # Index for dequeuing
        self.rear = -1  # Index for enqueuing
        self.size = 0   # Current number of elements
    
    def enqueue(self, item):
        """Add an item to the rear of the queue"""
        if self.is_full():
            self._resize(2 * self.capacity)
        
        # Use modulo to wrap around to the beginning if necessary
        self.rear = (self.rear + 1) % self.capacity
        self.array[self.rear] = item
        self.size += 1
    
    def dequeue(self):
        """Remove and return the front item from the queue"""
        if self.is_empty():
            raise IndexError("Queue is empty")
        
        item = self.array[self.front]
        self.array[self.front] = None  # Clean up reference
        self.front = (self.front + 1) % self.capacity
        self.size -= 1
        
        # Shrink array if it's too sparse
        if 0 < self.size < self.capacity // 4:
            self._resize(self.capacity // 2)
            
        return item
    
    def peek(self):
        """Return the front item without removing it"""
        if self.is_empty():
            raise IndexError("Queue is empty")
        return self.array[self.front]
    
    def is_empty(self):
        """Check if the queue is empty"""
        return self.size == 0
    
    def is_full(self):
        """Check if the queue is full"""
        return self.size == self.capacity
    
    def get_size(self):
        """Return the number of items in the queue"""
        return self.size
    
    def _resize(self, new_capacity):
        """Resize the underlying array to the new capacity"""
        new_array = [None] * new_capacity
        
        # Copy existing elements to new array, starting from index 0
        for i in range(self.size):
            new_array[i] = self.array[(self.front + i) % self.capacity]
        
        self.array = new_array
        self.capacity = new_capacity
        self.front = 0
        self.rear = self.size - 1 if self.size > 0 else -1

    def __str__(self):
        """Return string representation of the queue"""
        if self.is_empty():
            return "Queue: []"
        
        items = []
        for i in range(self.size):
            items.append(str(self.array[(self.front + i) % self.capacity]))
        
        return "Queue: [" + ", ".join(items) + "]"
