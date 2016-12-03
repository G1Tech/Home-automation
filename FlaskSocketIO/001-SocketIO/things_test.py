import time
import things

pi_things = things.PiThings()
button = pi_things.read_button()


def button_change(button):
    if button:
        print('Button is OFF!')
    else:
        print('Button is ON!')


pi_things.on_switch_change(button_change)

while True:
    pi_things.set_led(True)
    time.sleep(0.25)
    pi_things.set_led(False)
    time.sleep(0.25)
