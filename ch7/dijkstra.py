def findLowestCostNode(costs, seen) :
  cost = float("inf")
  node = None
  for n in costs.keys() :
    if n not in seen and costs[n] < cost : 
      cost = costs[n]
      node = n
  return node

def shortestPath(graph, costs, parents) :
  seen = []
  node = findLowestCostNode(costs, seen)
  
  while node is not None :
    seen.append(node)
    for n in graph[node].keys() :
      if costs[n] > costs[node] + graph[node][n] :
        costs[n] = costs[node] + graph[node][n]
        parents[n] = node
    
    node = findLowestCostNode(costs, seen)
  return (getRoute(parents), costs["finish"])

def getRoute(parents) :
  route = []
  current = "finish"
  while current != "start" :
    route.append(current)
    current = parents[current]
  route.append("start")
  route.reverse()
  return route

g = { "start" : { "a" : 6, "b" : 2},
      "a" : { "finish" : 1 }, 
      "b" : { "a" : 3, "finish" : 5 },
      "finish":{}}
c = { "a" : 6, 
      "b" : 2, 
      "finish" : float("inf")}
p = { "a" : "start", 
      "b" : "start", 
      "finish" : None}

print(shortestPath(g, c, p))

g = { "start" : { "a" : 5, "b" : 2},
      "a" : { "c" : 4, "d" : 2 }, 
      "b" : { "a" : 8, "d" : 7 },
      "c" : { "d" : 6, "finish" : 3 },
      "d" : { "finish" : 1 },
      "finish":{}}
c = { "a" : 5, 
      "b" : 2, 
      "c" : float("inf"),
      "d" : float("inf"),
      "finish" : float("inf")}
p = { "a" : "start", 
      "b" : "start", 
      "c" : None, 
      "d" : None, 
      "finish" : None}

print(shortestPath(g, c, p))

g = { "start" : { "a" : 10 },
      "a" : { "c" : 20 }, 
      "b" : { "a" : 1 },
      "c" : { "finish" : 30 },
      "finish":{}}
c = { "a" : 10, 
      "b" : float("inf"), 
      "c" : float("inf"), 
      "finish" : float("inf")}
p = { "a" : "start", 
      "b" : None, 
      "c" : None, 
      "finish" : None}

print(shortestPath(g, c, p))

g = { "start" : { "a" : 2, "b" : 2 },
      "a" : { "b" : 2 }, 
      "b" : { "c" : 2, "finish" : 2 },
      "c" : { "a" : -1, "finish" : 2 },
      "finish":{}}
c = { "a" : 2, 
      "b" : 2, 
      "c" : float("inf"), 
      "finish" : float("inf")}
p = { "a" : "start", 
      "b" : "start", 
      "c" : None, 
      "finish" : None}

print(shortestPath(g, c, p))
