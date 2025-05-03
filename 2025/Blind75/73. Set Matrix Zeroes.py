class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        # for i in range(len(matrix)):
        #     for j in range(len(matrix[0])):
        #         if matrix[i][j] == 0:
        #             for s in range(len(matrix[0])):
        #                 if matrix[i][s] != 0:
        #                     matrix[i][s] = '#'
        #             for t in range(len(matrix)):
        #                 if matrix[t][j] != 0:
        #                     matrix[t][j] = '#'
        # for i in range(len(matrix)):
        #     for j in range(len(matrix[0])):
        #         if matrix[i][j] == '#':
        #             matrix[i][j] = 0
        # return matrix

        #better solution, 只使用第一行第一列标记
        # 第一行第一列要另外处理
        first_row_zero = any(matrix[0][j] == 0 for j in range(len(matrix[0])))
        first_col_zero = any(matrix[i][0] == 0 for i in range(len(matrix)))
        for i in range(1, len(matrix)):
            for j in range(1, len(matrix[0])):
                if matrix[i][j] == 0:
                    matrix[0][j] = 0
                    matrix[i][0] = 0

        for i in range(1, len(matrix)):
            if matrix[i][0] == 0:
                for s in range(1, len(matrix[0])):
                    matrix[i][s] = 0
        for j in range(1, len(matrix[0])):
            if matrix[0][j] == 0:
                for t in range(1, len(matrix)):
                    matrix[t][j] = 0
        # 最后处理第一行和第一列
        if first_row_zero:
            for j in range(len(matrix[0])):
                matrix[0][j] = 0
        if first_col_zero:
            for i in range(len(matrix)):
                matrix[i][0] = 0