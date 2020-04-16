def max(arr) :
  if len(arr)==2 : return arr[0] if arr[0] > arr[1] else arr[1]
  restMax = max(arr[1:])
  return restMax if restMax > arr[0] else arr[0]
  

print("Max = {}".format(max([-2, 8, 15, -4, 10, 22, -30])))
