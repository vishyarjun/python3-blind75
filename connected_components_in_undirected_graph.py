from typing import List
def count_components(n: int, arr:List[List[int]]) ->int:
    parent = [i for i in range(n)]
    rank = [1]*n

    def find(n1):
        r = n1
        while r!=parent[r]:
            r = parent[parent[r]]
            r = parent[r]
        print(f'super parent of {n1} is {r}')
        return r

    print(parent)
    print(rank)
    def union(n1,n2):
        print(n1,n2)
        p1,p2 = find(n1),find(n2)

        if p1 == p2:
            return 0
        else:
            if rank[p2] > rank[p1]:
                parent[p1] = p2
                rank[p2] += rank[p1]
            else:
                parent[p2] = p1
                rank[p1] += rank[p2]
            return 1
    res = n
    for n1,n2 in arr:
        res-= union(n1,n2)
        print(parent)
        print(rank)
        print(res)
    return res
        
    
inp1 = [[0,1],[1,2],[2,3],[4,5]]
inp2 = [[0,1]]
print(count_components(6, inp1))
print(count_components(2, inp2))

'''
0--1--2--3

4--5

'''
