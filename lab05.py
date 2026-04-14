# -------------------------------
# LAB 5: Search Algorithms
# -------------------------------

# Part 1: Sequential Search
def sequential_search(arr, target):
    comparisons = 0
    for i in range(len(arr)):
        comparisons += 1
        if arr[i] == target:
            return i, comparisons
    return -1, comparisons


# Part 2: Binary Search (Iterative)
def binary_search_iterative(arr, target):
    left = 0
    right = len(arr) - 1
    comparisons = 0

    while left <= right:
        mid = (left + right) // 2
        comparisons += 1

        if arr[mid] == target:
            return mid, comparisons
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1, comparisons


# Part 2: Binary Search (Recursive)
def binary_search_recursive(arr, target, left, right, comparisons=0):
    if left > right:
        return -1, comparisons

    mid = (left + right) // 2
    comparisons += 1

    if arr[mid] == target:
        return mid, comparisons
    elif arr[mid] < target:
        return binary_search_recursive(arr, target, mid + 1, right, comparisons)
    else:
        return binary_search_recursive(arr, target, left, mid - 1, comparisons)


# -------------------------------
# Testing the Algorithms
# -------------------------------

# Unsorted list for sequential search
list1 = [23, 45, 12, 67, 89, 34, 56]
target = 67

print("Sequential Search:")
index, comp = sequential_search(list1, target)
print("List:", list1)
print("Searching for", target)

if index != -1:
    print("Found at index", index)
else:
    print("Not found")

print("Number of comparisons:", comp)


# Sorted list for binary search
list2 = sorted(list1)

print("\nBinary Search (Iterative):")
index, comp = binary_search_iterative(list2, target)
print("Sorted List:", list2)
print("Searching for", target)

if index != -1:
    print("Found at index", index)
else:
    print("Not found")

print("Number of comparisons:", comp)


print("\nBinary Search (Recursive):")
index, comp = binary_search_recursive(list2, target, 0, len(list2) - 1)
print("Sorted List:", list2)
print("Searching for", target)

if index != -1:
    print("Found at index", index)
else:
    print("Not found")

print("Number of comparisons:", comp)