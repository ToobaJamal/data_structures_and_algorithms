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
