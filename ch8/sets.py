statesNeeded = set(["mt", "wa", "or", "id", "nv", "ut" ,"ca", "az"])

stations = {}
stations["kone"] = set(["id", "nv", "ut"])
stations["ktwo"] = set(["wa", "id", "mt"])
stations["kthree"] = set(["or", "nv", "ca"])
stations["kfour"] = set(["nv", "ut"])
stations["kfive"] = set(["ca", "az"])

finalStations = set()

while statesNeeded :
  bestStation = None
  bestStationCovered = set()
  for station, states in stations.items() :
    covered = statesNeeded & states
    if len(covered) > len(bestStationCovered) : 
      bestStation = station
      bestStationCovered = covered

  finalStations.add(bestStation)
  statesNeeded -= bestStationCovered

print(finalStations)
