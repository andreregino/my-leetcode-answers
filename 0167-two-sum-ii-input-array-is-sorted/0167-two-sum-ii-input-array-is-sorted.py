class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left_pointer = 0
        right_pointer = len(numbers) -1
        for i in numbers:
            if numbers[left_pointer] + numbers[right_pointer] == target:
                return [left_pointer+1, right_pointer+1]
            elif numbers[left_pointer] + numbers[right_pointer] < target:
                left_pointer += 1
            else:
                right_pointer -= 1
        