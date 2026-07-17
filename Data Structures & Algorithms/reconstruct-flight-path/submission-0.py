class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        graph = defaultdict(list)
        for a,b in tickets:
            graph[a].append(b)
        for key in graph:
            graph[key].sort(reverse=True)
        path = []
        def dfs(airport):
            while graph[airport]:
                nxt = graph[airport].pop()
                dfs(nxt)
            path.append(airport)
        dfs('JFK')
        return path[::-1]