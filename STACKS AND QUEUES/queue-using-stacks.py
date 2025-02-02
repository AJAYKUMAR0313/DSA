class Queue:
    def __init__(self):
        """Initialize queue with two stacks"""
        self.stack1 = []  # For enqueue
        self.stack2 = []  # For dequeue
    
    def enqueue(self, x):
        """Add element x to the queue"""
        self.stack1.append(x)
    
    def dequeue(self):
        """Remove and return the front element from queue"""
        if self.is_empty():
            raise IndexError("Queue is empty")
        
        # If stack2 is empty, transfer all elements from stack1
        if not self.stack2:
            while self.stack1:
                self.stack2.append(self.stack1.pop())
        
        return self.stack2.pop()
    
    def peek(self):
        """Return the front element without removing it"""
        if self.is_empty():
            raise IndexError("Queue is empty")
        
        # If stack2 is empty, transfer all elements from stack1
        if not self.stack2:
            while self.stack1:
                self.stack2.append(self.stack1.pop())
        
        return self.stack2[-1]
    
    def is_empty(self):
        """Check if the queue is empty"""
        return len(self.stack1) == 0 and len(self.stack2) == 0
    
    def size(self):
        """Return the number of elements in queue"""
        return len(self.stack1) + len(self.stack2)
    
    def __str__(self):
        """Return string representation of the queue"""
        if self.is_empty():
            return "Queue: []"
        
        # Get all elements in queue order
        elements = []
        
        # First, add elements from stack2 (they're in correct order)
        elements.extend(reversed(self.stack2))
        
        # Then add elements from stack1 (they need to be reversed)
        elements.extend(self.stack1)
        
        return "Queue: " + str(elements)


# Alternative implementation with costly enqueue
class QueueCostlyEnqueue:
    def __init__(self):
        """Initialize queue with two stacks"""
        self.stack1 = []  # Main stack
        self.stack2 = []  # Helper stack
    
    def enqueue(self, x):
        """Add element x to the queue"""
        # Transfer all elements from stack1 to stack2
        while self.stack1:
            self.stack2.append(self.stack1.pop())
        
        # Add new element to stack1
        self.stack1.append(x)
        
        # Transfer all elements back to stack1
        while self.stack2:
            self.stack1.append(self.stack2.pop())
    
    def dequeue(self):
        """Remove and return the front element"""
        if self.is_empty():
            raise IndexError("Queue is empty")
        return self.stack1.pop()
    
    def peek(self):
        """Return the front element"""
        if self.is_empty():
            raise IndexError("Queue is empty")
        return self.stack1[-1]
    
    def is_empty(self):
        """Check if the queue is empty"""
        return len(self.stack1) == 0
    
    def size(self):
        """Return the number of elements"""
        return len(self.stack1)
    
    def __str__(self):
        """Return string representation of the queue"""
        if self.is_empty():
            return "Queue: []"
        return "Queue: " + str(list(reversed(self.stack1)))
