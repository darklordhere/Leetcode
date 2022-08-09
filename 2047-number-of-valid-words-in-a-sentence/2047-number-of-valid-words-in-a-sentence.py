class Solution:
    def countValidWords(self, sentence: str) -> int:
        c = 0
        p = "^([a-z]+(-?[a-z]+)?)?(!|\.|,)?$"
        s = sentence.split()
        for i in s:
            r = re.match(p,i)
            if r:
                c += 1
        return c
            