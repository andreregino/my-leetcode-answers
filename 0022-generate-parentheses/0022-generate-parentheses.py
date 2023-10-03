class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        # global
        stack = []
        res = []

        def backtrack(valueOpen, valueClose):
            if valueOpen == valueClose == n:
                res.append("".join(stack)) 
                return
        
            if valueOpen < n:
                stack.append("(")
                backtrack(valueOpen + 1, valueClose)
                stack.pop()

            if valueClose < valueOpen:
                stack.append(")")
                backtrack(valueOpen, valueClose + 1)
                stack.pop()
            
        backtrack(0,0)
        return res