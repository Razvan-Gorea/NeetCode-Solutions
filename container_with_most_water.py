class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left_pointer = 0
        right_pointer = len(heights) - 1
        max_area = 0

        while left_pointer < right_pointer:
            width = right_pointer - left_pointer
            height = min(heights[left_pointer], heights[right_pointer])
            area = width * height

            max_area = max(max_area, area)
            
            if heights[left_pointer] < heights[right_pointer]:
                left_pointer += 1
            else:
                right_pointer -= 1
        
        return max_area