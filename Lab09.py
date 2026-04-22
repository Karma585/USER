# Task 1: Selection Sort

def selection_sort(arr):
    n = len(arr)
    print("Original list:", arr)

    for i in range(n - 1):
        min_index = i

        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j

        # Swap
        arr[i], arr[min_index] = arr[min_index], arr[i]

        print(f"Pass {i+1}: {arr}")

    print("Sorted list:", arr)


# Test
arr = [29, 10, 14, 37, 13]
selection_sort(arr)

# Task 2: Selection Sort with counting

def selection_sort(arr):
    n = len(arr)
    comparisons = 0
    swaps = 0

    print("Original list:", arr)

    for i in range(n - 1):
        min_index = i

        for j in range(i + 1, n):
            comparisons += 1
            if arr[j] < arr[min_index]:
                min_index = j

        if min_index != i:
            arr[i], arr[min_index] = arr[min_index], arr[i]
            swaps += 1

        print(f"Pass {i+1}: {arr}")

    print("Sorted list:", arr)
    print("Total comparisons:", comparisons)
    print("Total swaps:", swaps)


# Test
arr = [29, 10, 14, 37, 13]
selection_sort(arr)

# Task 3: Create Index Table

def create_index_table(arr, block_size):
    index_table = []

    for i in range(0, len(arr), block_size):
        index_table.append((arr[i], i))

    print("Index table created:")
    for value, index in index_table:
        print(f"{value} -> {index}")

    return index_table


# Test
arr = [10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65]
block_size = 3

create_index_table(arr, block_size)

# Task 4: Indexed Search (Key Found)

def indexed_search(arr, index_table, key):
    print("Search key:", key)

    # Find range
    for i in range(len(index_table)):
        if i == len(index_table) - 1 or key < index_table[i + 1][0]:
            start = index_table[i][1]
            end = index_table[i + 1][1] - 1 if i < len(index_table) - 1 else len(arr) - 1
            break

    print("Index range found:")
    print(f"{arr[start]} <= {key} < {arr[end+1] if end+1 < len(arr) else 'end'}")

    print(f"Searching from index {start} to {end}:")

    for i in range(start, end + 1):
        print(f"Checking index {i}: {arr[i]}")
        if arr[i] == key:
            print(f"{key} found at index {i}")
            return i

    print("Not found")
    return -1


# Test
arr = [10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65]
index_table = [(10, 0), (25, 3), (40, 6), (55, 9)]

indexed_search(arr, index_table, 45)

# Task 5: Indexed Search (Key Not Found)

def indexed_search(arr, index_table, key):
    print("Search key:", key)

    # Find range
    for i in range(len(index_table)):
        if i == len(index_table) - 1 or key < index_table[i + 1][0]:
            start = index_table[i][1]
            end = index_table[i + 1][1] - 1 if i < len(index_table) - 1 else len(arr) - 1
            break

    print("Index range found:")
    print(f"{arr[start]} <= {key} < {arr[end+1] if end+1 < len(arr) else 'end'}")

    print(f"Searching from index {start} to {end}:")

    for i in range(start, end + 1):
        print(f"Checking index {i}: {arr[i]}")
        if arr[i] == key:
            print(f"{key} found at index {i}")
            return i

    print(f"{key} not found")
    return -1


# Test
arr = [10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65]
index_table = [(10, 0), (25, 3), (40, 6), (55, 9)]

indexed_search(arr, index_table, 43)