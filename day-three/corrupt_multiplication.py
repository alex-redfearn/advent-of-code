import re
from functools import reduce
from operator import mul


class CorruptMultiplication:

    def __init__(self, corrupt_data):
        self.corrupt_data = corrupt_data

    def multiply(self):
        total = 0

        for mul in self.__uncorrupt():
            total += self.__multiply(mul)

        return total

    def __uncorrupt(self):
        muls = []
        for data in self.__do(self.corrupt_data):
            muls.extend(re.findall(r"mul\([0-9]{1,3},[0-9]{1,3}\)", data))
        return muls

    @staticmethod
    def __do(corrupt_data):
        do = []

        for data in corrupt_data.split("do()"):
            do.append(data.split("don't()")[0])

        return do

    @staticmethod
    def __multiply(mul):
        nums = re.findall(r"\d+", mul)
        return int(nums[0]) * int(nums[1])
