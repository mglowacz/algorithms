from random import randint

def quickSort(arr) :
  if (len(arr) < 2) : return arr
  pivot = randint(0, len(arr))
  less = [val for idx, val in enumerate(arr) if val <= arr[pivot] and idx != pivot]
  greater = [val for idx, val in enumerate(arr) if val > arr[pivot] and idx != pivot]
  return quickSort(less) + [arr[pivot]] + quickSort(greater)


arr = [56, 21, 45, 2, 14, 86, 33, 12, 8]
print(arr)
print(quickSort(arr))


