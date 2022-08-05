class Solution:
    def strongPasswordCheckerII(self, password: str) -> bool:
        x = "!@#$%^&*()-+"
        p = password
        m,d,s,u,l = 0,0,0,0,0
        for j in range(len(p)):
            if (j < len(p)-1) and (p[j] == p[j+1]):
                m+=1
            elif p[j].isdigit():
                d+=1
            elif p[j].isupper():
                u += 1
            elif p[j].islower():
                l+=1
            elif p[j] in x:
                s+=1
        if m == 0 and d >= 1 and u >= 1 and s >= 1 and l >= 1 and len(p)>= 8:
            return True
        else:
            return False