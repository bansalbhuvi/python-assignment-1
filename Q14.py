def read_lines():
    lines = []
    while True:
        line = input("Enter a line (press Enter to finish): ")
        if not line:
            break
        lines.append(line)
    return lines

def main():
    print("Enter multiple lines. Press Enter on an empty line to finish.")
    lines = read_lines()
    print("\nYou entered the following lines:")
    for line in lines:
        print(line)

if __name__ == "__main__":
    main()
