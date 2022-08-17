class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        a=[".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        b="abcdefghijklmnopqrstuvwxyz"
        b,d,temp=list(b) , dict(zip(b,a)) , []
        for i in words:
            t=""
            for j in i:
                x=d[j]
                t+=x
            if t not in temp:
                temp.append(t)
        return (len(temp))