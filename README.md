README: AI Vacuum Cleaner Agents

Project Overview
This project simulates three types of Artificial Intelligence agents that perform cleaning tasks in a 2D grid environment:

Simple Reflex Agent
Goal-Based Agent
Utility-Based Agent

Each agent demonstrates a different level of intelligence and decision-making capability in how it perceives, reasons, and acts in a room with randomly placed dirt.

Objectives:
To understand and implement the different AI agent types.
To visualize the cleaning process in a grid-based environment.
To compare the performance (like number of moves, cells cleaned, and efficiency) of different agent strategies.

 Agent Types
1. Simple Reflex Agent
Behavior: Acts based only on the current percept (dirty or clean).
Logic: If current cell is dirty → clean it; else → move to the next cell.
Limitation: No memory or future planning.

Output:
![Screenshot 2025-06-15 214258](https://github.com/user-attachments/assets/e5cffb46-19b5-4d5b-84d7-a1df3100a31e)


3. Goal-Based Agent
Behavior: Takes actions to achieve a specific goal (e.g., clean the whole room).
Logic: Checks current state, evaluates whether the goal is met, and takes action accordingly.
Improvement: Can make smarter decisions like skipping already cleaned areas.

Output:

![Screenshot 2025-06-15 225823](https://github.com/user-attachments/assets/888dd458-97e2-46cb-bae4-12341e4c36f2)


3. Utility-Based Agent
Behavior: Chooses actions based on a utility function to maximize performance (e.g., minimize time, maximize dirt cleaned).
Logic: Uses sensors, state evaluations, and scores to decide the most valuable next move.
Advantage: Can choose optimal actions based on multiple factors.

Output:

![Screenshot 2025-06-15 232736](https://github.com/user-attachments/assets/f3d9f4b8-6c2b-451c-a05b-ca09b50cf74b)


## How to Run

1. Make sure you have Python installed (version 3.6+ recommended).
2. Save the code file (e.g., `vacuum_agent.py`).
3. Run the program using the command:

   ```bash


