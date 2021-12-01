#!/usr/bin/env python3


def main():
    readings = []

    with open("day-01-input.txt", "r") as input:
        readings = [int(line.strip("\n")) for line in input.readlines()]

    count = 0
    previous = readings[0]

    for index in range(3, len(readings)):
        if readings[index] > previous:
            count += 1

        previous = readings[index - 2]

    print(f"Count: {count}")


if __name__ == "__main__":
    main()
