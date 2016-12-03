import RPi.GPIO as GPIO
import threading

LED_PIN     = 17
BUTTON_PIN  = 4


class PiThings(object):

    def __init__(self):
        GPIO.setwarnings(False)
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(LED_PIN, GPIO.OUT)
        GPIO.setup(BUTTON_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)
        self._lock = threading.Lock()
        self._button_callback = None
        GPIO.add_event_detect(BUTTON_PIN, GPIO.BOTH,
                              callback=self._button_change, bouncetime=20)

    def _button_change(self, pin):
        if self._button_callback is not None:
            self._button_callback(GPIO.input(BUTTON_PIN))


    def on_button_change(self, callback):
        self._button_callback = callback

    def read_button(self):
        with self._lock:
            return GPIO.input(BUTTON_PIN)

    def set_led(self, value):
        GPIO.output(LED_PIN, value)
