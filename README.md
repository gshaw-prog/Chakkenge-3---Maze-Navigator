<h1> Challenge 3: Maze Navigator </h1>

This challenge focuses on :  
<ul>
<li>
  B2.5.1 File Processing
</li>
<li>
  B2.2.2 Arrays and Lists (specifically two-dimensional lists)
</li>
<li>
  B2.3.2 Selection Structures
</li>
<li>
  B2.3.3 Looping Structures
</li>
</ul>

<h2>Problem Description: </h2> You are provided with a text file <i>(maze-navigator.txt)</i> that represents a grid (a two-dimensional list).

<ul>
  <li>
    . represents an open space.
  </li>
   <li>
    # represents a wall.
  </li>
   <li>
    S represents the starting position.
  </li>
   <li>
    E represents the end position.
  </li>
</ul>

<h2>Your Task:</h2> 
Your task is to write a program that finds the shortest path from 'S' to 'E' using only up, down, left, and right moves. You must count the number of steps taken to solve the maze.
Construct a Python program with a function maze_navigator() that:

<ul>
  <li>
    Reads the maze-navigator.txt file and converts it into a two-dimensional list (or array) representing the maze.
  </li>
   <li>
    Finds the starting position ('S') and the end position ('E').
  </li>
   <li>
    Implements a pathfinding algorithm (e.g., a Breadth-First Search (BFS) simulation) to find the shortest path.
  </li>
   <li>
    Counts the number of steps in the shortest path.
  </li>
</ul>

<h2>Input:</h2> maze-navigator.txt

<h2>Function name: </h2> maze_navigator()

<h2>Return Value:</h2> An integer, being the number of steps taken to solve the maze. (The starting location is considered 0 steps, and you must step into the end location.)

<h2>Key Concepts to Apply:</h2>
<ul>
  <li>
    File Processing (B2.5.1): Read the maze layout from the text file line by line.
  </li>
  <li>
    Two-dimensional Lists/Arrays (B2.2.2): Represent the maze as a 2D list in Python. This data structure is ideal for grid-based problems.
  </li>
  <li>
     Looping Structures (B2.3.3): Use nested loops to traverse the 2D list to find 'S' and 'E'. More importantly, loops are essential for simulating movement and exploration in a pathfinding algorithm (e.g., a while loop for the main search process and for loops for checking adjacent cells).
  </li>
  <li>
    Selection Structures (B2.3.2): if statements will be used to check if a cell is a wall (#), an open space (.), the start (S), or the end (E). Also, to check if a move is within the maze boundaries.
  </li>
  <li>
    Algorithms (B2.4.2): This challenge involves a basic pathfinding algorithm simulation.
  </li>
</ul>
<b>Note on Recursion:</b> As per the instruction, avoid using recursion and simulate movement with loops.
<h2>Hints and Guidance:</h2>
<ul>
<li>
  Represent the maze as a list of lists (Python).
</li>
<li>
  To find the shortest path, consider using a Breadth-First Search (BFS) algorithm. This involves a queue to store (row, col, steps) tuples.
</li>
<li>
  You'll need a way to keep track of visited cells to avoid infinite loops and re-exploring paths. A separate 2D list or set of (row, col) tuples can serve as a visited tracker.
</li>
<li>
  Define the four possible moves: (0, 1) (right), (0, -1) (left), (1, 0) (down), (-1, 0) (up).
</li>
<li>
  The number of steps should be calculated from 'S' to 'E'. If 'S' is at (r, c) and 'E' is at (r', c'), and you arrive at 'E' in N steps from 'S', the return value is N.
</li>
</ul>
