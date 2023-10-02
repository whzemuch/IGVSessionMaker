import unittest
from track_class import GTfTrack
from pathlib import Path

class TestGTfTrack(unittest.TestCase):

    def test_add_track(self):
        # Setup
        track = GTfTrack("example.gtf", "red")

        # Test
        track.add_track()

        # Expected XML string
        expected_name = Path("example.gtf").name
        expected_XMLStr = (
            '\t\t<Track altColor="0,0,178" autoScale="false" clazz="org.broad.igv.track.FeatureTrack" color="red" '
            'displayMode="COLLAPSED" featureVisibilityWindow="-1" fontSize="10" '
            f'id="example.gtf" name="{expected_name}" renderer="BASIC_FEATURE" sortable="false" visible="true" windowFunction="count"/>\n'
        )

        # Assert
        self.assertEqual(track.XMLStr, expected_XMLStr)

if __name__ == "__main__":
    unittest.main()
