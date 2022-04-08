class Solution:
    def isPalindrome(self, x: int) -> bool:
        if ( x < 0 or ( x != 0 and x%10 == 0 )):
            return False
        c = 0
        while x > c:
            m = x % 10
            c = c*10 + m
            x = x//10
        if (x == c or x == c//10):
            return True