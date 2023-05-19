import sys
import csv

def crop_csv(filename, X):
    # Read the CSV file
    with open(filename, 'r', newline='') as file:
        reader = csv.reader(file)
        rows = [next(reader) for _ in range(X)]

    # Write the cropped rows to a new CSV file
    cropped_filename = f'cropped_{X}_{filename}'
    with open(cropped_filename, 'w', newline='') as file:
        writer = csv.writer(file, quoting=csv.QUOTE_ALL)
        writer.writerows(rows)

    print(f"Cropped CSV file saved as: {cropped_filename}")

def main():
    filename = sys.argv[1]
    X = int(sys.argv[2])
    crop_csv(filename, X)

if __name__ == "__main__":
    main()