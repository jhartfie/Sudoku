import pygame
from random import randint, shuffle

pygame.init()
pygame.display.set_caption("Sudoku")
font1 = pygame.font.SysFont("comicsans", 40)
btn = pygame.font.SysFont("arial", 15, bold=True)

black = (0, 0, 0)
white = (255, 255, 255)
height = 600
width = 500
screen = pygame.display.set_mode((width, height))
x = 0
y = 0
val = 0

grid = [
    [7, 8, 0, 4, 0, 0, 1, 2, 0],
    [6, 0, 0, 0, 7, 5, 0, 0, 9],
    [0, 0, 0, 6, 0, 1, 0, 7, 8],
    [0, 0, 7, 0, 4, 0, 2, 6, 0],
    [0, 0, 1, 0, 5, 0, 9, 3, 0],
    [9, 0, 4, 0, 6, 0, 0, 0, 5],
    [0, 7, 0, 3, 0, 0, 0, 1, 2],
    [1, 2, 0, 0, 0, 7, 4, 0, 0],
    [0, 4, 9, 2, 0, 6, 0, 0, 7]
]

rows = len(grid)  # 9
columns = len(grid[0])  # 9
dif = width / rows  # 500 / 9 = 55.5


def draw_box():
    for i in range(2):
        pygame.draw.line(screen, (127, 255, 0), (x * dif - 3, (y + i) * dif), (x * dif + dif + 3, (y + i) * dif), 7)
        pygame.draw.line(screen, (127, 255, 0), ((x + i) * dif, y * dif), ((x + i) * dif, y * dif + dif), 7)


def draw():
    for i in range(9):
        for j in range(0, 9):
            if grid[i][j] != 0:
                pygame.draw.rect(screen, (0, 255, 255), (i * dif, j * dif, dif + 1, dif + 1))
                text1 = font1.render(str(grid[i][j]), 1, black)
                screen.blit(text1, (i * dif + 15, j * dif + 15))
            else:
                continue
    for i in range(10):
        if i % 3 == 0:
            thick = 7
        else:
            thick = 1
        pygame.draw.line(screen, black, (0, i * dif), (500, i * dif), thick)
        pygame.draw.line(screen, black, (i * dif, 0), (i * dif, 500), thick)


def valid(m, i, j, val):
    for it in range(9):
        if m[i][it] == val:
            return False
        if m[it][j] == val:
            return False
    it = i // 3
    jt = j // 3
    for i in range(it * 3, it * 3 + 3):
        for j in range(jt * 3, jt * 3 + 3):
            if m[i][j] == val:
                return False
    return True


def solve(grid, i, j):
    while grid[i][j] != 0:
        if i < 8:
            i += 1
        elif i == 8 and j < 8:
            i = 0
            j += 1
        elif i == 8 and j == 8:
            return True
    pygame.event.pump()
    for it in range(1, 10):
        if valid(grid, i, j, it):
            grid[i][j] = it
            global x, y
            x = i
            y = j
            screen.fill(white)
            draw()
            draw_box()
            pygame.display.update()
            pygame.time.delay(20)
            if solve(grid, i, j) == 1:
                if fullgridtest():
                    return True
            else:
                grid[i][j] = 0
            screen.fill(white)

            draw()
            draw_box()
            pygame.display.update()
            pygame.time.delay(50)
    return False


def fullgridtest():
    global grid
    for row in range(9):
        for col in range(9):
            if grid[row][col] == 0:
                return False
    return True


