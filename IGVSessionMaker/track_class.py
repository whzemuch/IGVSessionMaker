# Define the Protocol for a Track
from pathlib import Path
from typing import Protocol




class Track(Protocol):
    XMLStr: str
    def add_track(self) -> None:
        ...

# Refactored BedTrack based on the Track Protocol
class BedTrack:
    def __init__(self, ifile: str, colour: str):
        self.ifile = ifile
        self.colour = colour
        self.XMLStr = ""

    def add_track(self):
        self.XMLStr += (
            '\t\t<Track altColor="0,0,178" autoScale="false" clazz="org.broad.igv.track.FeatureTrack" color="%s" '
            % (self.colour)
        )
        self.XMLStr += 'displayMode="SQUISHED" featureVisibilityWindow="-1" fontSize="10" height="20" '
        self.XMLStr += (
            'id="%s" name="%s" renderer="BASIC_FEATURE" sortable="false" visible="true" windowFunction="count"/>\n'
            % (self.ifile, Path(self.ifile).name)
        )

# Refactored BigWigTrack based on the Track Protocol
class BigWigTrack:
    def __init__(self, ifile: str, colour: str):
        self.ifile = ifile
        self.colour = colour
        self.XMLStr = ""

    def add_track(self):
        self.XMLStr += (
            '\t\t<Track altColor="0,0,178" autoScale="true" clazz="org.broad.igv.track.DataSourceTrack" color="%s" '
            % (self.colour)
        )
        self.XMLStr += 'displayMode="COLLAPSED" featureVisibilityWindow="-1" fontSize="10" height="30" '
        self.XMLStr += (
            'id="%s" name="%s" normalize="false" renderer="BAR_CHART" sortable="true" visible="true" windowFunction="mean">\n'
            % (self.ifile, Path(self.ifile).name)
        )
        self.XMLStr += '\t\t\t<DataRange baseline="0.0" drawBaseline="true" flipAxis="false" maximum="10" minimum="0.0" type="LINEAR"/>\n'
        self.XMLStr += "\t\t</Track>\n"

# Refactored GTfTrack based on the Track Protocol
class GTfTrack:
    def __init__(self, ifile: str, colour: str):
        self.ifile = ifile
        self.colour = colour
        self.XMLStr = ""

    def add_track(self):
        self.XMLStr += (
            '\t\t<Track altColor="0,0,178" autoScale="false" clazz="org.broad.igv.track.FeatureTrack" color="%s" '
            % (self.colour)
        )
        self.XMLStr += 'displayMode="COLLAPSED" featureVisibilityWindow="-1" fontSize="10" '
        self.XMLStr += (
            'id="%s" name="%s" renderer="BASIC_FEATURE" sortable="false" visible="true" windowFunction="count"/>\n'
            % (self.ifile, Path(self.ifile).name)
        )