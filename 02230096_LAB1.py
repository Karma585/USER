class CustomList:
    def __init__(self, capacity=10):
        # Private variables
        self._capacity = capacity
        self._size = 0
        self._data = [None] * capacity

        print(f"Created new CustomList with capacity: {self._capacity}")
        print(f"Current size: {self._size}")


# Create an object of CustomList
myList = CustomList()

class CustomList:
    def __init__(self, capacity=10):
        self._capacity = capacity
        self._size = 0
        self._data = [None] * capacity

        print(f"Created new CustomList with capacity: {self._capacity}")
        print(f"Current size: {self._size}")

    # 1. append(element)
    def append(self, element):
        if self._size >= self._capacity:
            print("List is full. Cannot append.")
            return
        
        self._data[self._size] = element
        self._size += 1
        print(f"Appended {element} to the list")

    # 2. get(index)
    def get(self, index):
        if index < 0 or index >= self._size:
            print("Index out of bounds")
            return None
        
        value = self._data[index]
        print(f"Element at index {index}: {value}")
        return value

    # 3. set(index, element)
    def set(self, index, element):
        if index < 0 or index >= self._size:
            print("Index out of bounds")
            return
        
        self._data[index] = element
        print(f"Set element at index {index} to {element}")

    # 4. size()
    def size(self):
        print(f"Current size: {self._size}")
        return self._size


# Example usage
myList = CustomList()

myList.append(5)
myList.get(0)
myList.set(0, 10)
myList.get(0)
myList.size()