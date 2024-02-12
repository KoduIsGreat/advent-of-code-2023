input = """1abc2
pqr3stu8vwx
a1b2c3d4e5f
treb7uchet"""


def find_answer_part_1(input: str) -> int:
    lines = input.split("\n")
    sum = 0
    for line in lines:
        if line == "":
            continue
        nums_only = "".join([c for c in line if not c.isalpha()])
        le = len(nums_only)
        sum += int(nums_only[0])*10
        if le == 0:
            sum += int(nums_only[0])
        else:
            sum += int(nums_only[le-1])
    return sum


sample_ans = find_answer_part_1(input)
print("Sample Answer: ", sample_ans)

with open("1/input.txt") as file:
    input = file.read()
    print("Answer: ", find_answer_part_1(input))
