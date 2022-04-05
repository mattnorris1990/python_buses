class BusStop:
    def __init__(self, name):
        self.name = name
        self.queue = []

    def queue_length(self):
        return len(self.queue)

    def add_to_queue(self, person_1):
        self.queue.append(person_1)

    def clear(self):
        self.queue.clear()
