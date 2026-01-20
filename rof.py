# # is there any path import heapq
# def astar(grid,start,goal):
#     rows=len(grid)
#     cols=len(grid[0])

#     def h(x,y):
#         return abs(x-goal[0])+abs(y-goal[1])
    
#     pq=[]
#     heapq.heappush(pq,(h(*start),0,start,None))
#     visited={}

#     while pq:
#         f,g,node,parent=heapq.heappop(pq)
       

#         if node in visited:
#             continue
#         visited[node]=parent

#         if node == goal:
#              path=[]
#              cur=goal
#              while cur:
#                  path.append(cur)
#                  cur=visited[cur]

#              return path[::-1]     
#         (x,y)=node
#         for dx,dy in [(0,-1),(-1,0),(0,1),(1,0)]:
#             if 0 <=x+dx<rows and 0<=y+dy<cols and grid[x+dx][y+dy]==0:
#                 ng=g+1
#                 nf=ng+h(x+dx,y+dy)
#                 heapq.heappush(pq,(nf,ng,(x+dx,y+dy),(x,y)))

#     return None

# import heapq
# def greedy(grid,start,goal):
#     rows=len(grid)
#     cols=len(grid[0])

#     def h(x,y):
#         return abs(x-goal[0])+abs(y-goal[1])
    
#     pq=[]
#     heapq.heappush(pq,(h(*start),0,start,None))
#     visited={}

#     while pq:
#         f,g,node,parent=heapq.heappop(pq)
       

#         if node in visited:
#             continue
#         visited[node]=parent

#         if node == goal:
#              path=[]
#              cur=goal
#              while cur:
#                  path.append(cur)
#                  cur=visited[cur]

#              return path[::-1]     
#         (x,y)=node
#         for dx,dy in [(0,-1),(-1,0),(0,1),(1,0)]:
#             if 0 <=x+dx<rows and 0<=y+dy<cols and grid[x+dx][y+dy]==0:
               
#                 nf=h(x+dx,y+dy)
#                 heapq.heappush(pq,(nf,0,(x+dx,y+dy),(x,y)))

#     return None
# grid = [
#     [0, 1, 0, 1, 0, 1, 1, 1, 0, 0,1, 0],  # Row 0 (top)
#     [0, 1, 0, 1, 0, 0, 0,1, 0, 1, 1, 0],  # Row 1
#     [0, 0, 0, 1, 0, 1, 0, 0, 0,1,1, 0],  # Row 2
#     [1, 0, 1, 1, 0, 1, 0, 1, 0,1, 1, 0],  # Row 3
#     [1, 0, 0, 0, 0, 1, 0, 1, 0,0,0, 0],  # Row 4
#     [1, 1, 1, 0, 1, 1, 0, 1,1, 1, 1, 1],  # Row 5
#     [0, 0, 0, 0, 1, 1, 0, 0, 0, 0,0, 0]   # Row 6 (bottom)
# ]


# start = (6, 0)  # 'A' in bottom-left
# goal = (11, 11)   # 'B' in top-right


# print("A* Path:", astar(grid, start, goal))
# print("Greedy Path:", greedy(grid, start, goal))from collections import Counter
from collections import Counter
a = "aaaaabbbccc"
my_counter = Counter(a)
print(my_counter.values())
a = "aaaaabbbccc"
my_counter = Counter(a)
print(my_counter.values())
print(my_counter.most_common(1)[0][1])
import heapq

def astar_graph_list(graph, heuristic, start, goal, greedy=False):
    """
    graph: list of lists, graph[i] = list of neighbors of node i
    heuristic: list, heuristic[i] = estimated cost from node i to goal
    start, goal: integer indices of start and goal nodes
    greedy: if True, perform greedy best-first search
    """
    pq = []
    heapq.heappush(pq, (heuristic[start], 0, start, None))
    visited = {}  # node -> parent

    while pq:
        f, g, node, parent = heapq.heappop(pq)

        if node in visited:
            continue

        visited[node] = parent

        if node == goal:
            path = []
            cur = goal
            while cur is not None:
                path.append(cur)
                cur = visited[cur]
            return path[::-1]

        for neigh in graph[node]:  # unweighted graph
            ng = g + 1  # COST per edge
            nf = heuristic[neigh] if greedy else ng + heuristic[neigh]
            heapq.heappush(pq, (nf, ng, neigh, node))

    return None


# Example usage with nested lists:
# Node 0 = A, 1 = B, 2 = C, 3 = D
graph_list = [
    [1, 2],  # A -> B, C
    [3],     # B -> D
    [3],     # C -> D
    []       # D
]

heuristic = [3, 2, 2, 0]  # Example heuristic values to goal D

path = astar_graph_list(graph_list, heuristic, start=0, goal=3, greedy=False)
print("Path:", path)
