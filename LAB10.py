# PART 01 Counting Sort Implementation
def counting_sort(arr):
    if len(arr) == 0:
        return arr

    # Find maximum value in the array
    max_val = max(arr)

    # Create count array
    count = [0] * (max_val + 1)

    # Count occurrences of each element
    for num in arr:
        count[num] += 1

    # Build the sorted array
    sorted_arr = []
    for i in range(len(count)):
        for _ in range(count[i]):
            sorted_arr.append(i)

    return sorted_arr


# -------- Main Program --------
if __name__ == "__main__":
    arr = [4, 2, 2, 8, 3, 3, 1]

    print("Original Array:", arr)
    sorted_arr = counting_sort(arr)
    print("Sorted Array:", sorted_arr)

#PART 02 Radix Sort Implementation
def counting_sort_for_radix(arr, exp):
    n = len(arr)

    # Output array
    output = [0] * n

    # Count array (0–9 for digits)
    count = [0] * 10

    # Step 1: Count occurrences of digits
    for i in range(n):
        index = (arr[i] // exp) % 10
        count[index] += 1

    # Step 2: Update count[i] to contain position info
    for i in range(1, 10):
        count[i] += count[i - 1]

    # Step 3: Build output array (stable sort)
    i = n - 1
    while i >= 0:
        index = (arr[i] // exp) % 10
        output[count[index] - 1] = arr[i]
        count[index] -= 1
        i -= 1

    # Step 4: Copy output to original array
    for i in range(n):
        arr[i] = output[i]


def radix_sort(arr):
    if len(arr) == 0:
        return arr

    # Find maximum number
    max_val = max(arr)

    # Apply counting sort for each digit
    exp = 1
    while max_val // exp > 0:
        counting_sort_for_radix(arr, exp)
        exp *= 10

    return arr


# -------- Main Program --------
if __name__ == "__main__":
    arr = [170, 45, 75, 90, 802, 24, 2, 66]

    print("Original Array:", arr)
    sorted_arr = radix_sort(arr)
    print("Sorted Array:", sorted_arr)
