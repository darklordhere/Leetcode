class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        l = []
        for i in words:
            for j in words:
                if i == j:
                    continue
                if i in j:
                    l.append(i)
                    break
        return l
        