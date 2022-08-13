class Solution:
    def squareIsWhite(self, coordinates: str) -> bool:
        c,a,b = coordinates , "aceg" , "bdfh"
        for i in range(0,len(c)):
            if (( c[0] in a ) and ( int(c[1])%2 != 0 )) or (( c[0] in b ) and ( int(c[1])%2 == 0 )):
                return False
        return True