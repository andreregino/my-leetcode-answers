class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        final_list = []
        for i in range (n):
            if (i+1) % 15 == 0:
                final_list.append("FizzBuzz")
            elif (i+1) % 3 == 0:
                final_list.append("Fizz")
            elif (i+1) % 5 == 0:
                final_list.append("Buzz")
            else:
                final_list.append(str(i+1))

        return final_list