class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.strip()
        if s == "": return 0
        else:
            i = 0 ; pn = 1 ; r = 0
            if s[i] == "+": i += 1
            elif s[i] == "-": i += 1;pn = -1
            while i < len(s) and s[i].isdigit(): r = r * 10 + int(s[i]) ; i += 1
            r *= pn;r = max(min(r,2**31-1),-2**31);return r
        
                
                    