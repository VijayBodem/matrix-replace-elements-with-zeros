m,n = list(map(int,input().split()))
matrix = []
for i in range(m):
    num_list = list(map(int,input().split()))
    matrix.append(num_list)
for i in range(m):
    for j in range(n):
        if i != j and i+j+1 != n:
            matrix[i][j] = 0
for i in matrix:
    print(*i)
    
# 5 5
#4 3 7 6 4
#4 4 7 7 6
#9 5 8 5 9
#3 6 6 2 4
#3 7 4 4 3

#4 0 0 0 4
#0 4 0 7 0
#0 0 8 0 0
#0 6 0 2 0
#3 0 0 0 3