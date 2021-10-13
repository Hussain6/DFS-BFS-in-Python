
# graph={
#     "A":["B","C"],
#     "B": ["D","E"],
#     "C":["B","F"],
#     "D":[],
#     "E":["F"],
#     "F":[]
# }
graph={

    "1": ["2","7","8"],
    "2" : ["3","6",],
    "3": ["4","5"],
    "4": [],
    "5":[],
    "6": [],
    "7":[],
    "8":["9","12"],
    "9":["10","11"],
    "10":[],
    "11":[],
    "12":[]
}

stack=[]

def DFS(start):
    if("11" not in stack):
        stack.append(start)
        for items in graph[start]:
          if items not in stack:
              DFS(items)

source="1"
DFS(source)
print(stack)



