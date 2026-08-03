# 904 fruits into basket
# from collections import defaultdict

# class Solution:
#     def totalFruit(self, fruits: List[int]) -> int:
#         count = defaultdict(int)
#         left = 0
#         ans = 0

#         for right in range(len(fruits)):
#             count[fruits[right]] += 1

#             while len(count) > 2:
#                 count[fruits[left]] -= 1
#                 if count[fruits[left]] == 0:
#                     del count[fruits[left]]
#                 left += 1

#             ans = max(ans, right - left + 1)

#         return ans


# 3. Longest Substring Without Repeating Characters
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_set = set()
        left = 0
        max_length = 0
        
        for right in range(len(s)):
            # If a duplicate character is found, shrink the window from the left
            while s[right] in char_set:
                char_set.remove(s[left])
                left += 1
            
            # Add the current character to the set and update max length
            char_set.add(s[right])
            max_length = max(max_length, right - left + 1)
            
        return max_length
