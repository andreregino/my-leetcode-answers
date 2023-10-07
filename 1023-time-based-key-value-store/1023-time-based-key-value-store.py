class TimeMap:

    def __init__(self):
       
        self.timebased = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if not key in self.timebased:
            self.timebased[key] = []
        self.timebased[key].append([value, timestamp])

    def get(self, key: str, timestamp: int) -> str:
        val = self.timebased.get(key, [])
        res = ""
        l = 0
        r = len(val) - 1

        while l <= r:
            m = (l + r) // 2
            if timestamp >= val[m][1]:
                res = val[m][0]
                l = m+1
            else:
                r = m-1
        return res


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)