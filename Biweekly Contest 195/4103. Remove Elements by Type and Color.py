**QUESTION**
4103. Remove Elements by Type and Color
You are given three integer arrays types, colors, and groupSize, where types and colors have length n, and groupSize has length m.
types[i] represents the type of the element at index i.
colors[i] represents the color of the element at index i.
groupSize[t] represents the required number of elements in a removable group of type t.
In one operation, you may remove exactly groupSize[t] consecutive elements if all of them have type t and the same color.
After each removal, the remaining elements become adjacent again while maintaining their relative order.
Return true if it is possible to remove all elements using a sequence of valid operations. Otherwise, return false.
