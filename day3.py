import sys

board = [[0 for i in range(1000)] for j in range(1000)]
overlap = [False for i in range(1306)]

count = 0
for line in sys.stdin:
    line = line.split()
    identity = int(line[0][1:])
    x, y = map(int, line[2][:-1].split(','))
    width, length = map(int, line[3].split('x'))
    for i in range(x+1, x+width+1):
        for j in range(y+1, y+length+1):
            if board[i][j] != 0:
                count += 1
                overlap[board[i][j]] = True
                overlap[identity] = True
            else:
                board[i][j] = identity
print("Overlapping Area:", count)

for i in range(len(overlap)):
    if not overlap[i]:
        print(i, "does not overlap")
