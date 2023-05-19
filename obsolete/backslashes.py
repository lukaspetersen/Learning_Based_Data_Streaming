import sys
import time

def remove_backslashes(filename):
    # Read the CSV file
    with open(filename, 'r', encoding='utf-8') as file:
        content = file.read()

    # Remove backslashes
    content = content.replace('\\', '')

    # Write the modified content back to the CSV file
    timestamp = time.strftime("%Y%m%d-%H%M%S")
    output_filename = f'output_no_backslashes_{timestamp}.csv'
    with open(output_filename, 'w', encoding='utf-8') as file:
        file.write(content)

    print(f"Output written to: {output_filename}")

def main():
    filename = sys.argv[1]
    remove_backslashes(filename)

if __name__ == "__main__":
    main()
