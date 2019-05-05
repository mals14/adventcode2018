from pathlib import Path
import sys

def main(input_file):
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
                    print('Just repeated: ' + str(freq))
                    return freq
                else:
                    freq_list.append(freq)
            # print('Lenth of list is {}. Frequency is {}'.format(len(freq_list), freq))
    return None


if __name__ == "__main__":

    # this if statement is to be able to run it from within VS Code
    if len(sys.argv) > 1:
        input_file = sys.argv[1]
    else:
        script_dir = Path(__file__).resolve().parent
        input_file = script_dir / 'input1_2.txt'

    print('2nd repeat for: ' + str(main(input_file)))

