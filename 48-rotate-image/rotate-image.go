func rotate(matrix [][]int)  {
    N := len(matrix)

    for i:= 0; i < N/2; i++{
        for j:= 0;j < (N + 1)/ 2; j ++{
            matrix[i][j], matrix[j][N-i-1], matrix[N-i-1][N-j-1], matrix[N-j-1][i] = matrix[N-j-1][i], matrix[i][j], matrix[j][N-i-1], matrix[N-i-1][N-j-1]
        }
    }
}