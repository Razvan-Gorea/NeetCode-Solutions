class Solution:
    def maxArea(self, heights: List[int]) -> int:
        
        start = 0
        end = len(heights) - 1
        water_long = 0

        while start < end:
            water_short = min(heights[start], heights[end]) * (end - start)
            if heights[start] < heights[end]:
                start += 1
            else:
                end -= 1
            
            if water_short > water_long:
                water_long = water_short

        return water_long
