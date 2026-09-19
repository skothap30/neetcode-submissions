class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        n = len(numbers) - 1
        i = 0
        while i < n:
            curr = numbers[i] + numbers[n]

            if curr == target:
                return [i + 1, n + 1]
            elif curr < target:
                i += 1
            else:
                n -= 1
            
