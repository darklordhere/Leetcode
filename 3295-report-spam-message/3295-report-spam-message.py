class Solution:
    def reportSpam(self, message: List[str], bannedWords: List[str]) -> bool:
        c = 0
        d = Counter(bannedWords)
        for i in message:
            if d.get(i,0) != 0:
                c += 1
        return c >= 2