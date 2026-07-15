class Trie():
    def __init__(self):
        self.children = {}
        self.is_end = False
    def insert(self,word):
        node = self
        for w in word:
            if w not in node.children:
                node.children[w] = Trie()
            node = node.children[w]
        node.is_end = True
class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        trie = Trie()
        for word in words:
            trie.insert(word)
        res = []
        n,m = len(board),len(board[0])
        visited = [[False] * m for _ in range(n)]
        def dfs(x,y,path,node):
            if board[x][y] not in node.children:
                return 
            node = node.children[board[x][y]]
            path += board[x][y]
            visited[x][y] = True
            if node.is_end:
                res.append(path)
                node.is_end = False
            direction = [[1,0],[-1,0],[0,-1],[0,1]]
            for i,j in direction:
                nx = x + i
                ny = y + j
                if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny]:
                    dfs(nx,ny,path,node)
            visited[x][y] = False

        for i in range(n):
            for j in range(m):
                dfs(i,j,"",trie)
        return res