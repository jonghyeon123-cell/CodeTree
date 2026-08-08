N = int(input())
grid = [list(map(int, input().split())) for i in range(N)]

count = 0
max = 0
for i in range(N - 2):
  for j in range(N - 2):
    if grid[i][j] == 1:
      count += 1
    if grid[i][j + 1] == 1:
      count += 1
    if grid[i][j + 2] == 1:
      count += 1
    if grid[i + 1][j] == 1:
      count += 1
    if grid[i + 1][j + 1] == 1:
      count += 1
    if grid[i + 1][j + 2] == 1:
      count += 1
    if grid[i + 2][j] == 1:
      count += 1
    if grid[i + 2][j + 1] == 1:
      count += 1
    if grid[i + 2][j + 2] == 1:
      count += 1
    if count >= max:
      max = count
    count = 0


print(max)