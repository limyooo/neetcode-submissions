class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        parent = {i : i for i in range(1,n+1)}
        res = []
        def find(a):
            if parent[a] != a:
                parent[a] = find(parent[a])
            return parent[a]
        def union(a,b):
            root_a = find(a)
            root_b = find(b)
            if root_a != root_b:
                parent[root_b] = root_a
            else:
                return True
            return False
        for a,b in edges:
            if union(a,b):
                return[a,b]
        return []

