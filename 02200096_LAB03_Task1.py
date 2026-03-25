class ArrayStack:
    def __init__(self, capacity=10):
        self.stack = [None] * capacity   # array for storing elements
        self.top = -1                    # variable to track top
        self.capacity = capacity
        print("Created new ArrayStack with capacity:", capacity)

    def is_empty(self):
        return self.top == -1


# Testing Task 1
s = ArrayStack()

print("Stack is empty:", s.is_empty())

class ArrayStack:
    def __init__(self, capacity=10):
        self.stack = [None] * capacity
        self.top = -1
        self.capacity = capacity

    def push(self, element):
        if self.top == self.capacity - 1:
            print("Stack Overflow")
            return
        self.top += 1
        self.stack[self.top] = element
        print("Pushed", element, "to the stack")

    def pop(self):
        if self.top == -1:
            print("Stack Underflow")
            return None
        popped = self.stack[self.top]
        self.top -= 1
        print("Popped element:", popped)
        return popped

    def peek(self):
        if self.top == -1:
            return None
        return self.stack[self.top]

    def is_empty(self):
        return self.top == -1

    def size(self):
        return self.top + 1

    def display(self):
        if self.top == -1:
            print("Stack is empty")
        else:
            print("Display stack:", self.stack[:self.top+1])


# Testing Task 2
s = ArrayStack()

s.push(10)
s.display()

s.push(20)
s.display()

s.push(30)
s.display()

print("Top element:", s.peek())

s.pop()

print("Stack size:", s.size())

s.display()