class Flight():
    def __init__(self, capacity):
        self.capacity = capacity
        self.passengers = []
    
    def addPassenger(self, name):
        if not self.openSeats(): # if self.openSeats() == 0: demek oluyor
            return False
        else:
            self.passengers.append(name)
            return True
    
    def openSeats(self):
        return self.capacity - len(self.passengers)

flight = Flight(3)

people = ["Harry", "Ron", "Hermione", "Ginny"]
for person in people:
    # success = 
    if flight.addPassenger(person):
        print(f"Added {person} to flight successfully.")
    else:
        print(f"No available seats for {person}")
