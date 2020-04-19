def frange(start, stop, step) :
  range = []
  v = start
  while v < stop :
    range.append(v)
    v+=step
  return range

def dynamic(items, bag, q) :
  r = frange(q, bag + q, q)
  print(r)
  subbags = r
  tab = []
  for i in range(0, len(items)) :
    row = []
    for weight in subbags :
      row.append([])
    tab.append(row)

  def printTab() :
    for i in range(0, len(items)) :
      print(tab[i])

  for i in range(0, len(items)) :
    for idx, subbagWeight in enumerate(subbags) :
      item = items[i]
      itemValue = item[1]
      itemWeight = item[2]
      tabWeight = 0
      tabValue = 0
      leftWeight = subbagWeight - itemWeight
      leftWeightIdx = [idx for idx, val in enumerate(subbags) if val == leftWeight]
      bestLeftItems = tab[i-1][leftWeightIdx[0]] if i > 0 and leftWeightIdx != [] else []
      bestLeftItemsValue = 0
      
      if (i > 0) : 
        for bestLeftItem in bestLeftItems :
          bestLeftItemsValue += bestLeftItem[1]
      
      for tabItem in tab[i][idx] :
        tabWeight += tabItem[2]
        tabValue += tabItem[1]
      
      previousItems = tab[i-1][idx] if tab[i-1][idx] else []
      previousValue = 0
      for previousItem in previousItems : previousValue += previousItem[1]
      
      
      if itemWeight <= subbagWeight and itemValue + bestLeftItemsValue > previousValue :
        tab[i][idx].append(item)
        tab[i][idx] += bestLeftItems
      else :
        tab[i][idx] += previousItems


  printTab()


  print("best set : ")
  bestSet = []
  bestSetValue = 0

  for i in range(0, len(items)) :
    for s in range (0, len(subbags)) :
      set = tab[i][s]
      setValue = 0
      for v in set : setValue += v[1]
      if setValue > bestSetValue :
        bestSetValue = setValue
        bestSet = set
  print(bestSet)
  print(bestSetValue)
  return bestSet


dynamic([('guitar', 1500, 1), ('stereo', 3000, 4), ('laptop', 2000, 3), ('iphone', 2000, 1), ('mp3', 1000, 1)], 4, 1)

dynamic([('westminster', 7, 0.5), ('globe theatre', 6, 0.5), ('national gallery', 9, 1), ('museum', 9, 2), ('cathedral', 8, 0.5)], 2, 0.5)

dynamic([('water', 10, 3), ('book', 3, 1), ('food', 3, 2), ('jacket', 5, 2), ('camera', 6, 1)], 6, 1)
