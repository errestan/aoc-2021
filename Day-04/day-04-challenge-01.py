#!/usr/bin/env python3


class Cell:
    def __init__(self, value):
        self.value = value
        self.state = False

    def __str__(self):
        return f"\033[94m{self.value:02}\033[0m" if self.state else f"{self.value:02}"

    def call(self, number):
        if self.value == number:
            self.state = True

    def check(self):
        return self.state


class Board:
    x_cells = 5
    y_cells = 5

    def __init__(self, state=None):
        self.cells = [[0 for _ in range(0, Board.x_cells)] for _ in range(0, Board.y_cells)]
        self.has_won = False

        if state is not None:
            for y in range(0, Board.y_cells):
                for x in range(0, Board.x_cells):
                    self.cells[y][x] = Cell(state.pop(0))

    def _check_rows(self):
        for y in range(0, Board.y_cells):
            result = True

            for x in range(0, Board.x_cells):
                if not self.cells[y][x].check():
                    result = False
                    break

            if result:
                return True

        return False

    def _check_cols(self):
        for x in range(0, Board.x_cells):
            result = True

            for y in range(0, Board.y_cells):
                if not self.cells[y][x].check():
                    result = False
                    break

            if result:
                return True

        return False

    def _check(self):
        result = False

        if self._check_rows():
            result = True
        elif self._check_cols():
            result = True
        else:
            result = False

        self.has_won = result

    def __str__(self):
        lines = []

        for y in range(0, Board.y_cells):
            lines.append(" ".join([str(i) for i in self.cells[y]]))

        return "\n".join(lines)

    def __repr__(self):
        return str(self)

    def call(self, number):
        for y in range(0, Board.y_cells):
            for x in range(0, Board.x_cells):
                self.cells[y][x].call(number)

        self._check()

    def get_score(self):
        score = 0

        for x in range(0, Board.x_cells):
            for y in range(0, Board.y_cells):
                if not self.cells[y][x].state:
                    score += self.cells[y][x].value

        return score


def main():
    called = []
    boards = []

    with open("day-04-input.txt", "r") as input_file:
        called = [int(number) for number in input_file.readline().rstrip("\n").split(",")]

        values = []

        for line in input_file.readlines():
            line = line.rstrip("\n")

            if line == "":
                continue

            values += [int(number) for number in line.split(" ") if number.isnumeric()]

            if len(values) == Board.x_cells * Board.y_cells:
                boards.append(Board(values))
                values = []

    score = 0

    for number in called:
        winner = False

        for board in boards:
            if board.has_won:
                continue

            board.call(number)

            if board.has_won:
                print(f"{board}\n")
                score = number * board.get_score()
                break

        if score != 0:
            break

    print(f"Score: {score}")


if __name__ == "__main__":
    main()
