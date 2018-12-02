#
# Daniel Wilches
# Nov 2018
#
# This program shows a random animation similar to a sound-wave.
#

from random import random
from microbit import *

NUM_COLUMNS = 5
MAX_HEIGHT = 2

# Intensity of the LEDs
INTENSITY = 5

current_heights = [0] * NUM_COLUMNS
increasing = [False] * NUM_COLUMNS


def main():
    while True:
        advance_current_heights()
        show_wave()
        sleep(100)


def advance_current_heights():
    for col in range(NUM_COLUMNS):
        # If this column arrived at the max/min heights, don't try to increase/decrease it any further, instead
        # change the direction.
        if increasing[col] and current_heights[col] == MAX_HEIGHT:
            increasing[col] = not increasing[col]
        if not increasing[col] and current_heights[col] == 0:
            increasing[col] = not increasing[col]

        # The direction can also change randomly, which does the effect of setting the amplitude of the wave on that
        # column.
        if 0 < current_heights[col] < MAX_HEIGHT and random() > 0.5:
            increasing[col] = not increasing[col]

        # Apply the current directions to the wave, but just maybe :) (the 50% random is what makes this look like
        # a wave)
        if random() > 0.5:
            if increasing[col]:
                current_heights[col] += 1
            else:
                current_heights[col] -= 1


def show_wave():
    for col in range(NUM_COLUMNS):
        if current_heights[col] == 0:
            display.set_pixel(col, 0, 0)
            display.set_pixel(col, 1, 0)
            display.set_pixel(col, 2, INTENSITY)
            display.set_pixel(col, 3, 0)
            display.set_pixel(col, 4, 0)
        elif current_heights[col] == 1:
            display.set_pixel(col, 0, 0)
            display.set_pixel(col, 1, INTENSITY)
            display.set_pixel(col, 2, INTENSITY)
            display.set_pixel(col, 3, INTENSITY)
            display.set_pixel(col, 4, 0)
        else:
            display.set_pixel(col, 0, INTENSITY)
            display.set_pixel(col, 1, INTENSITY)
            display.set_pixel(col, 2, INTENSITY)
            display.set_pixel(col, 3, INTENSITY)
            display.set_pixel(col, 4, INTENSITY)

main()
