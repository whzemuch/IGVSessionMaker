
import csv
import argparse
from pathlib import Path

def read_file_color(csv_path):
    """
    Validate that the CSV has two columns: one for file and one for color.
    Returns a list of tuples with (file, color).
    """
    with open(csv_path, "r") as fin:
        reader = csv.DictReader(fin)
        if "file" not in reader.fieldnames or "color" not in reader.fieldnames:
            raise ValueError(f"CSV should have 'file' and 'colour' columns. Found: {reader.fieldnames}")

        fileList = []
        for row in reader:
            ifile = row["file"]
            colour = row["color"].strip() if row["color"].strip() else "0,0,178"
            fileList.append({"ifile": ifile, "colour": colour,
                             "name": Path(ifile).name, "stem":Path(ifile).stem})

    return fileList

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Validate CSV content for file and color columns.")
    parser.add_argument("csv_path", type=str, help="Path to the CSV file to be validated.")
    args = parser.parse_args()
    
    validated_content = read_file_color(args.csv_path)
    for entry in validated_content:
        print(entry)
