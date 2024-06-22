from collections import deque
n, m = map(int, input().split())
desk = []
new_desk = [[10**10] * m for _ in range(n)]
visited = [[0] * m for _ in range(n)]
for i in range(n):
    desk.append(list(map(int, input().split())))
points = []
for i in range(n):
    for j in range(m):
        if desk[i][j]:
            points.append([i, j])
def on_board(x, y):
    return x > -1 and x < n and y > -1 and y < m
def bfs(points, visited, new_desk):
    queue = deque()
    for x, y in points:
        visited[x][y] = 1
        new_desk[x][y] = 0
        queue.append((x, y))
    dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if on_board(nx, ny) and not visited[nx][ny]:
                queue.append((nx, ny))
                visited[nx][ny] = 1
                new_desk[nx][ny] = min(new_desk[nx][ny], new_desk[x][y] + 1)
    return


bfs(points, visited, new_desk)
               
for i in range(n):
    print(' '.join(str(j) for j in new_desk[i]))