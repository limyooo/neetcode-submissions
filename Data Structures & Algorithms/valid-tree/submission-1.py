class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n - 1:
            return False
        parent = {i:i for i in range(n)}
        
        def find(a):
            if parent[a] != a:
                parent[a] = find(parent[a])
            return parent[a] 

        def union(a,b):
            root_a = find(a)
            root_b = find(b)
            if root_a != root_b:
                parent[root_b] = root_a
                return True
            return False

        for a,b in edges:
            if not union(a,b):
                return False
        return True


