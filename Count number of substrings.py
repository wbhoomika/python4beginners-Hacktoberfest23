class Solution:
     def substrCount (self,s, k):
        last, ts = [-1]*26, []
        ans = 0
        for i, c in enumerate(s):
            v = ord(c)-97
            if last[v] >= 0: ts.remove(last[v])
            last[v] = i
            ts.append(i)
            M = len(ts)
            if M > k: ans += ts[-k] - ts[-k-1]
            elif M == k: ans += ts[0] + 1
        return ans
