import numpy as np


class SudokuGame:
    grid = []

    def __init__(self) -> None:
        self._reset_grid()

    def __str__(self) -> str:
        # TODO: Improve printing function
        return str(np.matrix(self.grid))

    def _reset_grid(self) -> None:
        self.grid = np.zeros((9, 9)).tolist()

    def input_rows(self) -> None:
        for r in range(9):
            line = input(f"Line {r+1}: ")
            for i, c in enumerate(line):
                self.grid[r][i] = int(c)


class SudokuSolver:
    game: SudokuGame
    hasSolution: False

    def __init__(self, game: SudokuGame) -> None:
        self.game = game
        self.hasSolution = False

    def solve(self) -> SudokuGame:
        if self.hasSolution:
            return
        for i in range(9):
            for j in range(9):
                if self.game.grid[i][j] == 0:
                    for n in range(1, 10):
                        if self._isPossible(i, j, n):
                            self.game.grid[i][j] = n
                            self.solve()
                            if self.hasSolution:
                                return
                            self.game.grid[i][j] = 0
                    return
        self.hasSolution = True

    def _isPossible(self, row, col, number) -> bool:
        for i in range(9):
            if self.game.grid[row][i] == number or self.game.grid[i][col] == number:
                return False

        row0 = (row // 3) * 3
        col0 = (col // 3) * 3

        for i in range(3):
            for j in range(3):
                if self.game.grid[row0 + i][col0 + j] == number:
                    return False
        return True


if __name__ == "__main__":
    s = SudokuGame()
    s.input_rows()
    solver = SudokuSolver(s)
    solver.solve()
    print(s)
