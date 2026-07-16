class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        in_degree = [0] * numCourses
        for a,b in prerequisites:
            graph[b].append(a)
            in_degree[a] += 1

        res = []
        que = deque(i for i in range(numCourses) if in_degree[i] == 0)
        while que:
            curr = que.popleft()
            res.append(curr)
            for nei in graph[curr]:
                in_degree[nei] -= 1
                if in_degree[nei] == 0:
                    que.append(nei)
        if len(res) == numCourses:
            return res
        else:
            return []