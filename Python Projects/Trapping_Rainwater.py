# Title: 42. Trapping Rain Water
# Difficulty: Hard
# Problem: https://leetcode.com/problems/trapping-rain-water/description/

class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        if n == 0:
            return 0

        # Initialize left and right pointers
        left, right = 0, n - 1

        # Initialize variables to keep track of maximum heights from left and right sides
        left_max, right_max = 0, 0

        # Initialize variable to store the total trapped water
        total_water = 0

        # Main loop to process elements in the height list
        while left < right:
            # If height at the left pointer is smaller than height at the right pointer
            if height[left] < height[right]:
                # If the height at the left pointer is greater than or equal to the left_max
                if height[left] >= left_max:
                    # Update left_max to the current height
                    left_max = height[left]
                else:
                    # If the height at the left pointer is less than the left_max,
                    # there's a potential for water to be trapped.
                    # Add the trapped water to the total_water.
                    total_water += left_max - height[left]

                # Move the left pointer inward
                left += 1
            else:
                # If height at the right pointer is smaller than or equal to height at the left pointer
                # If the height at the right pointer is greater than or equal to the right_max
                if height[right] >= right_max:
                    # Update right_max to the current height
                    right_max = height[right]
                else:
                    # If the height at the right pointer is less than the right_max,
                    # there's a potential for water to be trapped.
                    # Add the trapped water to the total_water.
                    total_water += right_max - height[right]

                # Move the right pointer inward
                right -= 1

        # Return the total trapped water
        return total_water
