
def main():
    return

if __name__ == "__main__":

    # this if statement is to be able to run it from within VS Code
    if len(sys.argv) > 1:
        input_file = sys.argv[1]
    else:
        script_dir = Path(__file__).resolve().parent
        input_file = script_dir / 'input2_1.txt'

    main(input_file)