def read_file(filename):
    try:
        with open(filename, 'r') as file:
            for line in file:
                print(line.strip())  # strip() removes the newline character at the end
    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Call the function with 'sample.txt'
read_file('sample.txt')