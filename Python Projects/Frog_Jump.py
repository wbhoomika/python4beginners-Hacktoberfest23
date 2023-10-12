# Title: 403. Frog Jump
# Difficulty: Hard
# Problem: https://leetcode.com/problems/frog-jump/description/
from typing import List

# using stack (highest efficiency)
class Solution:
    def canCross(self, stones: List[int]) -> bool:
        n = len(stones)
        dp = {}  # Use a dictionary to store valid jumps for each stone

        for stone in stones:
            dp[stone] = set()

        dp[0].add(0)  # The first stone can only be reached with a jump of size 0

        for i in range(n):
            for j in dp[stones[i]]:
                for step in range(j - 1, j + 2):  # Next jump size could be j-1, j, or j+1
                    if step > 0 and stones[i] + step in dp:
                        dp[stones[i] + step].add(step)

        return len(dp[stones[-1]]) > 0


# using dp (low efficiency)
class Solution:
    def canCross(self, stones: List[int]) -> bool:
        n = len(stones)
        dp = [set() for _ in range(n)]
        dp[0].add(0)  # The first stone can only be reached with a jump of size 0

        for i in range(n):
            for j in dp[i]:
                for step in range(j - 1, j + 2):  # Next jump size could be j-1, j, or j+1
                    if step > 0 and stones[i] + step in stones:
                        next_idx = stones.index(stones[i] + step)
                        dp[next_idx].add(step)

        return len(dp[-1]) > 0
