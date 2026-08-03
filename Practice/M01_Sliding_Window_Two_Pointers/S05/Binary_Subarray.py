#1493 longest subarray of 1's after deleting one element
class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        left=0
        zeros=0
        ans=0
        for right in range(len(nums)):
            if nums[right]==0:
                zeros+=1
            while zeros>1:
                if nums[left]==0:
                    zeros-=1
                left+=1
            ans=max(ans,right-left)
        return ans


# 1004. Max Consecutive Ones III
class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        left=0
        zeros=0
        ans=0
        for right in range(len(nums)):
            if nums[right]==0:
                zeros+=1
            while zeros>k:
                if nums[left]==0:
                    zeros-=1
                left+=1
            ans=max(ans,right-left+1)
        return ans

# 930. Binary Subarrays With Sum