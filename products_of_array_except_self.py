class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = 1
        suffix = 1
        results = []
        
        i = 0
        while i < len(nums):
            results.append(prefix)
            prefix = prefix * nums[i]
            i += 1

        i = len(nums) - 1
        while i > -1:
            results[i] *= suffix
            suffix = suffix * nums[i]
            i -= 1
        
        return results
