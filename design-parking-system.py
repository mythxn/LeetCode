class ParkingSystem:
    def __init__(self, big: int, medium: int, small: int):
        self.spots = {}

        self.spots[1] = big
        self.spots[2] = medium
        self.spots[3] = small

    def addCar(self, carType: int) -> bool:
        if self.spots[carType] > 0:
            self.spots[carType] -= 1
            return True
        else:
            return False