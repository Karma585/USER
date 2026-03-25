# Node class
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


# LinkedStack class
class LinkedStack:
    def __init__(self):
        self.top = None
        self.count = 0
        print("Created new LinkedStack")

    def is_empty(self):
        return self.top is None


# Testing Task 3
stack = LinkedStack()
print("Stack is empty:", stack.is_empty())

# Node class
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


# LinkedStack class with stack operations
class LinkedStack:
    def __init__(self):
        self.top = None
        self.count = 0

    def push(self, element):
        new_node = Node(element)
        new_node.next = self.top
        self.top = new_node
        self.count += 1
        print("Pushed", element, "to the stack")

    def pop(self):
        if self.top is None:
            print("Stack is empty")
            return None
        popped = self.top.data
        self.top = self.top.next
        self.count -= 1
        print("Popped element:", popped)

    def peek(self):
        if self.top is None:
            return None
        return self.top.data

    def is_empty(self):
        return self.top is None

    def size(self):
        return self.count

    def display(self):
        current = self.top
        print("Display stack:", end=" ")
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("null")


# Testing Task 4
stack = LinkedStack()

stack.push(10)
stack.display()

stack.push(20)
stack.display()

stack.push(30)
stack.display()

print("Top element:", stack.peek())

stack.pop()

print("Current stack:")
stack.display()

print("Stack size:", stack.size())