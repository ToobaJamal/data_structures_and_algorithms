# Compute the running median of a sequence of numbers. That is, given a stream of numbers, print out the median of the list so far on each new element.

# For example, given the sequence [2, 1, 5, 7, 2, 0, 5], your algorithm should print out:

def median(arr):
    for i in range(1, len(arr)):
        j = i
        while arr[j - 1] > arr[j] and j > 0:
            arr[j - 1], arr[j] = arr[j], arr[j - 1]
            j -= 1
            
    return l[(len(l) + 1) // 2]
