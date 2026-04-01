# =========================================
# PART 1: Queue using Array
# =========================================

# -------- TASK 1 --------
# Implement ArrayQueue Class Structure

class ArrayQueue:
    def __init__(self, capacity=10):
        self.queue = [None] * capacity   # private array
        self.front = 0
        self.rear = -1
        self.count = 0
        self.capacity = capacity
        print(f"Created new Queue with capacity: {capacity}")
        print("Queue is empty:", self.is_empty())


# -------- TASK 2 --------
# Implement Array Queue Operations

    def is_empty(self):
        return self.count == 0

    def enqueue(self, element):
        if self.count == self.capacity:
            print("Queue Overflow")
            return
        self.rear = (self.rear + 1) % self.capacity
        self.queue[self.rear] = element
        self.count += 1
        print(f"Enqueued {element} to the queue")

    def dequeue(self):
        if self.is_empty():
            print("Queue Underflow")
            return
        element = self.queue[self.front]
        self.front = (self.front + 1) % self.capacity
        self.count -= 1
        print(f"Dequeued element: {element}")
        return element

    def peek(self):
        if self.is_empty():
            print("Queue is empty")
            return
        print("Front element:", self.queue[self.front])

    def size(self):
        print("Queue size:", self.count)

    def display(self):
        if self.is_empty():
            print("Queue is empty")
            return
        result = []
        for i in range(self.count):
            result.append(self.queue[(self.front + i) % self.capacity])
        print("Display queue:", result)


# =========================================
# PART 2: Queue using Linked List
# =========================================

# -------- TASK 3 --------
# Implement Node and LinkedQueue Structure

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedQueue:
    def __init__(self):
        self.front = None
        self.rear = None
        self.count = 0
        print("Created new LinkedQueue")
        print("Queue is empty:", self.is_empty())


# -------- TASK 4 --------
# Implement Linked List Queue Operations

    def is_empty(self):
        return self.front is None

    def enqueue(self, element):
        new_node = Node(element)
        if self.rear is None:
            self.front = self.rear = new_node
        else:
            self.rear.next = new_node
            self.rear = new_node
        self.count += 1
        print(f"Enqueued {element} to the queue")

    def dequeue(self):
        if self.is_empty():
            print("Queue Underflow")
            return
        temp = self.front
        self.front = self.front.next
        if self.front is None:
            self.rear = None
        self.count -= 1
        print(f"Dequeued element: {temp.data}")
        return temp.data

    def peek(self):
        if self.is_empty():
            print("Queue is empty")
            return
        print("Front element:", self.front.data)

    def size(self):
        print("Queue size:", self.count)

    def display(self):
        if self.is_empty():
            print("Queue is empty")
            return
        current = self.front
        result = ""
        while current:
            result += str(current.data) + " -> "
            current = current.next
        result += "null"
        print("Current queue:", result)


# =========================================
# TEST OUTPUT (matches lab example)
# =========================================

print("\n--- ARRAY QUEUE ---")
aq = ArrayQueue()

aq.enqueue(10)
aq.display()
aq.enqueue(20)
aq.display()
aq.enqueue(30)
aq.display()
aq.peek()
aq.dequeue()
aq.display()
aq.size()

print("\n--- LINKED QUEUE ---")
lq = LinkedQueue()

lq.enqueue(10)
lq.display()
lq.enqueue(20)
lq.display()
lq.enqueue(30)
lq.display()
lq.peek()
lq.dequeue()
lq.display()
lq.size()