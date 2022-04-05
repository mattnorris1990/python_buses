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

    
    # suggested solution
    # def pick_up_from_stop(self, bus_stop_to_pick_up_from):
    #     for passenger in bus_stop_to_pick_up_from.queue:
    #         self.passengers.append(passenger)
    #     bus_stop_to_pick_up_from.clear()



    
