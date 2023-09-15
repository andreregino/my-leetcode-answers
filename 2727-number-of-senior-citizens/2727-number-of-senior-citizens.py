class Solution:
    def countSeniors(self, details: List[str]) -> int:
        count_seniors = 0
        for detail in details:
            age = int(detail[11:13])
            #print(age)
            if age > 60:
                count_seniors+=1
        return count_seniors