class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        a , b , c = ransomNote , magazine , 0
        for i in a:
            if a.count(i) <= b.count(i):
                c+=1
        return c == len(a)
            