class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = list(zip(position, speed))
        cars.sort()
        fleet, maxtime = 0, 0
        for pos, spd in cars[::-1]:
            time = (target - pos) / spd
            if time > maxtime:
                fleet += 1
                maxtime = time
        return fleet
