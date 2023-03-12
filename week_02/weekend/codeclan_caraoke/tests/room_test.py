import unittest
from src.room import Room 
from src.guest import Guest
from src.song import Song

class TestRoom(unittest.TestCase):
    def setUp(self):
        self.guest_1 = Guest("Toby", 26, 75.00, "500 miles" )
        self.guest_2 = Guest("Meg", 28, 150.00, "evacuate the dance floor")
        self.guest_3 = Guest("Bob", 22, 15.00, "Sweet Home Alabama")
        self.guests_in_room = [self.guest_1, self.guest_2]

        self.room_1 = Room(1,"hip hop", 12, 10)
        self.room_2 = Room(2, "rock", 2, 5)

        self.song_1 = Song("Sweet Caroline", "Neil Diamond", 4.39)
        self.song_2 = Song("500 miles", "Pro Claimers", 3.85)
        self.song_3 = Song("Sweet Home Alabama", "Lynyrd Skynyrd", 4.02)
        self._song_list  = [self.song_1, self.song_2]

    def test_has_room_id(self):
        self.assertEqual( 2, self.room_2.id) 

    def test_type_of_music(self):
        self.assertEqual("hip hop", self.room_1.type_of_music)

    def test_total_guests_in_room(self):
        self.assertEqual(0, self.room_1.check_total_guests_in_room())

    def test_max_capacity_in_room(self):
        self.assertEqual(12, self.room_1.max_capacity)
    
    def test_room_has_entry_fee(self):
        self.assertEqual(10, self.room_1.entry_fee)

    def test_check_in_guest(self):
        self.room_1.check_in_guest(self.guest_3)
        self.assertEqual(1, self.room_1.check_total_guests_in_room())

    def test_check_out_guest(self):
        guest = Guest("Dave", 32, 300.00, "power")
        self.room_1.check_in_guest(guest)
        self.room_1.check_out_guest(guest)
        self.assertEqual(0, self.room_1.check_total_guests_in_room())


    def test_rooms_wont_add_if_above_max_capacity(self):
        self.room_2.check_in_guest(self.guest_1)
        self.room_2.check_in_guest(self.guest_2)
        self.assertEqual(2, len(self.room_2.guests_in_room))
        self.room_2.check_in_guest(self.guest_3)
        self.assertEqual(2, len(self.room_2.guests_in_room))


    def test_song_list_begins_at_0(self):
       self.assertEqual(0, self.room_1.song_count())
        
    def test_add_song_to_list(self):
        self.room_1.add_song_to_list(self.song_3)
        self.room_1.add_song_to_list(self.song_2)
        self.assertEqual(2, self.room_1.song_count())

    def test_customer_can_afford_entry(self):
        self.room_1 = Room(1,"hip hop", 12, 10)
        self.guest_1 = Guest("Toby", 26, 75.00, "500 miles" )            

        can_afford_entry = self.room_1.customer_can_afford_entry(self.room_1.entry_fee, self.guest_1.wallet)
        self.guest_1.reduce_wallet(self.room_1.entry_fee)
        self.assertEqual(65.00, self.guest_1.wallet)
        self.assertEqual(can_afford_entry, True)

    def test_customers_favourite_sing_in_room(self):
        self.room_1.add_song_to_list(self.song_3.name)
        self.room_1.add_song_to_list(self.song_2.name)

        guest_fav_song_in_room = self.room_1.check_favourtie_song(self.guest_1.favourite_song, self.room_1._song_list)
        self.assertEqual("500 miles", self.guest_1.favourite_song)
        self.assertEqual(2, len(self.room_1._song_list))
        self.assertEqual("Whoo", guest_fav_song_in_room)
