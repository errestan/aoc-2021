#!/usr/bin/env python3


def model_fish(fish, days):
    items = [0 for _ in range(9)]

    for i in fish:
        items[i] += 1

    for day in range(days):
        temp = [0 for _ in range(9)]

        for i in range(9):
            if i == 0:
                temp[6] += items[i]
                temp[8] += items[i]
            else:
                temp[i - 1] += items[i]

        items = temp

    return sum([count for count in items])


def main():
    input = []

    with open("day-06-input.txt", "r") as inpute_file:
        input = [int(i) for i in inpute_file.readline().split(",")]

    count = model_fish(input, 256)

    print(f"Count: {count}")


if __name__ == "__main__":
    main()
