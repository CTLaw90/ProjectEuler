board = []
size_of_matrix = 20

n = size_of_matrix + 1

for i in range(n):
    board.append([1] * n)
    
for y in range (1,n):
    for x in range(1,n):
        board[y][x] = (board[y-1][x]) + (board[y][x-1])
        
num_steps = board[n-1][n-1]

#print board

print num_steps