class Solution:
    def asteroidCollision(self, ast: List[int]) -> List[int]:
        s = []
        for a in ast:
            while s and a < 0 < (b := s[-1]):
                if b <= -a: s.pop()
                if b >= -a: 
                    break
            else: s.append(a)
        return s