# Maze-Problem
Maze Solver (Path Finding Algorithm)

This project is about solving a maze using a simple algorithm that finds the path to the goal within a **limited number of steps or iterations**.

##  What it does

- A maze is created with a start and goal point.
- An algorithm runs step by step.
- After a **limited number of tries**, the algorithm **finds the correct path** and reaches the goal.
- If it doesn’t reach the goal in time, it stops.

## 💡How it works (Basic Idea)

1. The algorithm looks around its current position.
2. It chooses the best possible next step.
3. It remembers the steps it took.
4. It avoids going in circles.
5. It keeps going until:
   - It finds the goal 
   - Or the max number of steps is used 

##  Files in the project

- `main.py`: The main file where the algorithm runs.
- `maze.py`: Code for creating and displaying the maze.
- `README.md`: This file.

##  How to run

1. Make sure Python is installed.
2. Run the project:

bash
python main.py
You’ll see the maze and how the algorithm moves step by step.

## 🧠 Goal

The goal of this project is to understand how algorithms can solve problems like finding a path through a maze using limited resources or time.
