class Car(object):
    def __init__(self,color,model,company,speedLimit,amt):
        self.color=color
        self.model=model
        self.company=company
        self.speedLimit=speedLimit
        self.amt=amt 

    def start(self):
        print("Started")
    
    def accelerate(self):
        print("Accelerating")

    def stop(self):
        print("Stop")

    def changeGear(self):
        print("Gear Changed")


innova=Car("beige","crysta","toyota","250 km","false")

innova.start()
innova.accelerate()

