from sense_hat import SenseHat
from time import sleep
sense = SenseHat()


while True:
        event = sense.stick.wait_for_event(emptybuffer=True)
        if event.direction == "left":
          sense.show_letter("X")
          sleep(5)
          sense.show_letter("A")
        elif event.direction == "right":
          sense.clear()
        