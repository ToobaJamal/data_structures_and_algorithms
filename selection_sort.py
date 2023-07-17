def selection_sort(arr):
    # initiate spot_marker variable
    spot_marker = 0
    # run loop while spot_marker is less than len of arr
    while spot_marker < len(arr):
        for i in range(spot_marker, len(arr)):
          # swap elements if arr[i] is less than element at spot_marker
            if arr[i] < arr[spot_marker]:
                arr[spot_marker], arr[i] = arr[i], arr[spot_marker]
        spot_marker += 1

# More efficient but slower algo

def selection_sort(arr):
    for i in range(len(arr)):
        min_index = i
        for j in range(i+1, len(arr)):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]
