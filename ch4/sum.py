def sum(arr) : 
  print(arr)
  if arr == [] : return 0
  return arr[0] + sum(arr[1:])


print("Sum = {}".format(sum([1,2,3,4,5,6])))




