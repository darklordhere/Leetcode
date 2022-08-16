class Solution:
    def interpret(self, command: str) -> str:
        c,s = command , ''
        for i in range(0,len(c)):
            if c[i] == 'G':
                s += 'G'
            elif c[i] == '('and c[i+1]==')':
                s += 'o'
            elif c[i] == '('and c[i+3]==')':
                s += 'al'
        return s