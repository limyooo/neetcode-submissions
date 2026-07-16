class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = defaultdict(list)
        in_degree = [0] * numCourses
        for a,b in prerequisites:
            graph[b].append(a)
            in_degree[a] += 1
        dq = deque(i for i in range(numCourses) if in_degree[i] == 0)

        count = 0
        while dq:
            curr = dq.popleft()
            count += 1
            for neigh in graph[curr]:
                in_degree[neigh] -= 1
                if in_degree[neigh] == 0:
                    dq.append(neigh)
        return count == numCourses