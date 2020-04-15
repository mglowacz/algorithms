def findSmallest(arr) :
  smallest = arr[0]
  smallestIndex = 0
  for i in range(1, len(arr)) :
    print(i)
    if arr[i] < smallest : 
      smallest = arr[i]
      smallestIndex = i
  
  print("Found smallest {} at index {}".format(smallest, smallestIndex))
  return smallestIndex


def selectionSort(arr) :
  sorted = []
  while len(arr) > 0 :
    smallestIndex = findSmallest(arr)
    sorted.append(arr.pop(smallestIndex))
  return sorted


list = [2,53,5,2,4477,95,321, -34]
print(findSmallest(list))



print("Sorted : ")
print(selectionSort(list))


