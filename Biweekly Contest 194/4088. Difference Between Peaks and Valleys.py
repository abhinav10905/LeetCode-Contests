**QUESTION**
4088. Difference Between Peaks and Valleys
You are given an integer array nums of length n.
An index i is called a peak if all of the following conditions hold:
0 < i < n - 1
nums[i] > nums[i - 1]
nums[i] > nums[i + 1]
An index i is called a valley if all of the following conditions hold:
0 < i < n - 1
nums[i] < nums[i - 1]
nums[i] < nums[i + 1]
Return an integer denoting the difference between the sum of all peak values and the sum of all valley values.

**CONSTRAINTS**
3 <= n == nums.length <= 100
-100 <= nums[i] <= 100

**CODE**
class Solution:
    def peakValleyDifference(self, nums: list[int]) -> int:
        a=0
        b=0
        for i in range (1,len(nums)-1):
            if nums[i]<nums[i-1] and nums[i]<nums[i+1]:
                b+=nums[i]
            elif nums[i]>nums[i-1] and nums[i]>nums[i+1]:
                a+=nums[i]
        return a-b

**ABOUT MY CODE**
TIME :- O(n)
SPACE :- O(1)
APPROACH :- Array, Math
