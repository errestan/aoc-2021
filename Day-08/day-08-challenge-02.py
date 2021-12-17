#!/usr/bin/env python3


# This list defines the rules used to deduce values. Column headings are:
#   Target  Filter  Remainder   Previous
#
# Where:
#   Target:     is the number the rule will attempt to deduce.
#   Filter:     is the number of "bits" should be present in the input in order to consider it to be useful.
#   Remainder:  is the number of set bits remaining after the input is xor'ed with the previous.
#   Previous:   is an optional previous value that is needed for the rule to work.
deduction_args = [
    (1, 2, 0),
    (4, 4, 0),
    (7, 3, 0),
    (8, 7, 0),
    (3, 5, 3, 1),
    (6, 6, 6, 1),
    (9, 6, 2, 4),
    (2, 5, 3, 9),
    (2, 5, 0),
    (3, 5, 0),
    (5, 5, 0),
    (6, 6, 0),
    (9, 6, 0),
    (0, 6, 0),
]


class Display:
    @staticmethod
    def str_to_value(input):
        value = 0

        for char in input:
            value |= 1 << ord(char) - ord("a")

        return value

    def __init__(self, samples=None, readings=None):
        self.encode_map = {}
        self.decode_map = {}
        self.samples = []
        self.readings = []

        if samples is not None:
            for sample in samples:
                self.samples.append(Display.str_to_value(sample))

        if readings is not None:
            for reading in readings:
                self.readings.append(Display.str_to_value(reading))

    def __str__(self):
        output = []

        for reading in self.readings:
            value = self.decode_map.get(reading)

            if value is not None:
                output.append(str(value))
            else:
                output.append("?")

        return "".join(output)

    def _deduce_value(self, target, filter, remainder, previous=None):
        if target in self.encode_map.keys():
            return False

        other = 0

        if previous is not None:
            other = self.encode_map.get(previous)

            if other is None:
                print(f"Need {previous} to get {target}")

        matches = []

        for sample in self.samples:
            if bin(sample).count("1") != filter or sample in self.decode_map.keys():
                continue

            if other == 0:
                matches.append(sample)
            elif bin(sample ^ other).count("1") == remainder:
                matches.append(sample)

        if len(matches) == 1:
            print(f"Found {target}: {matches[0]:x}")
            self.encode_map[target] = matches[0]
            self.decode_map[matches[0]] = target
            return True

        return False

    def decipher(self):
        if 10 == len(self.encode_map.values()) and 10 == len(self.decode_map.values()):
            print("Already de-ciphered reading")
            return True

        for args in deduction_args:
            result = self._deduce_value(*args)

            if result and "?" not in self.__str__():
                return True

        return False

    def reading(self):
        return int(self.__str__())


def main():
    input = None

    with open("day-08-input.txt", "r") as input_file:
        input = [line.strip() for line in input_file.readlines()]

    displays = []

    for line in input:
        samples, reading = (s.strip() for s in line.split("|"))

        display = Display(samples.split(" "), reading.split(" "))
        success = display.decipher()

        if not success:
            print("Failed to deduce mapping(s)")
            break

        print(display)

        displays.append(display)

    print(f"Total: {sum([display.reading() for display in displays])}")


if __name__ + "__main__":
    main()
