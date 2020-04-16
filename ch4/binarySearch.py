def binarySearch(arr, item) :
  if arr == [] : return -1
  if len(arr) == 1 : return 0 if item == arr[0] else -1
  mid = len(arr) // 2
  if arr[mid] == item : return mid

  sublist = arr[:mid] if arr[mid] > item else arr[mid + 1:] 
  subindex = 0 if arr[mid] > item else mid + 1
  bs = binarySearch(sublist, item)

  return -1 if bs == -1 else subindex + bs



arr = [1, 3, 4, 6, 7, 9, 12, 13, 18]

print(arr)
print("Found (1) at {}".format(binarySearch(arr, 1)))
print("Found (3) at {}".format(binarySearch(arr, 3)))
print("Found (7) at {}".format(binarySearch(arr, 7)))
print("Found (12) at {}".format(binarySearch(arr, 12)))
print("Found (18) at {}".format(binarySearch(arr, 18)))
print("Found (11) at {}".format(binarySearch(arr, 11)))

