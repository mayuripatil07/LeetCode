n = len(mat)
        m = len(mat[0])
        value = []
        for row in range(n):
            for col in range(m):
                val = []
                i = row
                j = col
                while(i < n and j < m):
                    val.append(mat[i][j])
                    i += 1
                    j += 1
                val.sort()
                i -= 1
                j -= 1
                while(len(val) > 0):
                    mat[i][j] = val.pop()
                    i -= 1
                    j -= 1
        return mat
