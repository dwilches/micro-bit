#
# Daniel Wilches
# Nov 2018
#
# This program shows a beating heart on the micro:bit's screen.
#

from microbit import *

# Look closely, this is a heart:
image = ("01010:"
         "11111:"
         "11111:"
         "01110:"
         "00100")

# Variables for controlling the dimming of the heart
make_dimmer = True
intensity = 1


def main():
    while True:
        heart_beat()
        sleep(50)


def heart_beat():
    global intensity, make_dimmer

    # If make_dimmer is True, then we reduce the intensity until we reach 1. When we reach 1 we set make_dimmer = False
    # so we start increasing the intensity. When the intensity reaches the max (9) we set make_dimmer = True again.
    new_image = image.replace('1', str(intensity))
    display.show(Image(new_image))

    if intensity == 9 or intensity == 1:
        make_dimmer = not make_dimmer

    intensity = intensity + (-1 if make_dimmer else 1)


main()
