class Solution:
    def isPalindrome(self, s: str) -> bool:
        c = ""
        for i in s:
            if i.isalnum() == True:
                c+=i.lower()
        return c == c[::-1]