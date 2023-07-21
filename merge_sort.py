def merge_sorted(arr1, arr2):
  sorted_arr = []
  i, j = 0, 0
  while i < len(arr1) and j < len(arr2):
    if arr[i] < arr[j]:
      sorted_arr.append(arr[i])
      i += 1
    else:
      sorted_arr.append(arr[j])
      j += 1
    while i < len(arr1):
      sorted_arr.append(arr1[i])
      i += 1
    while j < len(arr2):
      sorted_arr.append(arr2[j])
      j += 1
    return sorted_arr
    
def divide_arr(arr):
  if len(arr) < 2:
    return arr[:]
  else:
    middle = len(arr) // 2
    l1 = divide_arr(arr[:middle])
    l2 = divide_arr(arr[middle:])
    return merge_sorted(l1, l2)