class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numbers_seen = {}
        for index, val in enumerate(nums):
            result = target - val
            if result in numbers_seen:
                return [numbers_seen[result], index]
            else:
                numbers_seen[val] = index 
                
