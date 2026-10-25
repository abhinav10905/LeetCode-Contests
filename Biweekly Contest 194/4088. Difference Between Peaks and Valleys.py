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
