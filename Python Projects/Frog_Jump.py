# Title: 403. Frog Jump
# Difficulty: Hard
# Problem: https://leetcode.com/problems/frog-jump/description/

# using stack (highest efficiency)
class Solution:
    def canCross(self, stones: List[int]) -> bool:
        stone_set = set(stones)
        visited_set = set()
        stack = [(0, 0)]
        while stack:
            stone, jump = stack.pop()
            for j in [jump-1, jump, jump+1]:
                s = stone + j
                if j > 0 and s in stone_set and (s, j) not in visited_set:
                    if s == stones[-1]:
                        return True
                    stack.append((s, j))
            visited_set.add((stone, jump))
        return False

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
