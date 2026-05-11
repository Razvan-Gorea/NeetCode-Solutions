class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        number_counts = {}
        
        for num in nums:
            if num in number_counts:
                number_counts[num] += 1
            else:
                number_counts[num] = 1

        numbers_and_counts = sorted(number_counts.items(), key=lambda x: x[1],  reverse=True)
        
        numbers = [x[0] for x in numbers_and_counts]
        
        return numbers[:k]
        
