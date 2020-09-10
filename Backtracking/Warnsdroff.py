from heapq import heappush, heappop # for priority queue
import random
import string
n = 8 # width and height of the chessboard
board = [[0 for x in range(n)] for y in range(n)] # chessboard
# directions the Knight can move on the chessboard
dx = [-2, -1, 1, 2, -2, -1, 1, 2]
dy = [1, 2, 2, 1, -1, -2, -2, -1]
# start the Knight from a random position
row = 0
col = 0

for k in range(n * n):
    board[col][row] = k + 1
    pq = [] # priority queue of available neighbors
    for i in range(8):
        nx = row + dx[i]; ny = col + dy[i]
        if nx >= 0 and nx < n and ny >= 0 and ny < n:
            if board[ny][nx] == 0:
                # count the available neighbors of the neighbor
                ctr = 0
                for j in range(8):
                    ex = nx + dx[j]; ey = ny + dy[j]
                    if ex >= 0 and ex < n and ey >= 0 and ey < n:
                        if board[ey][ex] == 0: ctr += 1
                heappush(pq, (ctr, i))
    # move to the neighbor that has min number of available neighbors
    if len(pq) > 0:
        (p, m) = heappop(pq)
        row += dx[m]; col += dy[m]
        print(row,col)
    else: break

# print board
print(board)
# for cy in range(n):
#     for cx in range(n):
#         print (string.rjust(str(board[cy][cx]), 2),)
    # print
