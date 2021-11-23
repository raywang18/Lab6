from LED8x8 import LED8x8
import multiprocessing
import time

if __name__ == "__main__":
    pattern = [0b00111100, 0b01000010, 0b10100101, 0b10000001, 
                0b10100101, 0b10011001, 0b01000010, 0b00111100]
    dataPin, latchPin, clockPin = 17, 27, 22
    multiArray = multiprocessing.Array('b', len(pattern))
    # initial values for multiprocessing Array
    for i in range(len(pattern)):
      multiArray[i] = pattern[i]
    display = LED8x8(dataPin, latchPin, clockPin, pattern)
    p1 = multiprocessing.Process(target=display.display, args=([multiArray]))
    p1.start()