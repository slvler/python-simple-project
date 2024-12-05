class Bus:

    def __init__(self, name, model, year):
        self.name = name
        self.model = model
        self.year = year

    def drive(self):
        print("Bus name: "+ self.name)
