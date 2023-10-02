
from pathlib import Path
from typing import Protocol, List, Type, Dict, Optional
from track_class import Track
from make_tracks import generate_track_list
from read_csv import read_file_color

REF_GENE_PANEL = """
    <Panel height="100" name="FeaturePanel" width="1640">
        <Track attributeKey="Reference sequence" clazz="org.broad.igv.track.SequenceTrack" fontSize="20" id="Reference sequence" name="Reference sequence" sequenceTranslationStrandValue="POSITIVE" shouldShowTranslation="false" visible="true"/>
        <Track attributeKey="Refseq Genes" clazz="org.broad.igv.track.FeatureTrack" colorScale="ContinuousColorScale;0.0;836.0;255,255,255;0,0,178" fontSize="20" groupByStrand="false" id="https://hgdownload.soe.ucsc.edu/goldenPath/hg38/database/ncbiRefSeq.txt.gz" name="Refseq Genes" visible="true"/>
    </Panel>
    <PanelLayout dividerFractions="0.8699731903485255"/>
    <HiddenAttributes>
        <Attribute name="DATA FILE"/>
        <Attribute name="DATA TYPE"/>
        <Attribute name="NAME"/>
     </HiddenAttributes>
"""


class IGVSession:
    def __init__(self, XMLOut, fileList, Genome, PathPrefix=""):
        self.XMLOut = Path(XMLOut)
        self.Genome = Genome
        self.PathPrefix = PathPrefix
        
        self.fileList = fileList
        self.XMLStr = '<?xml version="1.0" encoding="UTF-8" standalone="no"?>\n'

    def _add_resources_section(self):
        self.XMLStr += '<Session genome="%s" hasGeneTrack="true" hasSequenceTrack="true" locus="All" version="8">\n' % (self.Genome)
        self.XMLStr += "\t<Resources>\n"
        for item in self.fileList:
            self.XMLStr += '\t\t<Resource path="%s"/>\n' % (item.get("ifile", ''))
        self.XMLStr += "\t</Resources>\n"



    def _add_panel_section(self):
        self.XMLStr += '\t<Panel height="1160" name="DataPanel" width="1897">\n'
        for item in generate_track_list(self.fileList):
            self.XMLStr += item.XMLStr
        self.XMLStr += "\t</Panel>\n"
        self.XMLStr += REF_GENE_PANEL
        
   

        

    def generate_session(self):
        self._add_resources_section()
        self._add_panel_section()
        self.XMLStr += "</Session>"

    def write_session(self):
        self.XMLOut.write_text(self.XMLStr)
        
  
if __name__ == "__main__":
    fileList = read_file_color("12345.csv")
    # for file in fileList:
    #     print(file)
    igv_xml = IGVSession("12345.xml", fileList=fileList, Genome="hg38")
    igv_xml.generate_session()
    igv_xml.write_session()
    
          
