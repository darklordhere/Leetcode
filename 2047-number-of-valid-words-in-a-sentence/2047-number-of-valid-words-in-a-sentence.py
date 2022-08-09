class Solution:
    def countValidWords(self, sentence: str) -> int:
        c,p,s = 0 , "^([a-z]+(-?[a-z]+)?)?(!|\.|,)?$" , sentence.split()
        for i in s:
            r = re.match(p,i)
            if r:
                c += 1
        return c
            