import pygame
import heapq
import random
import itertools

# Constants for game setup and appearance
GRID_SIZE = 20
CELL_SIZE = 30
WINDOW_SIZE = GRID_SIZE * CELL_SIZE

# Color definitions for game elements
PLAYER_COLOR = (0, 0, 255)
TREASURE_COLOR = (128, 0, 128)
OBSTACLE_COLOR = (0, 0, 0)
DAMAGE_COLOR = (255, 0, 0)
GOLD_COLOR = (255, 255, 0)
BACKGROUND_COLOR = (255, 255, 255)
BUTTON_COLOR = (0, 128, 0)
BUTTON_HOVER_COLOR = (0, 255, 0)
TEXT_COLOR = (255, 255, 255)

# Player attributes
PLAYER_HP = 100
PLAYER_GOLD = 10
FPS = 7

# Initialize Pygame
pygame.init()
screen = pygame.display.set_mode((WINDOW_SIZE, WINDOW_SIZE))
pygame.display.set_caption("AI Maze: Hunt for treasures")
clock = pygame.time.Clock()

# Heuristic function for A* algorithm
def heuristic(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

# A* search algorithm for pathfinding
def a_star_search(grid, start, goal):
    open_list = []
    heapq.heappush(open_list, (0, start))
    came_from = {}
    cost_so_far = {start: 0}

    while open_list:
        _, current = heapq.heappop(open_list)

        if current == goal:
            break

        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            next_cell = (current[0] + dx, current[1] + dy)
            if 0 <= next_cell[0] < GRID_SIZE and 0 <= next_cell[1] < GRID_SIZE:
                if grid[next_cell[1]][next_cell[0]] != "O":
                    new_cost = cost_so_far[current] + 1
                    if next_cell not in cost_so_far or new_cost < cost_so_far[next_cell]:
                        cost_so_far[next_cell] = new_cost
                        priority = new_cost + heuristic(goal, next_cell)
                        heapq.heappush(open_list, (priority, next_cell))
                        came_from[next_cell] = current
    return reconstruct_path(came_from, start, goal)

# Reconstructs the path
def reconstruct_path(came_from, start, goal):
    current = goal
    path = []
    while current != start:
        path.append(current)
        current = came_from[current]
    path.append(start)
    path.reverse()
    return path

# Generates the game grid
def generate_grid():
    grid = [[" " for _ in range(GRID_SIZE)] for _ in range(GRID_SIZE)]

    for _ in range(GRID_SIZE * 3):
        x, y = random.randint(0, GRID_SIZE - 1), random.randint(0, GRID_SIZE - 1)
        grid[y][x] = "O"

    for _ in range(GRID_SIZE):
        x, y = random.randint(0, GRID_SIZE - 1), random.randint(0, GRID_SIZE - 1)
        grid[y][x] = "D"

    for _ in range(GRID_SIZE):
        x, y = random.randint(0, GRID_SIZE - 1), random.randint(0, GRID_SIZE - 1)
        grid[y][x] = "G"

    treasures = []
    for _ in range(6):
        x, y = random.randint(0, GRID_SIZE - 1), random.randint(0, GRID_SIZE - 1)
        grid[y][x] = "T"
        treasures.append((x, y))

    player_start = (0, 0)
    grid[0][0] = "P"

    return grid, player_start, treasures

# Finds the optimal order for the AI to collect treasures using permutations
def find_best_path(grid, player, treasures):
    all_paths = []
    for perm in itertools.permutations(treasures):
        current_pos = player
        total_cost = 0
        for treasure in perm:
            path = a_star_search(grid, current_pos, treasure)
            total_cost += len(path) - 1
            current_pos = treasure
        all_paths.append((total_cost, perm))

    best_path = min(all_paths, key=lambda x: x[0])
    return best_path[1]

# Draws the grid
def draw_grid(grid):
    for y in range(GRID_SIZE):
        for x in range(GRID_SIZE):
            rect = pygame.Rect(x * CELL_SIZE, y * CELL_SIZE, CELL_SIZE, CELL_SIZE)
            if grid[y][x] == "O":
                pygame.draw.rect(screen, OBSTACLE_COLOR, rect)
            elif grid[y][x] == "D":
                pygame.draw.rect(screen, DAMAGE_COLOR, rect)
            elif grid[y][x] == "G":
                pygame.draw.rect(screen, GOLD_COLOR, rect)
            elif grid[y][x] == "T":
                pygame.draw.rect(screen, TREASURE_COLOR, rect)
            else:
                pygame.draw.rect(screen, BACKGROUND_COLOR, rect)

            pygame.draw.rect(screen, (200, 200, 200), rect, 1)

# Start menu screen
def start_menu():
    menu_running = True
    background_image = pygame.image.load("start.jpg")
    background_image = pygame.transform.scale(background_image, (WINDOW_SIZE, WINDOW_SIZE))
    font = pygame.font.Font(None, 36)
    title_font = pygame.font.Font(None, 48)  # Larger font for the title

    start_button = pygame.Rect(WINDOW_SIZE // 2 - 100, WINDOW_SIZE // 2 - 50, 200, 50)
    quit_button = pygame.Rect(WINDOW_SIZE // 2 - 100, WINDOW_SIZE // 2 + 20, 200, 50)

    while menu_running:
        screen.blit(background_image, (0, 0))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if start_button.collidepoint(event.pos):
                    menu_running = False
                if quit_button.collidepoint(event.pos):
                    pygame.quit()
                    exit()

        mouse_pos = pygame.mouse.get_pos()
        pygame.draw.rect(screen, BUTTON_HOVER_COLOR if start_button.collidepoint(mouse_pos) else BUTTON_COLOR, start_button)
        pygame.draw.rect(screen, BUTTON_HOVER_COLOR if quit_button.collidepoint(mouse_pos) else BUTTON_COLOR, quit_button)

        start_text = font.render("Start Game", True, TEXT_COLOR)
        quit_text = font.render("Quit Game", True, TEXT_COLOR)

        # Render and display the title
        title_text = title_font.render("AI Maze: Hunt for treasure !", True, OBSTACLE_COLOR)
        screen.blit(title_text, (WINDOW_SIZE // 2 - title_text.get_width() // 2, 50))

        screen.blit(start_text, (start_button.x + (start_button.width - start_text.get_width()) // 2, start_button.y + 10))
        screen.blit(quit_text, (quit_button.x + (quit_button.width - quit_text.get_width()) // 2, quit_button.y + 10))

        pygame.display.flip()
        clock.tick(60)


# Displays a message on the screen
def show_message(message, color):
    font = pygame.font.Font(None, 48)
    text = font.render(message, True, color)
    screen.fill(BACKGROUND_COLOR)
    screen.blit(text, (WINDOW_SIZE // 2 - text.get_width() // 2, WINDOW_SIZE // 2 - text.get_height() // 2))
    pygame.display.flip()
    pygame.time.delay(3000)

# Main function
def main():
    start_menu()
    grid, player, treasures = generate_grid()
    best_treasure_path = find_best_path(grid, player, treasures)

    player_hp = PLAYER_HP
    player_gold = PLAYER_GOLD

    for treasure in best_treasure_path:
        path = a_star_search(grid, player, treasure)
        for step in path:
            player = step
            x, y = player

            if grid[y][x] == "D":
                player_hp -= 15
                grid[y][x] = " "
            elif grid[y][x] == "G":
                player_gold += 10
                grid[y][x] = " "
            elif grid[y][x] == "T":
                grid[y][x] = " "

            if player_hp < 50:
                show_message("Game Over!", (255, 0, 0))
                return

            screen.fill(BACKGROUND_COLOR)
            draw_grid(grid)
            pygame.draw.rect(screen, PLAYER_COLOR, pygame.Rect(x * CELL_SIZE, y * CELL_SIZE, CELL_SIZE, CELL_SIZE))
            pygame.display.set_caption(f"HP: {player_hp} | Gold: {player_gold}")
            pygame.display.flip()
            clock.tick(FPS)

    show_message("You collected all treasures!", (0, 128, 0))
    pygame.quit()

main()