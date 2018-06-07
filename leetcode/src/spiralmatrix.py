#   Given a matrix of m x n elements (m rows, n columns), return all elements of the matrix in spiral order.
#   Input:
#   [
#    [ 1, 2, 3 ],
#    [ 4, 5, 6 ],
#    [ 7, 8, 9 ]
#   ]
#   Output: [1,2,3,6,9,8,7,4,5]

class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        # kick out any garbage
        if matrix == []:
            return

        # first, maybe figure out our dimensions
        left = 0
        right = len(matrix[0]) - 1
        top = 0
        bottom = len(matrix) - 1

        result = []

        while left <= right and top <= bottom:
            for r in range(left, right):
                result.append(matrix[top][r])
            
            for d in range(top + 1, bottom):
                result.append(matrix[d][right])

            for l in reversed(range(right, bottom)):
                result.append(matrix[bottom][l])
            
            for u in reversed(range(top + 1, bottom)):
                result.append(matrix[u][left])
            
            left += 1
            right -= 1
            top += 1
            bottom -= 1

        return result



print (Solution().spiralOrder([[ 1, 2, 3 ],
                                  [ 4, 5, 6 ],
                                  [ 7, 8, 9 ]]))
print (Solution().spiralOrder([[2,3]]))