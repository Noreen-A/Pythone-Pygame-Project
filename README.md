# Treasure Hunt AI Game

## Project Overview
The **Treasure Hunt AI Game** is a grid-based simulation where an AI agent autonomously navigates the game world to collect scattered treasures. The game environment consists of various elements:

- **Obstacles (Black Blocks):** Restrict movement and create challenges in pathfinding.
- **Damage Zones (Red Cells):** Reduce the player's health upon traversal, adding strategic complexity.
- **Gold (Yellow Blocks):** Bonus items that increase the player's score.
- **Treasures:** The goal of the AI agent, scattered across the grid.

The AI agent employs the **A* (A-star) algorithm**, a widely used pathfinding technique, to compute the shortest path to each treasure. The gameplay is fully automated, with the AI efficiently navigating through the grid while avoiding obstacles and managing health and score.

## Objective of the Script
This project aims to demonstrate AI pathfinding capabilities in a simulated environment. Specifically, it:

1. **Automates Gameplay:** Develops an AI agent that autonomously navigates the grid to collect all treasures optimally.
2. **Showcases Pathfinding:** Implements the **A* algorithm** to compute the shortest and most efficient paths while dynamically adapting to game constraints.
3. **Simulates Real-World Challenges:** Introduces obstacles and damage zones to mimic real-world navigation problems.
4. **Enhances Player Metrics:** Tracks and displays the player's health and score, ensuring meaningful interactions within the game.

## Code Structure
### 1. Constants and Initialization
- Defines essential constants such as grid size, player attributes (health, gold), and colors for various game elements.
- Initializes **Pygame**, sets up the display window, and prepares the game clock.

### 2. Heuristic Function & A* Algorithm
- Implements a **Manhattan distance heuristic** to guide the A* algorithm.
- Develops the `a_star_search` function, which explores the shortest path from the player's current position to a specified goal while avoiding obstacles.

### 3. Grid Generation
- The `generate_grid` function creates a randomized game grid with obstacles, damage zones, gold, and treasures.
- Ensures a unique and dynamic game layout on every run.

### 4. Grid Visualization
- The `draw_grid` function renders the game grid, visually differentiating elements using distinct colors.

### 5. Path Optimization
- The `find_best_path` function calculates the optimal sequence for the AI agent to collect multiple treasures.
- Uses permutations to evaluate all possible collection orders and selects the shortest overall route.

### 6. Message Display
- The `show_message` function handles endgame scenarios, displaying messages such as "Game Over" or "You collected all treasures!" with appropriate formatting and delays.

### 7. Main Game Logic
- The `main` function integrates all components, managing AI traversal, health and gold updates, and real-time grid rendering.
- Simulates the AI’s pathfinding and treasure collection process while ensuring smooth gameplay.

## Conclusion
The **Treasure Hunt AI Game** successfully integrates **AI algorithms** into an interactive and dynamic gaming environment. By utilizing the **A* algorithm**, the project highlights real-world applications of artificial intelligence in solving complex navigation problems. The inclusion of obstacles, damage zones, and treasures adds strategic depth, making the game both educational and engaging.

---

### How to Run the Game
1. Install **Python** and **Pygame** if not already installed.
   ```sh
   pip install pygame
   ```
2. Run the game script:
   ```sh
   python treasure_hunt.py
   ```
3. Watch the AI agent navigate the grid and collect treasures automatically!

---

### Future Enhancements
- Implement a **graphical user interface (GUI)** for a more immersive experience.
- Introduce **multiple AI agents** competing for treasures.
- Add **dynamic obstacles** that change position over time.

Enjoy the game! 🚀

