from pathlib import Path
import sys

def part1(input_file):
    with open(input_file,"r") as f:
        content = f.readlines()
        freq = 0
        for num in content:
            freq += int(num)
        return(freq)

def part2(input_file):
    freq_list = []
    with open(input_file,"r") as f:
        content = f.readlines()
        freq = 0
        freq_list.append(freq)
        while True:
            for num in content:
                freq += int(num)
                # print(freq)
                if freq in freq_list:
                    # print('Just repeated: ' + str(freq))
                    return freq
                else:
                    freq_list.append(freq)
            # print('Lenth of list is {}. Frequency is {}'.format(len(freq_list), freq))
    return None

if __name__ == "__main__":
    if len(sys.argv) > 1:
        input_file = sys.argv[1]
    else:
        script_dir = Path(__file__).resolve().parent
        input_file = script_dir / 'input1_1.txt'

    print(part1(input_file))
    print(part2(input_file))

