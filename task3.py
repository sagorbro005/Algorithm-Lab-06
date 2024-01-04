inputFile = open('input3_2.txt','r')
outputFile= open('output3_2.txt','w')
n, k = list(map(int,inputFile.readline().split(' ')))
parent = list(range(n+1))
frnd_circle = [1]*(n+1)       # There are no friendship between each other initially

# The find_parent function returns the representative (or the parent) of the friend circle
# that person node belongs to. If node is not its own parent, it recursively calls find_parent on its parent and
# updates its parent to the representative of its friend circle. This is known as “path compression”.
def find_parent(node):
    if parent[node]!=node:
        parent[node]=find_parent(parent[node])
    return parent[node]

# The union function merges the friend circles of persons ver1 and ver2.
# It first finds the representatives of their friend circles. If they belong to different friend circles,
# it makes the representative of ver1’s friend circle a child of the representative of ver2’s friend circle,
# effectively merging the two friend circles. It then updates the size of the new friend circle
def union(ver1,ver2):
    ver1_parent = find_parent(ver1)
    ver2_parent = find_parent(ver2)
    if ver1_parent!=ver2_parent:
        parent[ver2_parent]=ver1_parent
        frnd_circle[ver2_parent]+=frnd_circle[ver1_parent]
        frnd_circle[ver1_parent]=frnd_circle[ver2_parent]
    outputFile.writelines(str(frnd_circle[ver2_parent])+'\n')

for i in range(k):
    ver1,ver2=list(map(int,inputFile.readline().split(' ')))
    union(ver1,ver2)

