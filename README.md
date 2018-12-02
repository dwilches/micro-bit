# Code samples for the BBC micro:bit

I got a micro:bit for reviewing an add-on called wear:it, while doing the review I created some small
programs, which you can find in the `src` folder of this repository.

The review can be found here:
[micro:bit wear:it Development Kit - Review](https://www.element14.com/community/roadTestReviews/2840/l/microbit-wearit-development-kit-review)

The API reference I used for creating these programs can be found here:
[BBC micro:bit MicroPython](https://microbit-micropython.readthedocs.io/en/latest/tutorials/introduction.html)

# Some recommendations

* Use [mu-editor](https://codewith.mu/) for uploading the code to the micro:bit but programming on it 
  is not as nice as programming in [PyCharm](https://www.jetbrains.com/pycharm/) (which shows you syntax error
  for example), so what I kept doing was programming in PyCharm and only using mu-editor to flash my program into 
  the micro:bit. 
* Use [microrepl](https://github.com/ntoll/microrepl) for  quickly testing code snippets. When testing how a module
  from the API works, instead of flashing your program into the micro:bit you can use microrepl which speeds the
  testing process. 

# Source contents

* [doggy-music](https://github.com/dwilches/micro-bit/blob/master/src/doggy-music.py). Can be attached to a dog's
  costume to play music when the dog sits for a picture, and stops when the dog stands up or is walking. Check the
  dog costume [here](https://www.element14.com/community/roadTestReviews/2840/l/microbit-wearit-development-kit-review).

* [beating-heart](https://github.com/dwilches/micro-bit/blob/master/src/beating-heart.py). Shows a heart in the
  micro:bit's display and change its intensity back and forth, so it looks like it's beating.

* [sound-wave](https://github.com/dwilches/micro-bit/blob/master/src/sound-wave.py). Shows an animation that resembles
  a sound-wave.
