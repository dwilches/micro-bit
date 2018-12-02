#
# Daniel Wilches
# Nov 2018
#
# This program is used in a dog's costume to play music when the dogs sits, and stop the music when the dog stands.
# This also shows a beating heart on the micro:bit's screen while the dog is seating.
#
#
# Snippet to know which values are returned by the accelerometer in your case, use this program inside of microrepl:
#
# from microbit import *
# while True:
#    sleep(100)
#    print(accelerometer.get_y())
#
#
# This code uses switch debouncnig, but what is a debounce?
#
#    The accelerometer's reading can change rapidly around the "dog sitting/standing threshold". If that happens, the
#    program would think that the dog is sitting and standing repeatedly, and that would start and stop the music very
#    quickly many times.
#
#    To avoid this, I use two different thresholds, a first threshold to detect when the dog is sitting, and another
#    to detect when the dog is standing. In the middle of the two thresholds there is a "grey area" in which we don't
#    know what the dog is doing, so we just hang on to the previous status (thus debouncing the state change).
#
#    This means, if the dog was sitting and we get to the grey area, we assume the dog is still sitting; but if the
#    dog was standing and we get to the grey area, then we assume it's still standing.
#

from microbit import *


# This is how the AudioFX board works: put the pin to GND and the music will start, set the pin to a logical 1 and the
# music stops.
MUSIC_ON = 0
MUSIC_OFF = 1


def main():
    # Accelerometer readings to know when the dog is standing (found using the snippet at the bottom of this file)
    dog_standing = (-600, 600)

    # Used to debounce the readings from the accelerometer.
    dog_not_sitting = (dog_standing[0] - 200, dog_standing[1] + 200)

    # We store here True if in the last iteration we thought the dog was standing
    was_dog_standing_last_time = False

    while True:
        reading = accelerometer.get_y()
        is_dog_standing_now = dog_standing[0] < reading < dog_standing[1];
        is_in_grey_area = dog_not_sitting[0] < reading < dog_not_sitting[1];

        # If the dog is standing (or in the grey area after standing) then stop the music
        if is_dog_standing_now or (was_dog_standing_last_time and is_in_grey_area):
            was_dog_standing_last_time = True
            pin0.write_digital(MUSIC_OFF)
            display.clear()  # Clear the heart-beat
        else:
            # It seems the dog is sitting (or in grey area after sitting), start the music
            was_dog_standing_last_time = False
            pin0.write_digital(MUSIC_ON)
            heart_beat()

        sleep(50)


# Look closely, this is a heart (it's inverted):
image = ("00100:"
         "01110:"
         "11111:"
         "11111:"
         "01010")

# Variables for controlling the dimming of the heart
make_dimmer = True
intensity = 1


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
