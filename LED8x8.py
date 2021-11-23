from shifter import Shifter
import time

class LED8x8():

    def __init__(self, data, latch, clock):
        self.shifter = Shifter(data, latch, clock)            
    
    def display(self, pattern):
        while True:
            for i in range(len(pattern)):
                self.shifter.shiftByte(pattern[i])
                self.shifter.shiftByte(1<<i)
                time.sleep(0.001)