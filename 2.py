from pathlib import Path
import sys

def is_char_repeat(label, count):
    char_tested = []
    unique_char_list = list(set(label)) # created list of unique characters using list and set
    for unique_char in unique_char_list:
        unique_char_count = 0
        for char in label:
            if unique_char == char:
                unique_char_count += 1
        # now counted how many times unique_char repeats in label
        if unique_char_count == count:
            return 1
    return 0


def get_checksum(input_file):
    two_count = 0
    three_count = 0
    with open(input_file,"r") as f:
        content = f.read()
        labels = content.split('\n')
        for label in labels:
            two_count += is_char_repeat(label, 2)
            three_count += is_char_repeat(label, 3)
    return two_count * three_count

def part1(input_file):
    return get_checksum(input_file)

# for part 2

# given list of codes
# find codes that are identical except for one character being different

# how to achieve this - algorithm choices
    # option 1:
        # pick one string at a time, and compare with every other string
        # while comparing that string with another, if even one character different then move on to next string
        # move to next string and loop from that string onwards
    # option 2: (to make it efficient)
        # sort the strings - but is this useful? what if the character that is different is the first character
        # probably not useful

def differ_by_one_char(code1, code2):
    diff_char_count = 0
    for char_loc in range(0,len(code1)):
        if code1[char_loc] != code2[char_loc]:
            diff_char_count+=1
        if diff_char_count > 1:
            return False, None
    # if we are here then the previous return has not been reached and loop is over
    # create answer code
    if diff_char_count == 1:
        answer_code = ""
        for char_loc in range(0,len(code1)):
            if code1[char_loc] == code2[char_loc]:
                answer_code += code1[char_loc]
    return True, answer_code



def part2(input_file):
    # Load the file into a list
    with open(input_file, 'r') as f:
        codes = [line.rstrip() for line in f]
    # loop on the list
    found_answer = False
    for key, code in enumerate(codes):
        # loop again on all the strings after the current string
        # because already compared this string with the strings
        # prior to it in the list
        for code2 in codes[key+1:]:
            found_answer, answer_code = differ_by_one_char(code, code2)
            if found_answer:
                code_1 = code
                code_2 = code2
                break
        if found_answer:
            break
    # at this point the code should have found code and code 2
    # print(f'{code_1} and {code_2}')
    # print(f'Answer is {answer_code}')
    return answer_code



if __name__ == "__main__":

    # this if statement is to be able to run it from within VS Code
    if len(sys.argv) > 1:
        input_file = sys.argv[1]
    else:
        input_file = Path(__file__).stem + '.txt'

    print(part1(input_file))
    print(part2(input_file))

