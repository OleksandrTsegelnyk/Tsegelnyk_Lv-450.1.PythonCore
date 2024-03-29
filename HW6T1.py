# Given an array of integers.
#
# Return an array, where the first element is the count of positives numbers and the second element is sum of negative numbers.
#
# If the input array is empty or null, return an empty array.
#
# Example
# For input [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, -11, -12, -13, -14, -15], you should return [10, -65].

def count_positives_sum_negatives(arr):
    count_positive = len(list(n for n in arr if n > 0))
    negative_sum = sum(n for n in arr if n < 0)
    return [count_positive, negative_sum] if len(arr) > 0 else []

