from queue import Queue

graph={

    "A": ["B","D"],
    "B" : ["A","C",],
    "C": ["B"],
    "D": ["A","E","F"],
    "E":["D","F","G"],
    "F": ["D","E","H"],
    "G":["E","H"],
    "H":["G","F"]
}

visited=[]
output=[]
source="A"
que=Queue()
que.put(source)
visited.append(source)

while not que.empty():
    u=que.get()
    output.append(u)
    for item in graph[u]:
        if item not in visited:
            que.put(item)
            visited.append(item)

print(output)
