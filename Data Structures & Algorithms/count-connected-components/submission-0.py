class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
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
        merged = 0
        for a,b in edges:
            if union(a,b):
                merged += 1
        return n - merged
        
