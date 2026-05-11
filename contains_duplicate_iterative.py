class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        holder = set()
        for num in nums:
            if num in holder:
                return True
            else:
                holder.add(num)
        return False
