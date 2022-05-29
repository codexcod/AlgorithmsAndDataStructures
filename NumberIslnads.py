def callBFS(map, x, y):
    if (x < 0 or x >= len(map) or y < 0 or y >= len(map)) or map[x][y] == 0:
        return

    map[x][y] = 0
    callBFS(map, x + 1, y)
    callBFS(map, x - 1, y)
    callBFS(map, x, y + 1)
    callBFS(map, x, y - 1)


def countIslands(map):
    count = 0
    for x in range(len(map)):
        for y in range(len(map[x])):
            if map[x][y] == 1:
                count += 1
                callBFS(map, x, y)

    return count


map = [[0, 0, 0, 1, 1],
       [1, 0, 0, 1, 1],
       [0, 0, 0, 0, 0],
       [1, 0, 0, 1, 1],
       [0, 0, 0, 1, 1]]

print(countIslands(map))
