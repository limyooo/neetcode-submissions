class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0
        word_set = set(wordList)
        que = deque([(beginWord,1)])

        while que:
            word,step = que.popleft()
            if word == endWord:
                return step
            for i in range(len(word)):
                for j in 'qwertyuiopasdfghjklzxcvbnm':
                    new_word = word[:i] + j + word[i+1:]
                    if new_word in word_set:
                        word_set.remove(new_word)
                        que.append((new_word,step + 1))
        return 0

