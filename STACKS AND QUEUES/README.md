Stack using queue
I'll help you implement a Stack using two Queues. We'll implement all standard stack operations while maintaining LIFO (Last In First Out) behavior using FIFO (First In First Out) queues.

```python
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

```

I've provided two implementations:

1. Two-Queue Implementation:

   - Uses two queues (q1 and q2)
   - `push`: O(1) - simply add to q1
   - `pop`: O(n) - transfer n-1 elements to q2, then get last element
   - Space complexity: O(n)

2. Single-Queue Implementation:
   - Uses only one queue
   - `push`: O(n) - add element and rotate queue
   - `pop`: O(1) - simply remove from front
   - Space complexity: O(n)

Here's how to use either implementation:

```python
# Using two-queue implementation
stack = Stack()

# Or using single-queue implementation
# stack = StackSingleQueue()

stack.push(1)
stack.push(2)
stack.push(3)

print(stack)        # Stack: [3, 2, 1]
print(stack.pop())  # 3
print(stack.top())  # 2
print(stack.size()) # 2
```

Key differences between the implementations:

1. Two-queue approach has O(1) push but O(n) pop
2. Single-queue approach has O(n) push but O(1) pop
3. Single-queue uses less space but requires rotation during push

I'll walk through how the Stack works using the two-queue implementation with a visual example.

Let's use the Two-Queue Stack and perform some operations:

1. Initial State:

```
q1: []
q2: []
```

2. Let's push(1):

```
q1: [1]
q2: []
```

3. Push(2):

```
q1: [1, 2]
q2: []
```

4. Push(3):

```
q1: [1, 2, 3]
q2: []
```

5. Now let's see what happens during pop():
   - First, move all elements except the last one to q2

```
Step 1:
q1: [3]         # Only last element remains
q2: [1, 2]      # Moved first n-1 elements here

Step 2: Remove and save last element from q1
result = 3
q1: []
q2: [1, 2]

Step 3: Swap q1 and q2
q1: [1, 2]      # This becomes our main queue again
q2: []          # Empty helper queue
```

6. If we push(4) now:

```
q1: [1, 2, 4]
q2: []
```

Let's try the single-queue implementation to see the difference:

1. Initial empty state:

```
q: []
```

2. Push(1):

```
q: [1]    # No rotation needed for first element
```

3. Push(2):

```
Step 1: Add 2
q: [1, 2]

Step 2: Rotate once
q: [2, 1]    # Now 2 is at front (top of stack)
```

4. Push(3):

```
Step 1: Add 3
q: [2, 1, 3]

Step 2: Rotate twice
First rotation:  [1, 3, 2]
Second rotation: [3, 2, 1]   # Now 3 is at front (top of stack)
```

5. Pop():

```
Simply remove from front
q: [2, 1]    # 3 is removed and returned
```

The key thing to notice:

- In two-queue implementation: We move elements during pop()
- In single-queue implementation: We rotate elements during push()

Both achieve the same LIFO (Last In First Out) behavior of a stack, just with different trade-offs in when they do the work.

QUEUE USING STACK
I'll help you implement a Queue using two Stacks. We'll implement all standard queue operations while maintaining FIFO (First In First Out) behavior using LIFO (Last In First Out) stacks.

```python
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

```

Let me show you how these implementations work with examples:

1. First Implementation (Costly Dequeue):

```python
queue = Queue()

# Initial state
print(queue)  # Queue: []

# Enqueue operations (just push to stack1)
queue.enqueue(1)    # stack1: [1],    stack2: []
queue.enqueue(2)    # stack1: [1,2],  stack2: []
queue.enqueue(3)    # stack1: [1,2,3],stack2: []

print(queue)  # Queue: [1, 2, 3]

# First dequeue operation
# Transfers all elements to stack2
result = queue.dequeue()  # stack1: [], stack2: [3,2]
print(result)  # 1

# Next dequeue uses stack2 directly
result = queue.dequeue()  # stack1: [], stack2: [3]
print(result)  # 2
```

2. Second Implementation (Costly Enqueue):

```python
queue = QueueCostlyEnqueue()

# Enqueue 1:
# 1. Empty both stacks
# 2. Put 1 in stack1
queue.enqueue(1)    # stack1: [1]

# Enqueue 2:
# 1. Move 1 to stack2: stack1:[], stack2:[1]
# 2. Put 2 in stack1: stack1:[2], stack2:[1]
# 3. Move 1 back: stack1:[1,2]
queue.enqueue(2)    # stack1: [1,2]

queue.enqueue(3)    # stack1: [1,2,3]

print(queue)        # Queue: [1, 2, 3]
print(queue.dequeue())  # 1
print(queue.peek())     # 2
```

Key differences between the implementations:

1. First implementation (Queue):

   - O(1) enqueue
   - Amortized O(1) dequeue
   - Elements might be split between two stacks

