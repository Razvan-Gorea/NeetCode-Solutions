class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        set_of_nums = set(nums)

        longest_length = 0
        for num in set_of_nums:
            if num - 1 not in set_of_nums:
                
                current_length = 1
                
                while num + 1 in set_of_nums:
                    current_length += 1
                    num = num + 1
                
                if current_length > longest_length:
                    longest_length = current_length
        
        return longest_length

        # Time complexity: N
        # Space complexity: N
