**QUESTION**
4048. Count Values With Equally Spaced Occurrences I
You are given an integer array nums.
An integer x is called special if:
x appears exactly three times in nums.
All three occurrences of x are equally spaced in nums. In other words, if all occurrences of x are at indices i1 < i2 < i3, then i2 - i1 = i3 - i2.
Return the number of distinct special integers in nums.

**CONSTRAINTS**
3 <= nums.length <= 100
1 <= nums[i] <= 100

**CODE**
class Solution:
    def countSpecialIntegers(self, nums: list[int]) -> int:
        hash={}
        c=0
        for i in range (0,len(nums)):
            if nums[i] in hash:
                hash[nums[i]].append(i)
            else:
                hash[nums[i]]=[i]
        for i in hash:
            if len(hash[i])==3:
                if hash[i][1]-hash[i][0]==hash[i][2]-hash[i][1]:
                    c+=1
        return c

**ABOUT MY CODE**
TIME :- O(n)
SPACE :- O(n)
APPROACH :- Array, Hash Map
