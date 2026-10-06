class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        # Helps with making sure there are no duplicates
        nums.sort()
        for i, a in enumerate(nums):
            # Checks if the element before is the same as the current one, if true, then skip
            if i > 0 and a == nums[i - 1]:
                continue
            # Left starts at the element one after index i
            # Right starts at the last element of the list
            l, r = i + 1, len(nums) - 1

            while l < r:
                threeSum = a + nums[l] + nums[r]
                if threeSum > 0:
                    r -= 1
                elif threeSum < 0:
                    l += 1
                else:
                    res.append([a, nums[l], nums[r]])
                    # Moves the left pointer forward for the next iteration of threeSum
                    l += 1
                    # Check if the before element is the same as the current left element, if so keep iterating until it is not
                    while nums[l] == nums[l - 1] and l < r:
                        l += 1
        return res
        
