class Solution:
    def judgeCircle(self, moves: str) -> bool:
        dict_moves = {
            "U":0,
            "D":0,
            "L":0,
            "R":0
        }

        for move in moves:
            dict_moves[move] = dict_moves[move] + 1
        
        if dict_moves["U"] == dict_moves["D"] and dict_moves["L"] == dict_moves["R"]:
            return True
        return False
        