class Solution(object):
    def minimumSum(self, n):
        """
        :type num: int
        :rtype: int
        """
        x = sorted(str(n))
        return int(x[0]+x[3]) + int(x[1]+x[2])
        