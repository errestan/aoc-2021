#!/usr/bin/env python3


cache = {}


def calculate_fuel(start, target):
    distance = abs(target - start)

    if distance in cache:
        return cache[distance]
    else:
        fuel = sum([i for i in range(1, abs(target - start) + 1)])

        cache[distance] = fuel
        return fuel


def main():
    input = None

    with open("day-07-input.txt", "r") as input_file:
        input = [int(i) for i in input_file.readline().strip().split(",")]

    input.sort()

    best_fuel = sum([fuel for fuel in range(1, input[-1] * len(input) + 1)])
    best_pos = 0

    for pos in range(input[0], input[-1] + 1):
        total_fuel = 0

        for crab in input:
            total_fuel += calculate_fuel(crab, pos)

        if total_fuel < best_fuel:
            best_fuel = total_fuel
            best_pos = pos

    print(f"Total Fuel: {best_fuel} at position: {best_pos}")


if __name__ == "__main__":
    main()
