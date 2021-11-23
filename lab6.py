from LED8x8 import LED8x8

pattern = [0b00111100, 0b01000010, 0b10100101, 0b10000001, 
0b10100101, 0b10011001, 0b01000010, 0b00111100]

if __name__ == "__main__":
    dataPin, latchPin, clockPin = 17, 27, 22
    LEDdisplay = LED8x8(dataPin, latchPin, clockPin, pattern)
    LEDdisplay.display()