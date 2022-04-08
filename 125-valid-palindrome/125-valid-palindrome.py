class Solution:
    def isPalindrome(self, s: str) -> bool:
        res = [i for i in s.lower() if i.isalnum()]
        return all(res[i] == res[~i] for i in range(len(res) // 2 ))