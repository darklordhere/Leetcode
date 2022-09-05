class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        fresh, rotten = set(), set()
        time = 0
        for row in range(len(grid)): 
            for col in range(len(grid[0])): 
                if grid[row][col] == 1: 
                    fresh.add((row, col)) # collect fresh oranges
                if grid[row][col] == 2: 
                    rotten.add((row, col)) # collect rotten oranges
                    
        while fresh:
            rotting = set() 
            for i, j in fresh: 
                if (i-1, j) in rotten or (i+1, j) in rotten or (i, j-1) in rotten or (i, j+1) in rotten: # If any of the neighbors is rotten, then this fresh orange is going to rot
                    rotting.add((i,j))
            if not rotting: return -1 # If no orange rotted during this minute return -1
            fresh -= rotting # remove oranges that just rotted from fresh group
            rotten |= rotting # add oranges that just rotted to rotten group
            time += 1 # Count 1 minute
        return time