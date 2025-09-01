Here is a Python solution for "Challenge 3: Maze Navigator", incorporating programming techniques detailed in the B2 Programming section of the sources, along with comments to explain each step:

```python
def maze_navigator():
    """
    Reads a maze from 'maze-navigator.txt', finds the shortest path from 'S' to 'E',
    and returns the number of steps taken using a Breadth-First Search (BFS) simulation.

    This function applies concepts from:
    - B2.5.1 File Processing: Reading data from a text file.
    - B2.1.1 Programming Fundamentals: Using variables and data types (int, str, tuple, list, set).
    - B2.2.2 Arrays and Lists: Representing the maze as a two-dimensional list.
    - B2.2.4 Queues: Simulating a queue for BFS using a Python list.
    - B2.3.2 Selection Structures: Using if statements for maze boundaries and cell checks.
    - B2.3.3 Looping Structures: Using for and while loops for iteration and search.
    - B2.4.2 Programming Algorithms: Implementing a pathfinding algorithm (BFS).
    """

    maze = []
    start_pos = None
    end_pos = None

    # --- File Processing (B2.5.1) and Maze Initialization ---
    # Attempt to open and read the maze file.
    # Exception handling (B2.1.3) is used to prevent the program from crashing
    # if the file is not found or contains unreadable data.
    try:
        with open("maze-navigator.txt", "r") as file:
            # Iterate through each line in the file using a for loop (B2.3.3).
            # enumerate helps get both the row index (r) and the line content.
            for r, line in enumerate(file):
                # Clean the line by removing whitespace (like newline characters)
                # and convert it into a list of characters for the current row.
                row_chars = list(line.strip())
                maze.append(row_chars) # Add the row to our 2D list (B2.2.2).

                # Find the 'S' (start) and 'E' (end) positions using selection structures (B2.3.2).
                if 'S' in row_chars:
                    start_pos = (r, row_chars.index('S')) # Store (row, column) tuple.
                if 'E' in row_chars:
                    end_pos = (r, row_chars.index('E')) # Store (row, column) tuple.

    except FileNotFoundError:
        print("Error: The maze file 'maze-navigator.txt' was not found.")
        return -1  # Return -1 to indicate an error (no path found or file issue).
    except Exception as e:
        print(f"An unexpected error occurred while reading the maze file: {e}")
        return -1

    # Basic validation to ensure the maze, start, and end points are valid.
    if not maze or start_pos is None or end_pos is None:
        print("Error: Maze not properly formed or start/end positions are missing.")
        return -1

    # Get the dimensions of the maze (number of rows and columns).
    num_rows = len(maze)
    num_cols = len(maze) # Assumes all rows have the same number of columns, forming a rectangle.

    # --- Queue for BFS (B2.2.4) and Visited Tracker ---
    # A list is used to simulate a queue. For BFS, items are added to the end (enqueue)
    # and removed from the beginning (dequeue).
    # Each item in the queue is a tuple: (current_row, current_col, steps_taken).
    queue = []
    # A set is used to keep track of visited cells (row, col) to avoid revisiting
    # and to ensure the shortest path is found by preventing cycles.
    visited_cells = set()

    # Enqueue the starting position. The starting position itself is 0 steps.
    queue.append((start_pos, start_pos, 0))
    visited_cells.add((start_pos, start_pos))

    # Define possible movements: (delta_row, delta_column) for up, down, left, right.
    # This array is iterated through using a for loop (B2.3.3).
    movements = [(-1, 0), (1, 0), (0, -1), (0, 1)] # Up, Down, Left, Right

    # --- Breadth-First Search (BFS) Algorithm (B2.4.2) ---
    # The main BFS loop continues as long as there are positions in the queue to explore (B2.3.3).
    while queue:
        # Dequeue the oldest item from the front of the list (simulating queue.popleft()).
        # Python's list.pop(0) removes and returns the first element.
        current_r, current_c, steps = queue.pop(0)

        # Check if the current position is the end position using selection structures (B2.3.2).
        if current_r == end_pos and current_c == end_pos:
            return steps  # Return the total steps to reach the end.

        # Explore all valid neighbours of the current position.
        for dr, dc in movements:
            next_r, next_c = current_r + dr, current_c + dc # Calculate new coordinates.

            # --- Selection Structures (B2.3.2) for validating moves ---
            # Check if the new position is within the maze boundaries.
            is_within_bounds = (0 <= next_r < num_rows and 0 <= next_c < num_cols)

            if is_within_bounds:
                # Check if the new position is not a wall ('#') AND has not been visited yet.
                is_not_wall = (maze[next_r][next_c] != '#')
                is_not_visited = ((next_r, next_c) not in visited_cells)

                if is_not_wall and is_not_visited:
                    # Mark the new position as visited.
                    visited_cells.add((next_r, next_c))
                    # Enqueue the new position with an incremented step count.
                    queue.append((next_r, next_c, steps + 1))

    # If the loop finishes and the end position was never reached, it means no path exists.
    return -1 # Return -1 to indicate no path found.

# Example of how you might call the function (for testing, not part of the function itself)
# if __name__ == "__main__":
#     # To test, ensure 'maze-navigator.txt' exists in the same directory
#     # with a maze definition.
#     # Example content for maze-navigator.txt:
#     # S.#
#     # ...
#     # #.E
#     result = maze_navigator()
#     if result != -1:
#         print(f"The shortest path in the maze is {result} steps.")
#     else:
#         print("No path found to the end of the maze, or an error occurred.")
```