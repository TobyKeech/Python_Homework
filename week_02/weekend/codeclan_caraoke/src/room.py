class Room:
    def __init__(self, id, type_of_music, max_capacity):
        self.id = id
        self.type_of_music = type_of_music
        self.guests_in_room = []
        self.max_capacity = max_capacity
        self._song_list = []

    def check_total_guests_in_room(self):
        return len(self.guests_in_room)
                              
    def check_in_guest(self, guest):
        self.guests_in_room.append(guest) 

    def check_out_guest(self,guest):
        self.guests_in_room.remove(guest)

    def song_count(self):
        return len(self._song_list)
        
    def add_song_to_list(self,song):
        self._song_list.append(song)

    # def add_to_capacity(self,amount):
    #     self.max_capacity =+ amount