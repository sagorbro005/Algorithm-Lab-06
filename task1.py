import heapq
inputFile=open('input1_1.txt', 'r')
n_vertices,m_edges=list(map(int,inputFile.readline().split(' ')))
dict1={}
for i in range(m_edges):
    ver1,ver2,weight=list(map(int, inputFile.readline().split(' ')))
    try:
        dict1[ver1].append((ver2,weight))
    except KeyError:
        dict1[ver1] = [(ver2,weight)]
# For weighted graph Dijkstra's Algorithm will be used
# Priority queue will be used for after visiting one vertex
# which neighbour's vertex has less weight will come first
# If a vertex is already visited it will be not be counted anymore
source=int(inputFile.readline())
visited=[False]*(n_vertices+1)
queue=[]
shortest_path=[float('inf')]*(n_vertices+1)
shortest_path[source]=0
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
                    new_cost=shortest_path[current_vertex]+weight
                    if new_cost<shortest_path[adjacency_vertex]:
                        shortest_path[adjacency_vertex]=new_cost
                        heapq.heappush(queue,(new_cost,adjacency_vertex))
# If there is any infinity remaining, it will be replaced by -1
for i in range(n_vertices+1):
    if shortest_path[i]==float('inf'):
        shortest_path[i]=-1
outputFile=open('output1_1.txt', 'w')
# for key in dict1.keys():
#     value=dict1[key]
#     outputFile.writelines(f'{key}: {value}\n')
outputFile.writelines(' '.join(map(str,shortest_path[1:])))
