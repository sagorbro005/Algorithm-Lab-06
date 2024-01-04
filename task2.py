import heapq
inputFile=open('input2_3.txt', 'r')
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
source1,source2=list(map(int,inputFile.readline().split(' ')))
# Shortest path for source 1
visited1=[False]*(n_vertices+1)
queue1=[]
shortest_path1=[float('inf')]*(n_vertices+1)
shortest_path1[source1]=0
# In the queue (weight,vertex) will be appended in sorted order
heapq.heappush(queue1,(0,source1))
while queue1:
    _,current_vertex=heapq.heappop(queue1)
    if not visited1[current_vertex]:
        visited1[current_vertex] = True
        if current_vertex in dict1:
            for adjacency_vertex,weight in dict1[current_vertex]:
                # if a vertex is already visited then its weight is unchangeable
                if not visited1[adjacency_vertex]:
                    new_cost=shortest_path1[current_vertex]+weight
                    if new_cost<shortest_path1[adjacency_vertex]:
                        shortest_path1[adjacency_vertex]=new_cost
                        heapq.heappush(queue1,(new_cost,adjacency_vertex))
# Shortest path for source 2
visited2=[False]*(n_vertices+1)
queue2=[]
shortest_path2=[float('inf')]*(n_vertices+1)
shortest_path2[source2]=0
# In the queue (weight,vertex) will be appended in sorted order
heapq.heappush(queue2,(0,source2))
while queue2:
    _,current_vertex=heapq.heappop(queue2)
    if not visited2[current_vertex]:
        visited2[current_vertex] = True
        if current_vertex in dict1:
            for adjacency_vertex,weight in dict1[current_vertex]:
                # if a vertex is already visited then its weight is unchangeable
                if not visited2[adjacency_vertex]:
                    new_cost=shortest_path2[current_vertex]+weight
                    if new_cost<shortest_path2[adjacency_vertex]:
                        shortest_path2[adjacency_vertex]=new_cost
                        heapq.heappush(queue2,(new_cost,adjacency_vertex))
# This block of code for in which vertex source1 and source2 will meet and
# minimum time to reach to the target vertex from their starting point
# If there is any infinity in the shortest path then we will skip that because source vertex never goes to that vertex
index=None
for i in range(1,n_vertices+1):
    if shortest_path1[i]!=float('inf') and shortest_path2[i]!=float('inf'):
        if index is None:
            index=i
        else:
            if shortest_path1[i]>shortest_path2[i]:
                max1=shortest_path1[i]
            else:
                max1=shortest_path2[i]
            if shortest_path1[index]>shortest_path2[index]:
                max2=shortest_path1[index]
            else:
                max2=shortest_path2[index]
            if max1<max2:
                index=i
outputFile=open('output2_3.txt', 'w')
# After doing the above task if we get index=None then it means all vertices containing infinity
# that means there is no common point for both of the source vertex
if index is None:
    result='Impossible'
# if index!=None then the greatest index value of shortest_path will be minimum time to reach the target vertex
# Common meetup point will be the index
else:
    if shortest_path1[index]>shortest_path2[index]:
        time=shortest_path1[index]
    else:
        time=shortest_path2[index]
    result=f'Time {str(time)}\nNode {str(index)}'
outputFile.writelines(result)