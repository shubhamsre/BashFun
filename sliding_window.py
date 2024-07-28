#!/bin/python3

def max_sum_subarray(arr, k):
    n = len(arr)
    if n < k:
        print("Invalid input: k is larger than the array length.")
        return None

    # Compute the sum of the first window of size k
    max_sum  = sum(arr[:k])
    current_window_sum = max_sum

    # Compute sums of remaining windows by removing the first element of the previous window and adding the next element
    for i in range(k, n):
        current_window_sum += arr[i] - arr[i - k]
        max_sum = max(max_sum, current_window_sum)

    return max_sum

# Example usage:
# arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# k = 3
# print(f"Maximum sum of all subarrays of size {k}: {max_sum_subarray(arr, k)}")

# For the array [1, 2, 3, 4, 5, 6, 7, 8, 9] and K=3
# K=3:
# Initial sum of the first subarray [1, 2, 3] is 6.
# Slide the window to get the next subarray [2, 3, 4], update the sum to 9 (by adding 4 and subtracting 1).
# Continue this process for all subarrays of size K.
# The function will return 24, which is the sum of the subarray [7, 8, 9], the maximum sum of all subarrays of size K.