def randomize():
    clear()
    global grid
    numberList = [1, 2, 3, 4, 5, 6, 7, 8, 9]

    def fillGrid():
        global grid
        for i in range(0, 81):
            row = i // 9
            col = i % 9
            if grid[row][col] == 0:
                shuffle(numberList)
                for value in numberList:
                    if not (value in grid[row]):
                        if not value in (
                                grid[0][col],
                                grid[1][col],
                                grid[2][col],
                                grid[3][col],
                                grid[4][col],
                                grid[5][col],
                                grid[6][col],
                                grid[7][col],
                                grid[8][col]):
                            square = []
                            if row < 3:
                                if col < 3:
                                    square = [grid[i][0:3] for i in range(0, 3)]
                                elif col < 6:
                                    square = [grid[i][3:6] for i in range(0, 3)]
                                else:
                                    square = [grid[i][6:9] for i in range(0, 3)]
                            elif row < 6:
                                if col < 3:
                                    square = [grid[i][0:3] for i in range(3, 6)]
                                elif col < 6:
                                    square = [grid[i][3:6] for i in range(3, 6)]
                                else:
                                    square = [grid[i][6:9] for i in range(3, 6)]
                            else:
                                if col < 3:
                                    square = [grid[i][0:3] for i in range(6, 9)]
                                elif col < 6:
                                    square = [grid[i][3:6] for i in range(6, 9)]
                                else:
                                    square = [grid[i][6:9] for i in range(6, 9)]
                            if not value in (square[0] + square[1] + square[2]):
                                grid[row][col] = value
                                if fullgridtest():
                                    return True
                                else:
                                    if fillGrid():
                                        return True
                break
        grid[row][col] = 0

    fillGrid()

    numOfDeleted = 0
    while numOfDeleted < 40:
        row = randint(0, 8)
        col = randint(0, 8)
        if grid[row][col] != 0:
            grid[row][col] = 0
            numOfDeleted += 1


def clear():
    global grid
    grid = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0]
    ]


def reset():
    global grid
    grid = [
        [7, 8, 0, 4, 0, 0, 1, 2, 0],
        [6, 0, 0, 0, 7, 5, 0, 0, 9],
        [0, 0, 0, 6, 0, 1, 0, 7, 8],
        [0, 0, 7, 0, 4, 0, 2, 6, 0],
        [0, 0, 1, 0, 5, 0, 9, 3, 0],
        [9, 0, 4, 0, 6, 0, 0, 0, 5],
        [0, 7, 0, 3, 0, 0, 0, 1, 2],
        [1, 2, 0, 0, 0, 7, 4, 0, 0],
        [0, 4, 9, 2, 0, 6, 0, 0, 7]
    ]


def main():
    global grid
    run = True
    while run:
        screen.fill(white)

        solvebtn = pygame.Rect(20, 525, 100, 50)  # (left, top, width, height)
        solvetext = btn.render("Solve", True, white)
        solverect = solvetext.get_rect()
        solverect.center = solvebtn.center
        pygame.draw.rect(screen, black, solvebtn)
        screen.blit(solvetext, solverect)

        randombtn = pygame.Rect(140, 525, 100, 50)  # (left, top, width, height)
        randomtext = btn.render("Randomize", True, white)
        randomrect = randomtext.get_rect()
        randomrect.center = randombtn.center
        pygame.draw.rect(screen, black, randombtn)
        screen.blit(randomtext, randomrect)

        clearbtn = pygame.Rect(260, 525, 100, 50)  # (left, top, width, height)
        cleartext = btn.render("Clear", True, white)
        clearrect = cleartext.get_rect()
        clearrect.center = clearbtn.center
        pygame.draw.rect(screen, black, clearbtn)
        screen.blit(cleartext, clearrect)

        resetbtn = pygame.Rect(380, 525, 100, 50)  # (left, top, width, height)
        resettext = btn.render("Reset", True, white)
        resetrect = resettext.get_rect()
        resetrect.center = resetbtn.center
        pygame.draw.rect(screen, black, resetbtn)
        screen.blit(resettext, resetrect)
        draw()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            click, _, _ = pygame.mouse.get_pressed()
            if click == 1:
                mouse = pygame.mouse.get_pos()
                if randombtn.collidepoint(mouse):
                    randomize()
                if solvebtn.collidepoint(mouse):
                    solve(grid, 0, 0)
                if clearbtn.collidepoint(mouse):
                    clear()
                if resetbtn.collidepoint(mouse):
                    reset()
        pygame.display.update()

    pygame.quit()


main()
