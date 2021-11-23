import time
from led_display import LEDdisplay

# Simple demonstration of the LEDdisplay class.
# Note that we don't need RPi.GPIO here since all the I/O
# is done through the LEDdisplay class (we do however need
# to define the GPIO pins, since LEDdisplay is
# pin-agnostic).

dataPin, latchPin, clockPin = 17, 27, 22

# Pick a number sequence
sequence = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]

theLEDdisplay= LEDdisplay(dataPin, latchPin, clockPin)

while True:
  for n in range(len(sequence)):
    theLEDdisplay.setNumber(sequence[n])
    time.sleep(0.4)