#!/usr/bin/env python3


def main():
    lines = []

    with open("day-03-input.txt", "r") as input:
        lines = [line.rstrip("\n") for line in input.readlines()]

    values = [0 for _ in range(0, len(lines[0]))]

    for line in lines:
        for index in range(0, len(line)):
            if line[index] == "1":
                values[index] = values[index] + 1 if values[index] is not None else 1

    gamma = 0
    sigma = 0

    for index in range(0, len(lines[0])):
        pos = len(lines[0]) - index - 1

        if values[index] >= (len(lines) / 2):
            gamma |= 1 << pos
        else:
            sigma |= 1 << pos

    print(f"{gamma}, {sigma} = {gamma * sigma}")


if __name__ == "__main__":
    main()
