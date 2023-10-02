from pathlib import Path
import pandas as pd
from typing import Union, List

def get_file_list(input_dir: Union[Path, str], 
                  file_extensions: List[str], 
                  csv_file: Union[Path, str], 
                  color: str = "blue") -> pd.DataFrame:
    
    # Convert input_dir and csv_file to Path objects if they're not already
    input_dir = Path(input_dir)
    csv_file = Path(csv_file)
    
    # List to store matched files
    matched_files = []
    
    # Loop through each file extension and glob for matching files
    for ext in file_extensions:
        matched_files.extend(input_dir.glob(f'**/*.{ext}'))
    
    # Get the relative paths of matched files
    relative_files = [file.relative_to(input_dir).as_posix() for file in matched_files]
    
    # Construct a DataFrame
    df = pd.DataFrame({
        'file': relative_files,
        'color': [color] * len(relative_files)
    })
    
    # Write the DataFrame to a CSV file
    df.to_csv(csv_file, index=False)
    
    return df

if __name__ == "__main__":
    df = get_file_list("/Users/whzemuch/Box/ChenLab_Bioinformatics/BioinfoServices/_cProject_Bishop_Lab",
                       ["bigWig", "bw"], "12345.csv", "red")
