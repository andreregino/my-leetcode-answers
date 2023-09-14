class Solution:
    def squareIsWhite(self, coordinates: str) -> bool:
        white = ["b", "d", "f", "h"]
        coordinate = list(coordinates)
        if ((int(coordinate[1]) % 2 == 0) and (coordinate[0] not in white)) \
        or ((int(coordinate[1]) % 2 == 1) and (coordinate[0] in white)):
            return True
        else:
            return False
         
        