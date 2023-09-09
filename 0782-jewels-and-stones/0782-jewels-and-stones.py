class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        jewels_dict = {"total" : 0}

        for jewel in jewels:
            jewels_dict[jewel] = 0
        
        for stone in stones:
            if stone in jewels_dict:
                jewels_dict["total"] = jewels_dict["total"] + 1
        
        return jewels_dict["total"]
