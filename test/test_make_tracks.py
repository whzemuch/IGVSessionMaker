import unittest
from track_class import BedTrack, BigWigTrack
from make_tracks import _generate_one_track, generate_track_list

class TestTrackFunctions(unittest.TestCase):
    def test_generate_one_track(self):
        # Test BedTrack generation
        track = _generate_one_track('example.bed', 'color1')
        track.add_track()
        print(str(type(track)))
        self.assertIsInstance(track, BedTrack)
        self.assertEqual(track.ifile, 'example.bed')
        self.assertEqual(track.colour, 'color1')

        # Test BigWigTrack generation
        track = _generate_one_track('example.bw', 'color2')
        track.add_track()
        self.assertIsInstance(track, BigWigTrack)

        # Test unsupported file type
        track = _generate_one_track('example.unknown', 'color3')
        self.assertIsNone(track)

    def test_generate_track_list(self):
        file_data = [
            {'ifile': 'sample1.bed', 'colour': 'color1'},
            {'ifile': 'sample2.bw', 'colour': 'color2'},
            {'ifile': 'sample3.unknown', 'colour': 'color3'}
        ]
        
        track_list = generate_track_list(file_data)
        self.assertEqual(len(track_list), 2)
        self.assertIsInstance(track_list[0], BedTrack)
        self.assertIsInstance(track_list[1], BigWigTrack)

if __name__ == "__main__":
    unittest.main()
