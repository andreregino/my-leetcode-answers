class Solution:
    def removeTrailingZeros(self, num: str) -> str:
        flag = True
        while flag:
            if num[-1] == "0":
                num = num[:-1]
            else:
                flag = False

        return num