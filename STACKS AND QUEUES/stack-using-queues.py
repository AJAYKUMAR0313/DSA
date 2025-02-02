from collections import deque

class Stack:
    def __init__(self):
        """Initialize stack with two queues"""
        self.q1 = deque()  # Main queue
        self.q2 = deque()  # Helper queue
    
    def push(self, x):
        """Push element x onto stack"""
        # Add new element to q1
        self.q1.append(x)
    
    def pop(self):
        """Remove and return the top element from stack"""
        if self.is_empty():
            raise IndexError("Stack is empty")
        
        # Move all elements except the last one to q2
        while len(self.q1) > 1:
            self.q2.append(self.q1.popleft())
        
        # Get the last element (top of stack)
        result = self.q1.popleft()
        
        # Swap q1 and q2
        self.q1, self.q2 = self.q2, self.q1
        
        return result
    
    def top(self):
        """Return the top element without removing it"""
        if self.is_empty():
            raise IndexError("Stack is empty")
        
        # Move all elements except the last one to q2
        while len(self.q1) > 1:
            self.q2.append(self.q1.popleft())
        
        # Get the last element
        result = self.q1[0]
        
        # Move the last element to q2
        self.q2.append(self.q1.popleft())
        
        # Swap q1 and q2
        self.q1, self.q2 = self.q2, self.q1
        
        return result
    
    def is_empty(self):
        """Check if the stack is empty"""
        return len(self.q1) == 0
    
    def size(self):
        """Return the number of elements in stack"""
        return len(self.q1)
    
    def __str__(self):
        """Return string representation of the stack"""
        if self.is_empty():
            return "Stack: []"
        return "Stack: " + str(list(self.q1))

# Alternative implementation using single queue
class StackSingleQueue:
    def __init__(self):
        """Initialize stack with a single queue"""
        self.q = deque()
    
    def push(self, x):
        """Push element x onto stack"""
        self.q.append(x)
        # Rotate the queue so the last element becomes first
        for _ in range(len(self.q) - 1):
            self.q.append(self.q.popleft())
    
    def pop(self):
        """Remove and return the top element"""
        if self.is_empty():
            raise IndexError("Stack is empty")
        return self.q.popleft()
    
    def top(self):
        """Return the top element"""
        if self.is_empty():
            raise IndexError("Stack is empty")
        return self.q[0]
    
    def is_empty(self):
        """Check if the stack is empty"""
        return len(self.q) == 0
    
    def size(self):
        """Return the number of elements"""
        return len(self.q)
    
    def __str__(self):
        """Return string representation of the stack"""
        if self.is_empty():
            return "Stack: []"
        return "Stack: " + str(list(self.q))
