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

    def drop_off(self, person):
        self.passangers.remove(person)
    
    def empty_bus(self):
        self.passangers.clear()

    def pick_up_from_stop(self, bus_stop):
        BusStop.add_to_queue()

    

        

    
    
