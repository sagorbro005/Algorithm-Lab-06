import heapq
inputFile=open('input4b.txt', 'r')
n_vertices,m_edges=list(map(int,inputFile.readline().split(' ')))
dict1={}
for i in range(m_edges):
    ver1,ver2,weight=list(map(int, inputFile.readline().split(' ')))
    try:
        dict1[ver1].append((ver2,weight))
    except KeyError:
        dict1[ver1] = [(ver2,weight)]
    try:
        dict1[ver2].append((ver1,weight))
    except KeyError:
        dict1[ver2] = [(ver1,weight)]
# For weighted graph Prim's Algorithm (Similar to Dijkstra Algorithm) will be used
# Priority queue will be used for after visiting one vertex
# which neighbour's vertex has less weight will come first
# If a vertex is already visited it will be not be counted anymore
source=1
visited=[False]*(n_vertices+1)
queue=[]
shortest_path=[float('inf')]*(n_vertices+1)
shortest_path[source]=0
total=0
# In the queue (weight,vertex) will be appended in sorted order
heapq.heappush(queue,(0,source))
while queue:
    _,current_vertex=heapq.heappop(queue)
    if not visited[current_vertex]:
        visited[current_vertex] = True
        if current_vertex in dict1:
            for adjacency_vertex,weight in dict1[current_vertex]:
                # if a vertex is already visited then its weight is unchangeable
                if not visited[adjacency_vertex]:
                    if weight<shortest_path[adjacency_vertex]:
                        shortest_path[adjacency_vertex]=weight
                        heapq.heappush(queue,(weight,adjacency_vertex))
for i in range(1,len(shortest_path)):
    total+=shortest_path[i]
outputFile=open('output4b.txt', 'w')
outputFile.writelines(str(total))
