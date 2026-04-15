## 🧠 Project Title

**Sudoku Solver using Constraint Satisfaction Problem (CSP)**

---

## 📌 Overview

This project implements a **Sudoku Solver** using **Artificial Intelligence (CSP techniques)**.
It uses **Backtracking Search with Forward Checking** to efficiently solve Sudoku puzzles of varying difficulty levels through an **interactive Tkinter-based GUI**.

The system reads puzzles from `.txt` files and visually solves them while displaying important CSP metrics like **backtracking calls and failures**.

---

## 🎯 Objectives

* Apply **Constraint Satisfaction Problem (CSP)** concepts
* Implement **Backtracking Search Algorithm**
* Use **Forward Checking for domain reduction**
* Solve Sudoku puzzles of different difficulty levels
* Build an **interactive and user-friendly GUI**
* Analyze performance using **search metrics**

---

## ⚙️ Functionality / Working

1. User selects difficulty:

   * Easy
   * Medium
   * Hard
   * Very Hard

2. Puzzle is loaded from `.txt` file

3. Solver applies:

   * **Backtracking**
   * **Forward Checking**
   * **Constraint Propagation**

4. Final solution is displayed on GUI

5. System shows:

   * ✅ Backtracking Calls
   * ❌ Failures

---

## 🧰 Tools & Technologies Used

* **Python**
* **Tkinter (GUI)**
* Basic File Handling (`.txt`)
* CSP Concepts:

  * Backtracking
  * Forward Checking
  * Domain Reduction

---

## ✨ Features

✔ Interactive GUI (no terminal dependency)\
✔ Multiple difficulty levels\
✔ Real-time board visualization\
✔ Clean grid with structured layout\
✔ File-based puzzle loading\
✔ Displays CSP performance metrics\
✔ Reset & reload functionality\

---

## 📊 CSP Concepts Implemented

| Concept          | Description                          |
| ---------------- | ------------------------------------ |
| Backtracking     | Recursive search for solution        |
| Forward Checking | Eliminates invalid values early      |
| Domain Reduction | Limits possible values for each cell |

---

## 📁 Input Format

* Each Sudoku file contains:

  * 9 rows
  * 9 digits per row
  * `0` represents empty cells

---

## 📈 Observations

* Easy puzzles → fewer backtracking calls
* Hard puzzles → significantly more search effort
* Demonstrates **exponential complexity of CSP**

---

## 🚀 How to Run

1. Place all `.txt` files in same directory
2. Run the Python file:

```bash
python sudoku_solver.py
```

3. Select difficulty → Click “Load” → Click “Solve”

---

## 📌 Future Improvements

* Add **AC-3 Algorithm (Arc Consistency)**
* Add **step-by-step solving animation**
* Highlight changed cells dynamically
* Add timer and performance graphs
