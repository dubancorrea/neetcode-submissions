class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left = 0
        right = len(heights) - 1
        max_water = 0

        while left < right:  # range until the pointer meet
            width = right - left # distance between two bars
            shorter = min(heights[left], heights[right])  # water level is limited by the shorter bar
            area = width * shorter   # area of water this pais of bars can hold
            max_water = max(max_water, area) # update best if this one is bigger

            if heights[left] < heights[right]: #shorter size is limiting, if left or right heights are not equal increase left or decrease right
                left += 1
            else:
                right -= 1

        return max_water



        