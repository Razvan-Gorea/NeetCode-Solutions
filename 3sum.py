class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        sorted_nums = sorted(nums)
        end = len(sorted_nums) - 1
        results = [] 
        
        i = 0
        while i < len(sorted_nums):
            start = i + 1
            end = len(sorted_nums) - 1
            if (i > 0) and (sorted_nums[i] == sorted_nums[i-1]):
                i += 1
            else:
                while start < end:
                    if sorted_nums[start] + sorted_nums[end] == -(sorted_nums[i]):
                        results.append([sorted_nums[i], sorted_nums[start], sorted_nums[end]])
                        start += 1
                        end -= 1
                        while start < end and sorted_nums[start] == sorted_nums[start - 1]:
                            start += 1
                        while start < end and sorted_nums[end] == sorted_nums[end + 1]:
                            end -= 1
                    elif sorted_nums[start] + sorted_nums[end] < -(sorted_nums[i]):
                        start += 1
                    else:
                        end -= 1
                i += 1

        return results
	# Time Compexity: N^2
	# Space Complexity: N
