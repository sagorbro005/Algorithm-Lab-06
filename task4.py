import heapq
inputFile=open('input4_2.txt', 'r')
n_vertices,m_edges=list(map(int,inputFile.readline().split(' ')))
queue=[]
parent = list(range(n_vertices+1))
total=0
# Kruskal Algorithm
def find_parent(node):
    if parent[node]!=node:
        parent[node]=find_parent(parent[node])
    return parent[node]

# The union function merges the sets of vertices ver1 and ver2.
# It first finds the representatives of their sets. If they belong to different sets,
# it makes the representative of ver1’s set a child of the representative of ver2’s set,
# effectively merging the two sets. It then adds the weight of the edge between ver1 and ver2 to total.
def union(ver1,ver2,weight):
    global total
    ver1_parent = find_parent(ver1)
    ver2_parent = find_parent(ver2)
    if ver1_parent!=ver2_parent:
        parent[ver2_parent]=ver1_parent
        total+=weight

# This loop reads the next m_edges lines of the input file,
# each containing three integers separated by spaces. For each line,
# it splits the line into three strings, converts them to integers,
# and pushes a tuple containing the weight and the two vertices onto the priority queue.
for i in range(m_edges):
    ver1,ver2,weight=list(map(int,inputFile.readline().split(' ')))
    heapq.heappush(queue,(weight,ver1,ver2))

# This loop pops tuples from the priority queue until it is empty.
# For each tuple, it calls the union function on the two vertices and the weight.
while queue:
    weight,ver1,ver2=heapq.heappop(queue)
    union(ver1,ver2,weight)
outputFile=open('output4_2.txt','w')
outputFile.writelines(str(total))

