part_2_digits_dict = {
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9
}
part_2_digit_lengths = {
    "one": 3,
    "two": 3,
    "three": 5,
    "four": 4,
    "five": 4,
    "six": 3,
    "seven": 5,
    "eight": 5,
    "nine": 4
}
part_2_input = """two1nine
eightwothree
abcone2threexyz
xtwone3four
4nineeightseven2
zoneight234
7pqrstsixteen
"""


def find_answer_part_2(input: str) -> int:
    lines = input.split("\n")
    sum = 0
    for line in lines:
        if line == "":
            continue

        found = {}
        for i in range(len(line)):
            if line[i].isdigit():
                found[i] = int(line[i])
            for k in part_2_digits_dict.keys():
                if line[i:i+part_2_digit_lengths[k]] == k:
                    found[i] = part_2_digits_dict[k]

        left = 9999
        right = 0

        for k, v in found.items():
            if k < left:
                left = k
            if k > right:
                right = k

            print("k: ", k, " v: ", v, " left: ", left, " right: ", right)
        val = found[left]*10 + found[right]
        print("Found: ", found, " left: ", found[left],
              " right: ", found[right], " val: ", val, " line: ", line)
        sum += val

    return sum


sample_ans = find_answer_part_2("xtwo1nine")
print("Sample Answer: ", sample_ans)
ans = find_answer_part_2(part_2_input)
print("Answer: ", ans)

with open("1/input.txt") as file:
    input = file.read()
    print("Answer: ", find_answer_part_2(input))
