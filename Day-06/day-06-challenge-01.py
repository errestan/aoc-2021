#!/usr/bin/env python3


def model_fish(fish, days):
    if days == 0:
        return len(fish)

    days -= 1

    for i in range(0, len(fish)):
        if fish[i] == 0:
            # Reset the fish.
            fish[i] = 6

            # Add the new fish.
            fish.append(8)
        else:
            fish[i] -= 1

    print(f"{days}: {fish}")

    return model_fish(fish, days)


def main():
    input = []

    with open("day-06-input.txt", "r") as inpute_file:
        input = [int(i) for i in inpute_file.readline().split(",")]

    count = model_fish(input, 80)

    print(f"Count: {count}")


if __name__ == "__main__":
    main()
