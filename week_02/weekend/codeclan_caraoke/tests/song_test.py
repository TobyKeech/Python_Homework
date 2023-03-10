import unittest
from src.song import Song

class TestSong(unittest.TestCase):
    def setUp(self):
        
        self.song = Song("You Raise Me Up", "Westlife", 2.30)

    def test_song_has_name(self):
        self.assertEqual("You Raise Me Up", self.song.name)
    
    def test_song_has_artist(self):
        self.assertEqual("Westlife", self.song.artist)
        
    def test_length_of_song(self):
        self.assertEqual(2.30, self.song.length_of_song)

    