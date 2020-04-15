def binarySearch(list, item):
  low = 0
  high = len(list) - 1
  while low <= high :
    mid = (low + high) // 2
    print("low : {}, mid : {}, high : {}".format(low, mid, high))
    if list[mid] == item : return mid
    elif list[mid] > item : high = mid - 1
    else : low = mid + 1
  return None

list = [0, 1, 5, 10, 13, 24, 44, 52, 68, 72]

print(list)
print("Looking for {}".format(68))
print(binarySearch(list, 68))
print()


print(list)
print("Looking for {}".format(0))
print(binarySearch(list, 0))
print()


print(list)
print("Looking for {}".format(44))
print(binarySearch(list, 44))
print()


print(list)
print("Looking for {}".format(36))
print(binarySearch(list, 36))
print()


