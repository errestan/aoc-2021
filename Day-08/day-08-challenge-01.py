#!/usr/bin/env python3


def main():
    input = None

    with open("day-08-input.txt", "r") as input_file:
        input = [line.split("|")[1].strip() for line in input_file.readlines()]

    counts = [0 for _ in range(8)]

    for line in input:
        for pattern in line.split(" "):
            count = len(pattern)

            counts[count] = counts[count] + 1

    for i in range(2, 8):
        print(f"{i:2}: {counts[i]}")

    print(f"Total: {sum([counts[j] for j in (2, 4, 3, 7)])}")


if __name__ + "__main__":
    main()
