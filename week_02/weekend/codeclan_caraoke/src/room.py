class Room:
    def __init__(self, id, type_of_music, max_capacity, entry_fee):
        self.id = id
        self.type_of_music = type_of_music
        self.guests_in_room = []
        self.max_capacity = max_capacity
        self._song_list = []
        self.entry_fee = entry_fee

    def check_total_guests_in_room(self):
        return len(self.guests_in_room)
                              
    def check_in_guest(self, guest):
        if len(self.guests_in_room) < self.max_capacity:
            self.guests_in_room.append(guest)
        else:
            return None

    def check_out_guest(self,guest):
        self.guests_in_room.remove(guest)

    def song_count(self):
        return len(self._song_list)
        
    def add_song_to_list(self,song):
        self._song_list.append(song)

    def customer_can_afford_entry(self, fee, wallet):
        if fee <= wallet:
            return True
        else:
            return False
        

    def check_favourtie_song(self, fav_song, song_list):
        if fav_song in song_list:
            return "Whoo"
        else:
           return None

        