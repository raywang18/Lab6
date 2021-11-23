from shifter import Shifter

class LED8x8():

    def __init__(self, data, latch, clock, pattern):
        self.shifter = Shifter(data, latch, clock)
        self.pattern = pattern            
    
    def display(self):
        while True:
            for i in range(len(self.pattern)):
                self.shifter.shiftByte(self.pattern[i])
                self.shifter.shiftByte(1<<i)