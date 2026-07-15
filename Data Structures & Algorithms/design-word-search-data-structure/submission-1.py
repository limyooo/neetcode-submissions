class WordDictionary:

    def __init__(self):
        self.children = {}
        self.is_end = False

    def addWord(self, word: str) -> None:
        node = self
        for w in word:
            if w not in node.children:
                node.children[w] =  WordDictionary()
            node = node.children[w]
        node.is_end = True

    def search(self, word: str) -> bool:
        def dfs(node,index):
            if index == len(word):
                return node.is_end
            ch = word[index]
            if ch == '.':
                for child in node.children.values():
                    if dfs(child,index+1):
                        return True
                return False
            else:
                if ch not in node.children:
                    return False
                return dfs(node.children[ch],index+1)
        return dfs(self,0)
