class Solution:
    def makeEqual(self, words: List[str]) -> bool:
        j = ''.join(words)
        s = set(j)
        for i in s :
            if j.count(i) % len(words) != 0 : return False 
        return True