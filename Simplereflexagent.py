import tkinter as tk
import random
import time

# Grid size
ROWS = 4
COLS = 4
CELL_SIZE = 100
DELAY = 0.5  # seconds

# Colors
DIRTY_COLOR = "brown"
CLEAN_COLOR = "white"
AGENT_COLOR = "blue"

class Environment:
    def __init__(self, master):
        self.master = master
        self.canvas = tk.Canvas(master, width=COLS*CELL_SIZE, height=ROWS*CELL_SIZE)
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
                    j*CELL_SIZE, i*CELL_SIZE,
                    (j+1)*CELL_SIZE, (i+1)*CELL_SIZE,
                    fill=color, outline="black"
                )
        self.draw_agent()

    def draw_agent(self):
        i, j = self.agent_pos
        self.canvas.create_oval(
            j*CELL_SIZE+20, i*CELL_SIZE+20,
            (j+1)*CELL_SIZE-20, (i+1)*CELL_SIZE-20,
            fill=AGENT_COLOR,
            tags="agent"
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

    def clean_cell(self):
        i, j = self.agent_pos
        if self.grid[i][j] == 'D':
            self.grid[i][j] = 'C'
            self.cleaned += 1
            self.update_cell(i, j)

class ReflexAgent:
    def __init__(self, env: Environment):
        self.env = env

    def act(self):
        for i in range(ROWS):
            for j in range(COLS):
                self.env.move_agent(i, j)
                self.env.moves += 1
                self.env.clean_cell()

        self.show_stats()

    def show_stats(self):
        tk.messagebox.showinfo(
            "Cleaning Complete",
            f"Total Moves: {self.env.moves}\nCells Cleaned: {self.env.cleaned}"
        )

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Simple Reflex Vacuum Agent")
    import tkinter.messagebox  # Needed for popup

    env = Environment(root)
    agent = ReflexAgent(env)

    root.after

#my name jbdskjabbs