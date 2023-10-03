# https://leetcode.com/problems/number-of-good-pairs/

"""
Given an array of integers nums, return the number of good pairs.

A pair (i, j) is called good if nums[i] == nums[j] and i < j.

 

Example 1:

Input: nums = [1,2,3,1,1,3]
Output: 4
Explanation: There are 4 good pairs (0,3), (0,4), (3,4), (2,5) 0-indexed.
Example 2:

Input: nums = [1,1,1,1]
Output: 6
Explanation: Each pair in the array are good.
Example 3:

Input: nums = [1,2,3]
Output: 0
 

Constraints:

1 <= nums.length <= 100
1 <= nums[i] <= 100
"""
# CODE

class Solution:
    def numIdenticalPairs(self, nums):
        # Create a dictionary to store the count of each number
        num_count = {}
        
        # Initialize the answer variable
        ans = 0
        
        # Iterate through the given array 'nums'
        for num in nums:
            # Check if the number already exists in the dictionary
            if num in num_count:
                # If it exists, add the current count to the answer
                ans += num_count[num]
            
            # Update the count of the current number in the dictionary
            num_count[num] = num_count.get(num, 0) + 1
        
        # Return the final answer
        return ans
