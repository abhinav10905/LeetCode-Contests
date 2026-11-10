**QUESTION**
4103. Remove Elements by Type and Color
You are given three integer arrays types, colors, and groupSize, where types and colors have length n, and groupSize has length m.
types[i] represents the type of the element at index i.
colors[i] represents the color of the element at index i.
groupSize[t] represents the required number of elements in a removable group of type t.
In one operation, you may remove exactly groupSize[t] consecutive elements if all of them have type t and the same color.
After each removal, the remaining elements become adjacent again while maintaining their relative order.
Return true if it is possible to remove all elements using a sequence of valid operations. Otherwise, return false.

**CONNSTRAINTS**
1 <= n == types.length == colors.length <= 105
1 <= m == groupSize.length <= 105
0 <= types[i] <= m - 1
1 <= colors[i] <= 105
1 <= groupSize[t] <= n

**CODE**
class Solution:
    def canRemoveAll(self, types: list[int], colors: list[int], groupSize: list[int]) -> bool:
        stack=[]
        for i in range (0,len(types)):
            if stack!=[] and stack[-1][0]==types[i] and stack[-1][1]==colors[i]:
                stack[-1][2]+=1
            else:
                stack.append([types[i],colors[i],1])
            if stack[-1][2]==groupSize[types[i]]:
                a=stack.pop()
        if stack==[]:
            return True
        else:
            return False

**ABOUT MY CODE**
TIME :- O(n)
SPACE :- O(n)
APPROACH :- Stack
            
        
