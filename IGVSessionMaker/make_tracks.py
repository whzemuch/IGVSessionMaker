from pathlib import Path
from .track_class import Track, BedTrack, BigWigTrack, GTfTrack
from typing import   List, Type, Dict, Optional
from .read_csv import read_file_color

# Track class mapping configuration
TRACK_CLASS_MAPPING: Dict[str, Type[Track]] = {
    ".bed": BedTrack,
    ".broadpeak": BedTrack,
    ".narrowpeak": BedTrack,
    ".bw": BigWigTrack,
    ".bigwig": BigWigTrack,
    ".tdf": BigWigTrack,
    ".gtf": GTfTrack
    # Add other mappings as needed
}


def _generate_one_track(ifile_str: str, colour: str) -> Optional[Track]:
    """
    Generates a single Track object based on the given file path and color.
    
    Parameters:
        - ifile_str: The file path.
        - colour: The color.
    
    Returns:
        - An instance of the corresponding Track object or None if the file type is not recognized.
    """
    ifile = Path(ifile_str)
    track_func = TRACK_CLASS_MAPPING.get(ifile.suffix.lower(), '')
    
    if track_func:
        track = track_func(ifile_str, colour)
        track.add_track()
        return track
    

def generate_track_list(file_data: List[dict]) -> List[Track]:
    """
    Generates a list of Track objects based on the given file data.
    
    Parameters:
        - file_data: A list of tuples. Each tuple consists of a file path and a color.
    
    Returns:
        - A list of Track objects.
    """
    track_lst = []
    for item in file_data:
        ifile_str = item.get('ifile', '')
        colour = item.get('colour', '')
        track = _generate_one_track(ifile_str, colour)
        if track:
            track_lst.append(track)
    return track_lst
 
if __name__ == "__main__":
    # parser = argparse.ArgumentParser(description="Make tracks for igv.")
    # parser.add_argument("csv_path", type=str, help="Path to the CSV file to be validated.")
    # args = parser.parse_args()
    
    # fileList = read_file_color(args.csv_path)
    # tracks = generate_track_list(fileList)
    
    # for track in tracks:
    #     print(track)
    file_data = [
            {'ifile': 'sample1.bed', 'colour': 'color1'},
            {'ifile': 'sample2.bw', 'colour': 'color2'},
            {'ifile': 'sample3.unknown', 'colour': 'color3'}
        ]
    track_list = generate_track_list(file_data)
    for track in track_list:
        print(track.XMLStr)
    # track = _generate_one_track('example.bw', 'color1')
    # track.add_track() 
    # print(track.XMLStr)  
    
    
    
