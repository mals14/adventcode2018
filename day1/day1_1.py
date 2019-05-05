from pathlib import Path
import sys

def main(input_file):
    with open(input_file,"r") as f:
        content = f.readlines()
        freq = 0
        for num in content:
            freq += int(num)
        print(freq)


if __name__ == "__main__":
    if len(sys.argv) > 1:
        input_file = sys.argv[1]
    else:
        script_dir = Path(__file__).resolve().parent
        input_file = script_dir / 'input1_1.txt'

    main(input_file)

