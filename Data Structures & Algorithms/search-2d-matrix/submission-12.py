class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        size = [len(matrix),len(matrix[0])]
        print(size)
        if size == [1,1]:
            if matrix[0][0] == target:
                return True
            else:
                return False
        row_left = 0
        row_right = size[0]-1
        const_col = size[1]-1
        while row_left<=row_right:
            mid = (row_right+row_left) // 2
            print(mid)
            if target == matrix[mid][const_col]:
                return True
            elif matrix[mid][0] <= target <= matrix[mid][const_col]:
                row_left = mid
                break
            elif (target > matrix[mid][const_col]) and (row_left+1<= row_right):
                row_left = mid+1
            else:
                row_right = mid-1
        print("row left is:",row_left)
        left = 0
        right = size[1]-1
        while (left<=right):
            m = (left+right)//2
            if matrix[row_left][m] == target:
                return True
            elif matrix[row_left][m] < target:
                left = m+1
            else:
                right = m-1
        return False

        
        