2. Second implementation (QueueCostlyEnqueue):
   - O(n) enqueue
   - O(1) dequeue
   - All elements always in order in one stack

The first implementation is generally more efficient in practice because:

1. It spreads out the cost of moving elements
2. Each element is moved at most twice (once to stack2 and once back)
3. Provides amortized O(1) time complexity for both operations

QUEUE COSTLY DEQUEUE

I'll walk through how the Queue works using the two-stack implementation with a visual example.

Let's use the first implementation (Queue with costly dequeue) and perform operations:

1. Initial State:

```
stack1: []    (for enqueue)
stack2: []    (for dequeue)
```

2. enqueue(1):

```
stack1: [1]   <- new elements go here
stack2: []
```

3. enqueue(2):

```
stack1: [1, 2]   <- top of stack1
stack2: []
```

4. enqueue(3):

```
stack1: [1, 2, 3]   <- top of stack1
stack2: []
```

5. Now let's dequeue() (want to remove 1):

```
Step 1: stack2 is empty, so transfer all elements from stack1 to stack2
Transfer 3: stack1: [1, 2],    stack2: [3]
Transfer 2: stack1: [1],       stack2: [3, 2]
Transfer 1: stack1: [],        stack2: [3, 2, 1]   <- top of stack2

Step 2: Pop from stack2
stack1: []
stack2: [3, 2]    <- 1 is removed and returned
```

6. Another dequeue() (want to remove 2):

```
stack2 is not empty, so directly pop from stack2
stack1: []
stack2: [3]       <- 2 is removed and returned
```

7. Let's enqueue(4):

```
stack1: [4]       <- new elements still go to stack1
stack2: [3]
```

8. One more dequeue() (want to remove 3):

```
stack2 still has elements, so pop from stack2
stack1: [4]
stack2: []        <- 3 is removed and returned
```

9. Final dequeue() (want to remove 4):

```
Step 1: stack2 is empty, transfer from stack1
stack1: []
stack2: [4]

Step 2: Pop from stack2
stack1: []
stack2: []        <- 4 is removed and returned
```

The key points to notice:

1. New elements always go to stack1
2. We only transfer elements to stack2 when:
   - We need to dequeue
   - stack2 is empty
3. Once elements are in stack2, we use them all up before transferring more
4. The transfer process reverses the order:
   - stack1: [1,2,3] (3 at top)
   - After transfer, stack2: [3,2,1] (1 at top)
   - This reversal is what converts LIFO to FIFO!

Think of it like a line of people:

- New people join the back of line (stack1)
- When we need to serve people, we make them all turn around (transfer to stack2)
- Now we can serve them in the correct order!

QueueCostlyEnqueue

I'll walk through how QueueCostlyEnqueue works with a visual example. This version makes enqueue operations costly but keeps dequeue simple.

Let's go through each operation:

1. Initial State:

```
stack1: []    (main stack)
stack2: []    (helper stack)
```

2. enqueue(1):

```
Step 1: stack1 is empty, so just add 1
stack1: [1]
stack2: []
```

3. enqueue(2):

```
Step 1: Move everything to stack2
stack1: []
stack2: [1]

Step 2: Add new element to stack1
stack1: [2]
stack2: [1]

Step 3: Move everything back to stack1
stack1: [1, 2]    <- 1 is at top (front of queue)
stack2: []
```

4. enqueue(3):

```
Step 1: Move everything to stack2
stack1: []
stack2: [2, 1]

Step 2: Add new element to stack1
stack1: [3]
stack2: [2, 1]

Step 3: Move everything back to stack1
stack1: [1, 2, 3]    <- 1 is at top (front of queue)
stack2: []
```

5. dequeue() (want to remove 1):

```
Simply pop from stack1
stack1: [2, 3]    <- returns 1
stack2: []
```

6. enqueue(4):

```
Step 1: Move everything to stack2
stack1: []
stack2: [3, 2]

Step 2: Add new element to stack1
stack1: [4]
stack2: [3, 2]

Step 3: Move everything back to stack1
stack1: [2, 3, 4]    <- 2 is at top (front of queue)
stack2: []
```

The key points about this implementation:

1. stack1 always maintains queue order (front element at top)
2. Every enqueue requires moving all existing elements twice
3. dequeue is simple - just pop from stack1
4. We only use stack2 during enqueue operations

Think of it like a stack of books:

- To add a new book at the bottom (enqueue)
  - Move all books to a temporary stack (stack2)
  - Put the new book down
  - Move all books back
- To remove a book (dequeue)
  - Simply take the top book

This implementation is less efficient than the first one because:

- Each enqueue operation is O(n)
- We move elements more times than necessary
- Better suited when dequeues are more frequent than enqueues

Would you like me to explain anything else about this implementation?
