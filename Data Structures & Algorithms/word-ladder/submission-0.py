class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        dic=set(wordList)
        if endWord not in dic:
            return 0
        q=deque([beginWord])
        visited=set()
        visited.add(beginWord)
        steps=1
        while q:
            for _ in range(len(q)):
                word=q.popleft()
                if word==endWord:
                    return steps
                for i in range(len(word)):
                    for c in range(0,26):
                        char=chr(ord('a')+c)
                        if char == word[i]:
                            continue
                        newW=word[:i]+char+word[i+1:]
                        if newW not in dic:
                            continue
                        if newW in visited:
                            continue
                        visited.add(newW)
                        q.append(newW)
            steps+=1
        return 0
