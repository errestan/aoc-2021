#!/usr/bin/env python3


def main():
    instructions = []

    with open("day-02-input.txt", "r") as input:
        instructions = [instruction.split(" ") for instruction in input.readlines()]

    x_pos = 0
    y_pos = 0
    aim = 0

    for dir, val in instructions:
        val = int(val.rstrip("\n"))

        if dir == "up":
            aim -= val
        elif dir == "down":
            aim += val
        elif dir == "forward":
            x_pos += val
            y_pos += aim * val
        else:
            raise ValueError(f"Invalid direction {dir}")

    print(f"{x_pos}, {y_pos} = {x_pos * y_pos}")


if __name__ == "__main__":
    main()
