import pygame
import random
import sys

# ---------------- SETTINGS ----------------
R, C = 20, 20
CELL = 25
WIDTH, HEIGHT = C * CELL, R * CELL
FPS = 60

# ---------------- WALL STRUCTURE ----------------
# 1 = wall exists, 0 = removed
northWall = [[1 for _ in range(C)] for _ in range(R)]
eastWall  = [[1 for _ in range(C)] for _ in range(R)]

visited = [[False for _ in range(C)] for _ in range(R)]

# ---------------- PYGAME SETUP ----------------
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Maze Generator + Solver")
clock = pygame.time.Clock()

# ---------------- DRAW MAZE ----------------
def draw_maze(path=[], dead=[]):
    screen.fill((255, 255, 255))

    for i in range(R):
        for j in range(C):
            x, y = j * CELL, i * CELL

            # north wall
            if northWall[i][j]:
                pygame.draw.line(screen, (0, 0, 0), (x, y), (x + CELL, y), 2)

            # east wall
            if eastWall[i][j]:
                pygame.draw.line(screen, (0, 0, 0), (x + CELL, y), (x + CELL, y + CELL), 2)

            # left boundary
            if j == 0:
                pygame.draw.line(screen, (0, 0, 0), (x, y), (x, y + CELL), 2)

            # bottom boundary
            if i == R - 1:
                pygame.draw.line(screen, (0, 0, 0), (x, y + CELL), (x + CELL, y + CELL), 2)

    # draw solver path
    for (i, j) in path:
        pygame.draw.rect(screen, (255, 0, 0), (j * CELL + 5, i * CELL + 5, CELL - 10, CELL - 10))

    for (i, j) in dead:
        pygame.draw.rect(screen, (0, 0, 255), (j * CELL + 8, i * CELL + 8, CELL - 16, CELL - 16))

    pygame.display.update()

# ---------------- MAZE GENERATION (DFS STACK MOUSE) ----------------
def generate_maze():
    stack = []

    ci, cj = random.randint(0, R - 1), random.randint(0, C - 1)
    visited[ci][cj] = True
    stack.append((ci, cj))

    while stack:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        i, j = stack[-1]

        neighbors = []

        # UP
        if i > 0 and not visited[i - 1][j]:
            neighbors.append((i - 1, j, "N"))

        # DOWN
        if i < R - 1 and not visited[i + 1][j]:
            neighbors.append((i + 1, j, "N_down"))

        # LEFT
        if j > 0 and not visited[i][j - 1]:
            neighbors.append((i, j - 1, "E_left"))

        # RIGHT
        if j < C - 1 and not visited[i][j + 1]:
            neighbors.append((i, j + 1, "E"))

        if neighbors:
            ni, nj, direction = random.choice(neighbors)
            visited[ni][nj] = True
            stack.append((ni, nj))

            # remove walls
            if direction == "N":
                northWall[i][j] = 0
            elif direction == "N_down":
                northWall[i + 1][j] = 0
            elif direction == "E":
                eastWall[i][j] = 0
            elif direction == "E_left":
                eastWall[i][j - 1] = 0

        else:
            stack.pop()

        draw_maze()
        clock.tick(FPS)

# ---------------- SOLVER (BACKTRACKING MOUSE) ----------------
def solve_maze(start, end):
    stack = [start]
    visited2 = [[False for _ in range(C)] for _ in range(R)]
    path = []
    dead = []

    while stack:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        i, j = stack[-1]
        visited2[i][j] = True
        path.append((i, j))

        if (i, j) == end:
            return path

        moved = False

        # try directions randomly
        dirs = [(1,0), (-1,0), (0,1), (0,-1)]
        random.shuffle(dirs)

        for di, dj in dirs:
            ni, nj = i + di, j + dj

            if 0 <= ni < R and 0 <= nj < C and not visited2[ni][nj]:

                # check walls
                if di == -1 and northWall[i][j] == 0:
                    stack.append((ni, nj))
                    moved = True
                    break
                elif di == 1 and northWall[i + 1][j] == 0:
                    stack.append((ni, nj))
                    moved = True
                    break
                elif dj == 1 and eastWall[i][j] == 0:
                    stack.append((ni, nj))
                    moved = True
                    break
                elif dj == -1 and eastWall[i][j - 1] == 0:
                    stack.append((ni, nj))
                    moved = True
                    break

        if not moved:
            dead.append(stack.pop())
            path.append(dead[-1])

        draw_maze(path, dead)
        clock.tick(FPS)

    return path

# ---------------- RANDOM START & END ----------------
def get_start_end():
    start = (0, random.randint(0, C - 1))
    end = (R - 1, random.randint(0, C - 1))
    return start, end

# ---------------- MAIN ----------------
def main():
    generate_maze()

    start, end = get_start_end()

    print("Start:", start, "End:", end)

    solve_maze(start, end)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return

        clock.tick(30)

if __name__ == "__main__":
    main()