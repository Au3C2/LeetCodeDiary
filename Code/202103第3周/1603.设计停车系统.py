'''
Description: 
Autor: Au3C2
Date: 2021-03-19 10:17:29
LastEditors: Au3C2
LastEditTime: 2021-03-19 10:17:48
'''
class ParkingSystem:

    def __init__(self, big: int, medium: int, small: int):
        
        self.slot = {1:big, 2:medium, 3:small}

    def addCar(self, carType: int) -> bool:
        
        if self.slot[carType] > 0:
            self.slot[carType] -= 1
            return True
        else:
            return False


# Your ParkingSystem object will be instantiated and called as such:
# obj = ParkingSystem(big, medium, small)
# param_1 = obj.addCar(carType)

# 设计，简单。奇怪的题目
# https://leetcode-cn.com/problems/design-parking-system/