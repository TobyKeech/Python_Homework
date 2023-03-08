from src.bus_stop import BusStop
class Bus:
    def __init__(self, route_number, destination):
        self.route_number = route_number
        self.destination = destination
        self.passangers = []
       
    def drive(self):
        return "Brum brum"
    
    def passenger_count(self):
        return len(self.passangers)
    
    def pick_up(self, new_person):
        self.passangers.append(new_person)
    
    def pick_up_from_stop(self,bus_stop):
       
        for person in bus_stop.queue:
            self.pick_up(person)
        # another way of doing it using one line
        # self.passangers.extend(bus_stop.queue)
        bus_stop.clear_queue()
        

    def drop_off(self, person):
        self.passangers.remove(person)
    
    def empty_bus(self):
        self.passangers.clear()

    