class Solution:
    def countMatches(self, items: List[List[str]], ruleKey: str, ruleValue: str) -> int:
        t,c,n = [],[],[]
        for i in items:
            for j in i:
                if ruleKey == "type":
                    t.append(i[0])
                if ruleKey == "color":
                    c.append(i[1])
                if ruleKey == "name":
                    n.append(i[2])
        print(t)
        r = []
        if ruleKey == "type":
            l = t
        if ruleKey == "color":
            l = c
        if ruleKey == "name":
            l = n
        for k in range(0,len(l),3):
            if ruleKey == "type":
                r.append(t[k])
            if ruleKey == "color":
                r.append(c[k])
            if ruleKey == "name":
                r.append(n[k])
        print(r)
        return (r.count(ruleValue))
                    
                    
                    
                    
                    