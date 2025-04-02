# Used two binary search algorithms which give a time complexity of O(logm + logn) = O(log(m*n))
# First algorithm searches if the target can be located in a certain row
# Second algorithm searches whether the target is in that certain row or not

class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        search_row = 0
        top = 0
        bottom = len(matrix) - 1

        while top <= bottom:
            mid = (top+bottom) // 2
            if matrix[mid][0] > target:
                bottom = mid - 1
            elif matrix[mid][len(matrix[0])-1] < target:
                top = mid + 1
            else:
                search_row = mid
                break
        
        l = 0
        r = len(matrix[0]) - 1

        while l <= r:
            m = (l+r)//2
            if matrix[search_row][m] > target:
                r = m-1
            elif matrix[search_row][m] < target:
                l = m+1
            else:
                return True
    
        return False
        
