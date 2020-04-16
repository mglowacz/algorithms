def count(arr) :
  if arr == [] : return 0
  return 1 + count(arr[1:])

print("Count = {}".format(count([0,1,2,3,4,5,6,7,8,9])))

