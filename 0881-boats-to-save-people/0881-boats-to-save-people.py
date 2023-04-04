class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        c = 0
        h = len(people)-1
        boats = 0
        while c <= h:
            if people[c] + people[h] <= limit:
                c += 1 ; h -= 1
            else:
                h -= 1
            boats += 1
        return boats