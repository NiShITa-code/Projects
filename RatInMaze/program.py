import random
from colorama import Fore, Back, Style, init
init(autoreset=True)
WALL = '▓'
OPEN_SPACE = '◌'
PATH = '◍'
def generate_maze(n):
    wall_percentage = 25
    maze = [[OPEN_SPACE for _ in range(n)] for _ in range(n)]
    num_walls = int(n * n * wall_percentage / 100)
    # Place walls randomly
    for _ in range(num_walls):
        i, j = random.randint(0, n-1), random.randint(0, n-1)
        # Ensure the start and end points are not walls
        while (i, j) == (0, 0) or (i, j) == (n-1, n-1):
            i, j = random.randint(0, n-1), random.randint(0, n-1)
        maze[i][j] = '▓'  


    maze[0][0] = 'S'
    maze[n-1][n-1] = 'E'
    return maze

def print_maze(maze):
    for row in maze:
        print('-' * len(row) * 4)  # print horizontal lines
        for cell in row:
            if cell == WALL:
                print(Fore.RED + cell, end=' | ')
            elif cell == OPEN_SPACE:
                print(Fore.BLUE + cell, end=' | ')
            elif cell == 'S':
                print(Fore.GREEN + cell, end=' | ')
            elif cell == 'E':
                print(Fore.GREEN + cell, end=' | ')
        print()
    print('-' * len(maze[0]) * 4)  # print horizontal line for the last row

from collections import deque



def find_path(maze):
    start = (0, 0)
    end = (len(maze)-1, len(maze)-1)

    queue = deque([(start, [])])
    visited = set()

    while queue:
        (current, path) = queue.popleft()

        if current == end:
            return path + [current]

        if current in visited:
            continue

        visited.add(current)

        row, col = current
        neighbors = [(row-1, col), (row+1, col), (row, col-1), (row, col+1)]

        for neighbor in neighbors:
            n_row, n_col = neighbor
            if 0 <= n_row < len(maze) and 0 <= n_col < len(maze[0]) and maze[n_row][n_col] != '▓':
                queue.append(((n_row, n_col), path + [current]))

    return None  # No path found


def print_path(maze, path):
    for row in range(len(maze)):
        print('-' * len(maze[0]) * 4)
        for col in range(len(maze[0])):
            if (row, col) in path:
                print(Fore.GREEN + '◍', end=' | ')
            else:
                if maze[row][col] == WALL:
                    print(Fore.RED + maze[row][col], end=' | ')
                elif maze[row][col] == OPEN_SPACE:
                    print(Fore.BLUE + maze[row][col], end=' | ')
                elif maze[row][col] == 'S':
                    print(Fore.GREEN + maze[row][col], end=' | ')
                elif maze[row][col] == 'E':
                    print(Fore.YELLOW + maze[row][col], end=' | ')
        print()
    print('-' * len(maze[0]) * 4) 




def main():
    while True:
        n = int(input('Enter the size of the maze: '))
        maze = generate_maze(n)
        print_maze(maze)
        
        print("1. Print the path")
        print("2. Generate another puzzle")
        print("3. Exit the Game")

        choice = input("Enter your choice (1/2/3): ")

        if choice == "1":
            path = find_path(maze)
            if path:
                print_path(maze, path)
            else:
                print("No path found.")
        elif choice == "2":
            continue

        elif choice == "3":
            break
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")

        
        

if __name__ == '__main__':
    main()