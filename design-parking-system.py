class ParkingSystem:
    def __init__(self, big, medium, small):
        """
        :type big: int
        :type medium: int
        :type small: int
        """
        self.spots = [big, medium, small]

    def addCar(self, carType):
        """
        :type carType: int
        :rtype: bool
        """
        self.spots[carType - 1] -= 1
        return self.spots[carType - 1] >= 0
