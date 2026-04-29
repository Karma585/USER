# YourStudentNo_LAB6.py

# ---------------- QUICK SORT ---------------- #

def quick_sort(arr):
    comparisons = 0
    swaps = 0

    def median_of_three(a, low, high):
        mid = (low + high) // 2
        if a[low] > a[mid]:
            a[low], a[mid] = a[mid], a[low]
        if a[low] > a[high]:
            a[low], a[high] = a[high], a[low]
        if a[mid] > a[high]:
            a[mid], a[high] = a[high], a[mid]
        return mid

    def partition(a, low, high):
        nonlocal comparisons, swaps

        pivot_index = median_of_three(a, low, high)
        pivot = a[pivot_index]

        a[pivot_index], a[high] = a[high], a[pivot_index]
        swaps += 1

        i = low - 1
        for j in range(low, high):
            comparisons += 1
            if a[j] <= pivot:
                i += 1
                a[i], a[j] = a[j], a[i]
                swaps += 1

        a[i + 1], a[high] = a[high], a[i + 1]
        swaps += 1
        return i + 1

    def quick_sort_recursive(a, low, high):
        if low < high:
            pi = partition(a, low, high)
            quick_sort_recursive(a, low, pi - 1)
            quick_sort_recursive(a, pi + 1, high)

    quick_sort_recursive(arr, 0, len(arr) - 1)
    return arr, comparisons, swaps


# ---------------- MERGE SORT ---------------- #

def merge_sort(arr):
    comparisons = 0
    accesses = 0

    def merge(left, right):
        nonlocal comparisons, accesses
        result = []
        i = j = 0

        while i < len(left) and j < len(right):
            comparisons += 1
            accesses += 2
            if left[i] <= right[j]:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1
            accesses += 1

        while i < len(left):
            result.append(left[i])
            i += 1
            accesses += 1

        while j < len(right):
            result.append(right[j])
            j += 1
            accesses += 1

        return result

    def merge_sort_recursive(a):
        if len(a) <= 1:
            return a
        mid = len(a) // 2
        left = merge_sort_recursive(a[:mid])
        right = merge_sort_recursive(a[mid:])
        return merge(left, right)

    sorted_arr = merge_sort_recursive(arr)
    return sorted_arr, comparisons, accesses


# ---------------- MAIN ---------------- #

if __name__ == "__main__":
    data = [38, 27, 43, 3, 9, 82, 10]

    print("Original List:", data)

    # Quick Sort
    qs_sorted, qs_comp, qs_swaps = quick_sort(data.copy())
    print("\nSorted using Quick Sort:", qs_sorted)
    print("Number of comparisons:", qs_comp)
    print("Number of swaps:", qs_swaps)

    # Merge Sort
    ms_sorted, ms_comp, ms_access = merge_sort(data.copy())
    print("\nSorted using Merge Sort:", ms_sorted)
    print("Number of comparisons:", ms_comp)
    print("Number of array accesses:", ms_access)