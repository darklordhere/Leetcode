class Solution(object):
    def minimumMoves(self, s):
        return len(re.findall('X..', s + 'OO'))
        