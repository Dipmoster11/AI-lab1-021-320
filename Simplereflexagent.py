import tkinter as tk
import random

# Constants
ROWS = 10
COLS = 10
CELL_SIZE = 50
DELAY = 100  # in milliseconds


class SimpleReflexAgent:
    def __init__(self, environment):
        self.env = environment
        self.row = 0
        self.col = 0
        self.moves = 0
        self.cleaned = 0

    def sense(self):
        return self.env[self.row][self.col] == 'D'

    def act(self):
        if self.sense():
            self.env[self.row][self.col] = 'C'  # Clean the dirt
            self.cleaned += 1
        else:
            self.move()

    def move(self):
        # Move to the next cell in row-wise order
        if self.col < COLS - 1:
            self.col += 1
        elif self.row < ROWS - 1:
            self.col = 0
            self.row += 1
        self.moves += 1

    def is_done(self):
        # Finish if reached the last cell and it's not dirty
        return self.row == ROWS - 1 and self.col == COLS - 1 and self.env[self.row][self.col] != 'D'


class VacuumApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Simple Reflex Vacuum Agent")

        self.canvas = tk.Canvas(root, width=COLS * CELL_SIZE, height=ROWS * CELL_SIZE)
        self.canvas.pack()

        # Initialize environment with random clean ('C') or dirty ('D') cells
        self.env = [[random.choice(['D', 'C']) for _ in range(COLS)] for _ in range(ROWS)]

        self.agent = SimpleReflexAgent(self.env)

        # Start the agent updates
        self.root.after(DELAY, self.update)

    def draw(self):
        self.canvas.delete("all")
        for i in range(ROWS):
            for j in range(COLS):
                x0 = j * CELL_SIZE
                y0 = i * CELL_SIZE
                x1 = x0 + CELL_SIZE
                y1 = y0 + CELL_SIZE
                fill_color = "white" if self.env[i][j] == 'C' else "brown"
                self.canvas.create_rectangle(x0, y0, x1, y1, fill=fill_color, outline="black")

        # Draw the agent as a blue circle
        ax0 = self.agent.col * CELL_SIZE + 10
        ay0 = self.agent.row * CELL_SIZE + 10
        ax1 = ax0 + CELL_SIZE - 20
        ay1 = ay0 + CELL_SIZE - 20
        self.canvas.create_oval(ax0, ay0, ax1, ay1, fill="blue")

    def update(self):
        self.draw()
        if not self.agent.is_done():
            self.agent.act()
            self.root.after(DELAY, self.update)
        else:
            self.agent.act()
            self.draw()
            self.show_stats()

    def show_stats(self):
        stats = f"Cleaning complete!\nMoves taken: {self.agent.moves}\nCells cleaned: {self.agent.cleaned}"
        stats_window = tk.Toplevel(self.root)
        stats_window.title("Statistics")
        tk.Label(stats_window, text=stats, font=("Arial", 14)).pack(padx=20, pady=20)


# Main block to run the GUI
if __name__ == "__main__":
    root = tk.Tk()
    app = VacuumApp(root)
    root.mainloop()
