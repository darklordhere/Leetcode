class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        s = sorted(list(set(sentence)))
        alpha = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
        if alpha == s:
            return True
        return False