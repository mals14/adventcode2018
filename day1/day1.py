from pathlib import Path

script_dir = Path(__file__).resolve().parent
input_file = script_dir / 'input.txt'

print(input_file)

with open(input_file,"r") as f:
    content = f.readlines()
    freq = 0
    for num in content:
        freq += int(num)
    print(freq)