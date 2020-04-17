from collections import deque

def bfs(graph) :
  seen = []
  q = deque()
  q.append("a")

  print(q)
  while q :
    v = q.popleft()
    if v in seen : continue
    seen.append(v)
    print("seen", seen)
    for x in graph[v] : 
      q.append(x)



graph = {}
graph["a"] = ["b", "c"]
graph["b"] = ["d", "e"]
graph["c"] = ["e", "f"]
graph["d"] = ["i"]
graph["e"] = ["g"]
graph["f"] = ["g"]
graph["g"] = ["h"]
graph["h"] = []
graph["i"] = ["j"]
graph["j"] = []

print(bfs(graph))


#             i
#           /   \
#         d       j
#       / 
#     b
#   /   \
# a       e       h
#   \   /   \   /
#     c       g 
#       \   /
#         f  
#

