class Bus:
    def __init__(self, route_number, destination):
        self.route_number = route_number
        self.destination = destination
        self.passengers = []

    def drive(self):
        return "Brum brum"

    def passenger_count(self):
        return len(self.passengers)

    def pick_up(self, passenger_1):
        self.passengers.append(passenger_1)
    
    def drop_off(self, passenger_1):
        self.passengers.remove(passenger_1)

    def empty(self):
        self.passengers.clear()

    def pick_up_from_stop(self, input_bus_stop):
        passengers = input_bus_stop.queue
        
        self.passengers.extend(passengers)
        return input_bus_stop.queue_length()


    
