#!/usr/bin/env python3


def count_bits(list, column):
    values = [0 for _ in range(0, len(list[0]))]

    for line in list:
        if line[column] == "1":
            values[column] = values[column] + 1

    return values[column]


def most_common_bit(values, column):
    count = count_bits(values, column)
    return 1 if count >= (len(values) / 2) else 0


def least_common_bit(values, column):
    count = count_bits(values, column)
    return 1 if count < (len(values) / 2) else 0


def filter_value(result, column, value):
    return True if int(result[column]) == value else False


def filter_list(lines, value):
    results = lines

    for pos in range(0, len(lines[0])):
        bit = 0

        if value == 1:
            bit = most_common_bit(results, pos)
        else:
            bit = least_common_bit(results, pos)

        results = [result for result in results if filter_value(result, pos, bit)]

        if len(results) <= 1:
            break

    return results


def bin_to_dec(lines):
    dec_val = 0
    bin_len = len(lines[0])

    for bin_val in lines:
        for index in range(0, bin_len):
            if bin_val[index] == "1":
                dec_val |= 1 << (bin_len - index - 1)

    return dec_val


def main():
    lines = []

    with open("day-03-input.txt", "r") as input:
        lines = [line.rstrip("\n") for line in input.readlines()]

    oxygen = filter_list(lines, 1)
    oxygen_rate = bin_to_dec(oxygen)

    scrubber = filter_list(lines, 0)
    scrubber_rate = bin_to_dec(scrubber)

    print(f"{oxygen_rate}, {scrubber_rate} = {oxygen_rate * scrubber_rate}")


if __name__ == "__main__":
    main()
