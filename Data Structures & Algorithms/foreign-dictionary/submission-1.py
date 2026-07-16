class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        net_word = set("".join(words))
        graph = {letter: set() for letter in net_word}
        in_degree = {letter: 0 for letter in net_word}
        for i in range(len(words) - 1):
            w1 = words[i]
            w2 = words[i + 1]
            if len(w1) > len(w2) and w1.startswith(w2):
                return ""
            for a,b in zip(w1,w2):
                if a != b:
                    if b not in graph[a]:
                        graph[a].add(b)
                        in_degree[b] += 1
                    break #只需要比较第一个
        res = []
        que = deque([c for c in net_word if in_degree[c] == 0])
        while que:
            ch = que.popleft()
            res.append(ch)
            for nei in graph[ch]:
                in_degree[nei] -= 1
                if in_degree[nei] == 0:
                    que.append(nei)
        
        if len(res) != len(net_word):
            return ""
        return "".join(res)
