#!/usr/bin/env python3


def main():
    readings = []

    with open("day-01-input.txt", "r") as input:
        readings = input.readlines()

    print(f"Reading {len(readings)} entries")

    count = 0
    previous = int(readings[0].strip("\n"))

    for reading in readings:
        reading = int(reading.strip("\n"))

        if reading > previous:
            count += 1

        previous = reading

    print(f"Count: {count}")


if __name__ == "__main__":
    main()
