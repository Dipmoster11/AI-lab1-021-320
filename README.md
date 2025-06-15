# Simple Reflex Agent Vacuum Cleaner

This project implements a simple reflex agent simulation of a vacuum cleaning robot in a 10x10 grid environment using Python and Tkinter for visualization.

---

## Overview

The agent moves systematically across a grid environment that consists of cells which can either be **dirty** or **clean**. The agent senses whether the current cell is dirty, cleans it if so, and then moves to the next cell. The simulation continues until all cells are cleaned.

---

## Features


- **Grid Environment:** 10 rows x 10 columns grid, where each cell is randomly initialized as dirty or clean.
- **Simple Reflex Agent:** The agent can sense dirt in the current cell and act accordingly by cleaning or moving.
- **Visual Representation:** Uses `tkinter` to display the grid and the agent’s position.
- **Statistics:** Displays the total number of moves taken and cells cleaned once the cleaning is complete.

---
![Screenshot 2025-06-15 214258](https://github.com/user-attachments/assets/b4a4d568-8cd1-4b40-a472-977ddc5b2d6c)

## How to Run

1. Make sure you have Python installed (version 3.6+ recommended).
2. Save the code file (e.g., `vacuum_agent.py`).
3. Run the program using the command:

   ```bash


