import unittest
from src.room import Room 
from src.guest import Guest
from src.song import Song

class TestRoom(unittest.TestCase):
    def setUp(self):
        self.guest_1 = Guest("Toby", 26, 75.00)
        self.guest_2 = Guest("Meg", 28, 150.00)
        self.guest_3 = Guest("Bob", 22, 15.00)
        self.guests_in_room = [self.guest_1, self.guest_2]

        self.room = Room(1,"hip hop", 9)

        self.song_1 = Song("Sweet Caroline", "Neil Diamond", 4.39)
        self.song_2 = Song("500 miles", "Pro Claimers", 3.85)
        self.song_3 = Song("Sweet Home Alabama", "Lynyrd Skynyrd", 4.02)

        self._song_list  = [self.song_1, self.song_2]

    def test_has_room_id(self):
        self.assertEqual( 1, self.room.id) 

    def test_type_of_music(self):
        self.assertEqual("hip hop", self.room.type_of_music)

    def test_total_guests_in_room(self):
        self.assertEqual(0, self.room.check_total_guests_in_room())

    def test_max_capacity_in_room(self):
        self.assertEqual(9, self.room.max_capacity)

    def test_check_in_guest(self):
        self.room.check_in_guest(self.guest_3)
        self.assertEqual(1, self.room.check_total_guests_in_room())

    def test_check_out_guest(self):
        guest = Guest("Dave", 32, 300.00)
        self.room.check_in_guest(guest)
        self.room.check_out_guest(guest)
        self.assertEqual(0, self.room.check_total_guests_in_room())
    
    def test_song_list_begins_at_0(self):
       self.assertEqual(0, self.room.song_count())
        
    def test_add_song_to_list(self):
        self.room.add_song_to_list(self.song_3)
        self.assertEqual(1, self.room.song_count())


    # def test_add_to_capacity(self):
    #     self.room.add_to_capacity(2)
    #     self.assertEqual(11, self.room.max_capacity)


    # def test_capacity_checker(self,guest):
    #     guest  = 1

    #     self.room.capacity_checker(self,guest)
    #     self.assertEqual("Sorry no space", self.room.max_capacity)
