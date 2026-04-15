import tkinter as tk
from tkinter import messagebox

# ---------------- FILE PATHS ----------------
files = {
    "Easy": "easy.txt",
    "Medium": "medium.txt",
    "Hard": "hard.txt",
    "Very Hard": "very_hard.txt"
}

# ---------------- GLOBAL COUNTERS ----------------
backtrack_calls = 0
failures = 0

# ---------------- READ FROM TXT ----------------
def read_board(file):
    board = []
    with open(file, "r") as f:
        for line in f:
            board.append([int(x) for x in line.strip()])
    return board


# ---------------- CSP LOGIC ----------------
def get_domain(board, r, c):
    nums = set(range(1, 10))

    for i in range(9):
        nums.discard(board[r][i])
        nums.discard(board[i][c])

    br, bc = (r//3)*3, (c//3)*3
    for i in range(br, br+3):
        for j in range(bc, bc+3):
            nums.discard(board[i][j])

    return list(nums)


def find_empty(board):
    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:
                return i, j
    return None


def forward_check(board):
    for i in range(9):
        for j in range(9):
            if board[i][j] == 0 and len(get_domain(board, i, j)) == 0:
                return False
    return True


def solve(board):
    global backtrack_calls, failures
    backtrack_calls += 1

    empty = find_empty(board)
    if not empty:
        return True

    r, c = empty

    for val in get_domain(board, r, c):
        board[r][c] = val

        if forward_check(board) and solve(board):
            return True

        board[r][c] = 0

    failures += 1
    return False


# ---------------- GUI ----------------
class SudokuGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Sudoku CSP Solver")
        self.root.configure(bg="#1e1e2f")

        self.level = tk.StringVar(value="Easy")

        tk.Label(root, text="Sudoku CSP Solver",
                 font=("Arial", 20, "bold"),
                 fg="white", bg="#1e1e2f").pack(pady=10)

        tk.OptionMenu(root, self.level,
                      "Easy", "Medium", "Hard", "Very Hard").pack()

        self.frame = tk.Frame(root, bg="black")
        self.frame.pack(pady=10)

        self.cells = [[None]*9 for _ in range(9)]

        for i in range(9):
            for j in range(9):
                e = tk.Entry(self.frame, width=3,
                             font=("Arial", 16),
                             justify='center', bd=2)
                e.grid(row=i, column=j, padx=1, pady=1)
                self.cells[i][j] = e

        # Buttons
        tk.Button(root, text="Load Puzzle",
                  command=self.load_board,
                  bg="#4CAF50", fg="white").pack(pady=5)

        tk.Button(root, text="Solve",
                  command=self.solve_board,
                  bg="#2196F3", fg="white").pack(pady=5)

        tk.Button(root, text="Reset",
                  command=self.reset,
                  bg="#f44336", fg="white").pack(pady=5)

        # CSP Output Labels
        self.info = tk.Label(root, text="",
                             font=("Arial", 12),
                             fg="yellow", bg="#1e1e2f")
        self.info.pack(pady=10)

    def load_board(self):
        file = files[self.level.get()]
        board = read_board(file)

        for i in range(9):
            for j in range(9):
                self.cells[i][j].delete(0, tk.END)
                if board[i][j] != 0:
                    self.cells[i][j].insert(0, str(board[i][j]))

        self.info.config(text="Puzzle Loaded")

    def get_board(self):
        board = []
        for i in range(9):
            row = []
            for j in range(9):
                val = self.cells[i][j].get()
                row.append(int(val) if val else 0)
            board.append(row)
        return board

    def solve_board(self):
        global backtrack_calls, failures
        backtrack_calls = 0
        failures = 0

        board = self.get_board()

        if solve(board):
            for i in range(9):
                for j in range(9):
                    self.cells[i][j].delete(0, tk.END)
                    self.cells[i][j].insert(0, str(board[i][j]))

            # Show CSP results
            self.info.config(
                text=f"Solved | Backtracking Calls: {backtrack_calls} | Failures: {failures}"
            )
        else:
            messagebox.showerror("Error", "No Solution Found")

    def reset(self):
        for i in range(9):
            for j in range(9):
                self.cells[i][j].delete(0, tk.END)

        self.info.config(text="")


# ---------------- RUN ----------------
root = tk.Tk()
app = SudokuGUI(root)
root.mainloop()