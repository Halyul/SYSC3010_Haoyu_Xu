#!/usr/bin/python3

from sense_hat import SenseHat
sense = SenseHat()
sense.low_light = True # The LEDs are so bright!!!
initials = [
  "H",
  "X"
  ]
counter = 0
exit = False

def show(letter):
  sense.show_letter(letter)

while exit is False:
    try : 
        show(initials[counter % 2])
        counter += 1
        # a complete joystick action
        sense.stick.wait_for_event()
        sense.stick.wait_for_event(emptybuffer=True)
    except KeyboardInterrupt:
        print("\nInterrupted, quit.")
        sense.clear()
        exit = not exit