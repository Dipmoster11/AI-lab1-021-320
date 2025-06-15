import tkinter as tk
import random
import time
import tkinter.messagebox

# Grid config
ROWS = 4
COLS = 4
CELL_SIZE = 100
DELAY = 0.25  # seconds per move

# Colors
DIRTY_COLOR = "brown"
CLEAN_COLOR = "white"
AGENT_COLOR = "purple"

class Environment:
    def __init__(self, master):
        self.master = master
        self.canvas = tk.Canvas(master, width=COLS * CELL_SIZE, height=ROWS * CELL_SIZE)
        self.canvas.pack()
        self.grid = [[random.choice(['D', 'C']) for _ in range(COLS)] for _ in range(ROWS)]
        self.agent_pos = [0, 0]
        self.moves = 0
        self.cleaned = 0
        self.rects = [[None for _ in range(COLS)] for _ in range(ROWS)]
        self.draw_grid()

    def draw_grid(self):
        for i in range(ROWS):
            for j in range(COLS):
                color = DIRTY_COLOR if self.grid[i][j] == 'D' else CLEAN_COLOR
                self.rects[i][j] = self.canvas.create_rectangle(
                    j * CELL_SIZE, i * CELL_SIZE,
                    (j + 1) * CELL_SIZE, (i + 1) * CELL_SIZE,
                    fill=color, outline="black"
                )
        self.draw_agent()

    def draw_agent(self):
        i, j = self.agent_pos
        self.canvas.create_oval(
            j * CELL_SIZE + 20, i * CELL_SIZE + 20,
            (j + 1) * CELL_SIZE - 20, (i + 1) * CELL_SIZE - 20,
            fill=AGENT_COLOR, tags="agent"
        )

    def update_cell(self, i, j):
        color = DIRTY_COLOR if self.grid[i][j] == 'D' else CLEAN_COLOR
        self.canvas.itemconfig(self.rects[i][j], fill=color)

    def move_agent(self, new_i, new_j):
        self.canvas.delete("agent")
        self.agent_pos = [new_i, new_j]
        self.draw_agent()
        self.master.update()
        time.sleep(DELAY)
        self.moves += 1

    def clean_cell(self):
        i, j = self.agent_pos
        if self.grid[i][j] == 'D':
            self.grid[i][j] = 'C'
            self.cleaned += 1
            self.update_cell(i, j)

    def get_dirty_cells(self):
        return [(i, j) for i in range(ROWS) for j in range(COLS) if self.grid[i][j] == 'D']


class UtilityBasedAgent:
    def __init__(self, env: Environment):
        self.env = env

    def compute_utility(self, pos):
        agent_i, agent_j = self.env.agent_pos
        target_i, target_j = pos
        distance = abs(target_i - agent_i) + abs(target_j - agent_j)
        return -distance  # Utility is higher for closer cells

    def move_to(self, target):
        agent_i, agent_j = self.env.agent_pos
        target_i, target_j = target

        # Move row-wise
        while agent_i != target_i:
            agent_i += 1 if target_i > agent_i else -1
            self.env.move_agent(agent_i, agent_j)

        # Move column-wise
        while agent_j != target_j:
            agent_j += 1 if target_j > agent_j else -1
            self.env.move_agent(agent_i, agent_j)

    def act(self):
        while True:
            dirty_cells = self.env.get_dirty_cells()
            if not dirty_cells:
                break

            utilities = [(self.compute_utility(cell), cell) for cell in dirty_cells]
            best_cell = max(utilities, key=lambda x: x[0])[1]
            self.move_to(best_cell)
            self.env.clean_cell()

        self.show_stats()

    def show_stats(self):
        tk.messagebox.showinfo(
            "Cleaning Complete",
            f"Total Moves: {self.env.moves}\nCells Cleaned: {self.env.cleaned}"
        )


if __name__ == "__main__":
    root = tk.Tk()
    root.title("Utility-Based Vacuum Agent")

    env = Environment(root)
    agent = UtilityBasedAgent(env)

    root.after(1000, agent.act)
    root.mainloop()
