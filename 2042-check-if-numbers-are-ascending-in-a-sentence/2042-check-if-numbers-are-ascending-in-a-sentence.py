class Solution:
    def areNumbersAscending(self, s: str) -> bool:
        x = s.split(' ')
        l = []
        for i in x:
            if i.isdigit():
                l.append(int(i))
        for j in range(1,len(l)):
            if l[j] == l[j-1]:
                return False
            if l[j] < l[j-1]:
                return False
        return True
            