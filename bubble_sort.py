def bubble_sort(arr):
  # set sorted flag
  sorted = False
  # since each iteration sorts the highest unsorted index, last_unsorted_index keeps track of the last unsorted index 
  last_unsorted_index = len(arr) - 1
  # run a while loop until arr is not sorted
  while not sorted:
    # set sorted equal to True
    sorted = True
    # run a for loop until the last_sorted_index
    for i in range(last_sorted_index):
      # set sorted to False if two array elements are not sorted
      if arr[i] > arr[i + 1]:
        sorted = False
        # swap the unsorted elements
        arr[i], arr[i + 1] = arr[i + 1], arr[i]
        # minus 1 from the last_unsorted_index
        last_unsorted_index -= 1
