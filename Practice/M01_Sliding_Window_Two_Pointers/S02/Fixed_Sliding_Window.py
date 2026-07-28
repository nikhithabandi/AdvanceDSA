# maximum average subarray 
class Solution:
    def findMaxAverage(nums: List[int], k: int) -> float:
        current_sum=sum(nums[:k])
        max_sum=current_sum
        for i in range(k,len(nums)):
            current_sum += nums[i] - nums[i-k]
            if current_sum>max_sum:
                max_sum=current_sum
        return max_sum/k
nums = [1,12,-5,-6,50,3]
k = 4
print(Solution.findMaxAverage(nums,k))

#number of subarrays of size k and average greater than or equal to threshold

class Solution:
    def numOfSubarrays(arr: List[int], k: int, threshold: int) -> int:
        win_sum = sum(arr[0:k])
        count = 0
        if(win_sum/k) >= threshold:
            count+=1
        n = len(arr)
        for i in range(n-k):
            win_sum = win_sum - arr[i] + arr[k+i]
            if (win_sum/k) >= threshold:
                count+=1
        return count