from typing import List

class Solution2:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:

        i = 0
        j = 0

        while i < len(s):

            while j < len(s) and s[i:j+1] not in wordDict:
                j += 1

            print(s[i:j+1])
            print(j)

            if j == len(s) and s[i:j+1] not in wordDict:
                return False

            i = j + 1

        return True

from collections import deque

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        words = set(wordDict)
        queue = deque([0])
        seen = set()

        while queue:
            start = queue.popleft()
            if start == len(s):
                return True

            for end in range(start + 1, len(s) + 1):
                if end in seen:
                    continue

                if s[start:end] in words:
                    queue.append(end)
                    #seen.add(end)

        return False


s = Solution()
print(s.wordBreak('aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaab',
                  ["a","aa","aaa","aaaa","aaaaa","aaaaaa","aaaaaaa","aaaaaaaa","aaaaaaaaa","aaaaaaaaaa"]))
#print(s.wordBreak('catsandog', ["cats","dog","sand","and","cat"]))

#print(s.wordBreak('leetcode', ["leet","code"]))