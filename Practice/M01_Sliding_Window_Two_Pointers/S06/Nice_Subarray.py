# 1248 count number of nice subarrays
class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int):
        freq = {0: 1}
        odd_count = 0
        ans = 0

        for num in nums:
            if num % 2 == 1:
                odd_count += 1

            ans += freq.get(odd_count - k, 0)
            freq[odd_count] = freq.get(odd_count, 0) + 1

        return ans

# 1763 longest nice subarray
class Solution:
    def longestNiceSubstring(self, s: str) -> str:
        if len(s)<2:
            return ""
        unique = set(s)
        for i,ch in enumerate(s):
            if ch.lower() in unique and ch.upper() in unique:
                continue
            left_str=self.longestNiceSubstring(s[:i])
            right_str=self.longestNiceSubstring(s[i+1:])
            return left_str if len(left_str)>=len(right_str) else right_str
        return s