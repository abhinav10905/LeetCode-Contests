**QUESTION**
3963. Create Grid With Exactly One Path
You are given two integers m and n, representing the number of rows and columns of a grid.
Construct any m x n grid consisting only of the characters '.' and '#', where:
'.' represents a free cell.
'#' represents an obstacle cell.
A valid path is a sequence of free cells that:
Starts at the top-left cell (0, 0).
Ends at the bottom-right cell (m - 1, n - 1).
Moves only:
Right, from (i, j) to (i, j + 1), or
Down, from (i, j) to (i + 1, j).
Return any grid such that there is exactly one valid path from the top-left cell to the bottom-right cell.

**CONSTRAINTS**
1 <= m, n <= 25

**CODE**
class Solution:
    def createGrid(self, m: int, n: int) -> list[str]:
        a=[]
        i=0
        if n==1:
            return list("."*m)
        elif m==1:
            s="."
            a=""
            for i in range (n):
                a=a+s
            a=[a]
            return a
        else:
            a=[]
            g="#"
            s=".."
            for i in range (n-2):
                s=s+g
            a.append(s)
            g="#."
            s="#"
            for i in range (n-2):
                g=g+s
            z=g
            if z!="":
                for i in range (m-2):
                    a.append(z)
            s="#"
            for i in range (n-1):
                s=s+"."
            a.append(s)
            return a
            
**ABOUT MY CODE**
TIME :- O(n+m)
SPACE :- O(n+m)
APPROACH :- Array, String
                
        
        
            
        
        
