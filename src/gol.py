from copy import deepcopy

def get_state(cells, x, y):
    summed = 0
    x_max = len(cells[0]) - 1
    y_max = len(cells) - 1

    if (y > 0): #top
        summed += int(cells[y - 1][x])
    if (x < x_max and y > 0): #top right
        summed += int(cells[y - 1][x + 1])
    if (x < x_max): #right
        summed += int(cells[y][x + 1])
    if (x < x_max and y < y_max): #bottom right
        summed += int(cells[y + 1][x + 1])
    if (y < y_max): #bottom
        summed += int(cells[y + 1][x])
    if (x > 0 and y < y_max): #bottom left
        summed += int(cells[y + 1][x - 1])
    if (x > 0): #left
        summed += int(cells[y][x - 1])
    if (x > 0 and y > 0): #top left
        summed += int(cells[y - 1][x - 1])

    if (summed == 3):
        return 1
    elif (summed == 2):
        return cells[y][x]
    return 0

def get_next_gen(cells):
    dest = deepcopy(cells)

    for y in range(len(dest)):
        for x in range(len(dest[y])):
            dest[y][x] = get_state(cells, x, y)
    return dest
