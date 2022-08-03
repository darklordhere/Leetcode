class Solution:
    def decodeMessage(self, key: str, message: str) -> str:
        mapping = {}
        i = 0
        for char in key:
            if char!=' ' and char not in mapping:
                mapping[char] = chr(97+ i)
                i += 1
                
        res = ''
        
        for m in message:
            if m != ' ':
                res += mapping[m]
            else:
                res += ' '
        return res