#!/usr/bin/python3

"""

    I am using a sense hat module on RPi 4
    This is a old program I wrote a while before
    It can be used to set the orientation of the 
    LED matrix and display some sensor states

"""

from sense_hat import SenseHat
from time import sleep

sense = SenseHat()
sense.low_light = True # The LEDs are so bright!!!
sense.set_imu_config(True, True, True)

def main():
    try:
        print("Use the joystick to choose the LED matrix orientation where you can see the question mark correctly.")
        sense.show_letter("?")
        event = sense.stick.wait_for_event()
        direction = event.direction
        action = event.action

        if direction == "down":
            sense.set_rotation(0)
        elif direction == "left":
            sense.set_rotation(90)
        elif direction == "up":
            sense.set_rotation(180)
        elif direction == "right":
            sense.set_rotation(270)
        else:
            print("The orientation left unchanged")
        
        sleep(1)
        sense.show_message("Carleton")

        humidity = sense.get_humidity()
        print("Humidity: %s %%rH" % humidity)

        temp = sense.get_temperature()
        print("Temperature: %s C" % temp)

        pressure = sense.get_pressure()
        print("Pressure: %s Millibars" % pressure)

        orientation_rad = sense.get_orientation_radians()
        print("p: {pitch}, r: {roll}, y: {yaw}".format(**orientation_rad))

        orientation = sense.get_orientation_degrees()
        print("p: {pitch}, r: {roll}, y: {yaw}".format(**orientation))

        orientation = sense.get_orientation()
        print("p: {pitch}, r: {roll}, y: {yaw}".format(**orientation))

        north = sense.get_compass()
        print("North: %s" % north)

        raw = sense.get_compass_raw()
        print("x: {x}, y: {y}, z: {z}".format(**raw))

        gyro_only = sense.get_gyroscope()
        print("p: {pitch}, r: {roll}, y: {yaw}".format(**gyro_only))

        raw = sense.get_gyroscope_raw()
        print("x: {x}, y: {y}, z: {z}".format(**raw))

        accel_only = sense.get_accelerometer()
        print("p: {pitch}, r: {roll}, y: {yaw}".format(**accel_only))

        raw = sense.get_accelerometer_raw()
        print("x: {x}, y: {y}, z: {z}".format(**raw))

        
    except KeyboardInterrupt:
        print("\nInterrupted, quit.")
        sense.clear()


if __name__ == "__main__":
    main()
    sense.clear()