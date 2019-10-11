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

def main(input_file):
    print(f'checksum is {get_checksum(input_file)}')

def get_input_file_name(fileName):
    """Get the number after day and before underscore.

    Arguments:
        __file__ {string} -- [description]

    Returns:
        [string] -- [script trailing number]
    """
    import re
    regex = r'day(\d+)_'
    dayNumber = re.search(regex, fileName)[1]
    return dayNumber

if __name__ == "__main__":

    # this if statement is to be able to run it from within VS Code
    if len(sys.argv) > 1:
        input_file = sys.argv[1]
    else:
        script_dir = Path(__file__).resolve().parent
        inputFileNumber = get_input_file_name(__file__)
        input_file = script_dir / "input_files" / f'input{inputFileNumber}.txt'

    main(input_file)

