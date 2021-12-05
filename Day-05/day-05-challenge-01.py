#!/usr/bin/env python3


class Line:
    def __init__(self, start_x=0, start_y=0, end_x=0, end_y=0):
        self.x1 = start_x
        self.y1 = start_y

        self.x2 = end_x
        self.y2 = end_y

    def is_diagonal(self):
        if self.x1 != self.x2 and self.y1 != self.y2:
            return True

        return False

    def is_vertical(self):
        if self.x1 == self.x2:
            return True

        return False

    def is_horizontal(self):
        if self.y1 == self.y2:
            return True

        return False


class Display:
    def __init__(self, lines=None):
        self.x_width = 0
        self.y_width = 0
        self.lines = []

        if lines is not None:
            for line in lines:
                x1, y1 = [int(point) for point in line[0].split(",")]
                x2, y2 = [int(point) for point in line[1].split(",")]

                line = Line(x1, y1, x2, y2)

                # Skip Diagonal lines.
                if line.is_diagonal():
                    continue

                # Expand the board.
                self._expand_board(line)

                self.lines.append(line)

        self.board = [[0 for _ in range(0, self.x_width)] for _ in range(0, self.y_width + 1)]

        if len(self.lines):
            self._draw_lines()

    def _expand_board(self, line):
        if line.x1 >= self.x_width or line.x2 >= self.x_width:
            self.x_width = max(line.x1, line.x2) + 1
        if line.y1 >= self.y_width or line.y2 >= self.y_width:
            self.y_width = max(line.y1, line.y2) + 1

    def _draw_line(self, line):
        if line.is_horizontal():
            for x in range(min(line.x1, line.x2), max(line.x1, line.x2) + 1):
                self.board[line.y1][x] = self.board[line.y1][x] + 1
        elif line.is_vertical():
            for y in range(min(line.y1, line.y2), max(line.y1, line.y2) + 1):
                self.board[y][line.x1] = self.board[y][line.x1] + 1

    def _draw_lines(self):
        for line in self.lines:
            self._draw_line(line)

    def _render(self):
        lines = []

        for y in range(0, self.y_width):
            line = []

            for x in range(0, self.x_width):
                value = self.board[y][x]

                if value:
                    line.append(str(value))
                else:
                    line.append(".")

            lines.append("".join(line))

        return "\n".join(lines)

    def __str__(self):
        return self._render()


def main():
    input = []

    with open("day-05-input.txt", "r") as input_file:
        input = [line.rstrip("\n").split(" -> ") for line in input_file.readlines()]

    display = Display(input)

    print(display)

    count = 0

    for y in range(0, display.y_width):
        for x in range(0, display.x_width):
            if display.board[y][x] > 1:
                count += 1

    print(f"Count: {count}")


if __name__ == "__main__":
    main()
