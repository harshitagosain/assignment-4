def write_to_file(filename):
    """
    Takes user input and writes it to the specified file (overwriting if it exists).
    """
    user_input = input("Enter some text to write to the file: ")
    with open(filename, 'w') as file:
        file.write(user_input + '\n')
    print("Data written to file successfully.")


def append_to_file(filename):
    """
    Takes additional user input and appends it to the specified file.
    """
    additional_input = input("Enter additional text to append to the file: ")
    with open(filename, 'a') as file:
        file.write(additional_input + '\n')
    print("Data appended to file successfully.")


def read_file(filename):
    """
    Reads and displays the content of the specified file.
    """
    print("\nFinal contents of the file:")
    try:
        with open(filename, 'r') as file:
            for line in file:
                print(line.strip())
    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")


def main():
    """
    Main function to run the full write-append-read process.
    """
    filename = 'output.txt'
    write_to_file(filename)
    append_to_file(filename)
    read_file(filename)


if __name__ == '__main__':
    main()