from shifter import Shifter
import time

class LED8x8():

    def __init__(self, data, latch, clock, pattern):
        self.shifter = Shifter(data, latch, clock)
        self.pattern = pattern            
    
    def display(self, multiArray):
        while True:
            for i in range(len(self.pattern)):
                multiArray[i] = self.pattern[i]
                self.shifter.shiftByte(self.pattern[i])
                self.shifter.shiftByte(1<<i)
                time.sleep(0.001)