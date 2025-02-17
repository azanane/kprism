class Process:
    def __init__(self, name = "", delay = "", needs = {}, results = {}, cost = 0, delay_to_make = 0):
        self.name = name
        self.needs = needs  # Using a set to represent needs (hashable items)
        self.results = results  # Using a set to represent results (hashable items)
        self.delay = delay
        self.cost = cost

    def add_need(self, name, quantity):
        self.needs[name] = quantity
    
    def add_result(self, name, quantity):
        self.results[name] = quantity

    def __lt__(self, other):
        # Compare based on the delay
        return self.delay < other.delay
