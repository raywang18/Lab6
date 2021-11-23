from LED8x8 import LED8x8
import multiprocessing
import random
import time

if __name__ == "__main__":
    dataPin, latchPin, clockPin = 17, 27, 22
    pattern = multiprocessing.Array('b', 8)
    led_display = LED8x8(dataPin, latchPin, clockPin)
    def display_fn(pattern):
      led_display.display(pattern)
    p1 = multiprocessing.Process(target=display_fn, args=([pattern]))
    p1.daemon = True
    p1.start()
    for i in range(len(pattern)):
      pattern[i] = 0b11111111
    x = 0
    y = 0
    while True:
      dx = random.randint(-1, 1)
      dy = random.randint(-1, 1)

      if x+dx<=7 and x+dx>=0:
        x += dx
      if y+dy<=7 and y+dy>=0:
        y += dy

      pattern[y] = ~(0b10000000 >> x) & 0b11111111
      time.sleep(0.1)