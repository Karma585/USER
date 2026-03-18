# Node class
class Node:
    def __init__(self, data):
        self.data = data   # stores the value
        self.next = None   # points to next node


# LinkedList class
class LinkedList:
    def __init__(self):
        self.head = None   # first node
        self.tail = None   # last node (optional)
        self.size = 0      # number of elements

        print("Created new LinkedList")
        self.print_status()

    # Method to display current status
    def print_status(self):
        print("Current size:", self.size)
        print("Head:", self.head.data if self.head else "None")


# Create a new LinkedList
list1 = LinkedList()

# Node class
class Node:
    def __init__(self, data):
        self.data = data   # stores the value
        self.next = None   # points to next node


# LinkedList class
class LinkedList:
    def __init__(self):
        self.head = None   # first node
        self.tail = None   # last node (optional)
        self.size = 0      # number of elements

        print("Created new LinkedList")
        self.print_status()

    # Method to display current status
    def print_status(self):
        print("Current size:", self.size)
        print("Head:", self.head.data if self.head else "None")


# Create a new LinkedList
list1 = LinkedList()