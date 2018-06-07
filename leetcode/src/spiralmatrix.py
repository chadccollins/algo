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
        result = []

        # kick out any garbage
        if matrix == []:
            return result

        # first, maybe figure out our dimensions
        left = 0
        right = len(matrix[0]) - 1
        top = 0
        bottom = len(matrix) - 1

        while left <= right and top <= bottom:
            # do a loop around the spiral
            # left to right
            for r in range(left, right + 1):
                result.append(matrix[top][r])
            # top to bottom 
            for d in range(top + 1, bottom):
                result.append(matrix[d][right])
            # right to left
            # as long as top < bottom, we still have a row to consume, if top == bottom, there is no row left
            if top < bottom:
                for l in reversed(range(left, right + 1)):
                    result.append(matrix[bottom][l])
            # bottom to top (+1 so we stop just short of overlap) 
            # same thing here, if left < right, there is a column left to consume, but if left == right, there's nothing left
            if left < right:
                for u in reversed(range(top + 1, bottom)):
                    result.append(matrix[u][left])

            # now that we've completed a loop, shink our boundries  
            left += 1
            right -= 1
            top += 1
            bottom -= 1

        return result

print (Solution().spiralOrder([[ 1, 2, 3 ],
                                  [ 4, 5, 6 ],
                                  [ 7, 8, 9 ]]))

print (Solution().spiralOrder([[2,3]]))