import smbus
from .leds import Leds
from .temperature_sensor import TemperatureSensor
from .touch_sensor import TouchSensor

class TouchberryPi(object):

    def __init__(self):
        self.i2c_bus = smbus.SMBus(1)

        self.key_down_callback = None
        self.key_up_callback = None
        self.key_change_callback = None

        self.touch = TouchSensor(self.i2c_bus)
        self.temperature_sensor = TemperatureSensor()
        self.leds = Leds()

    def get_temperature(self):
        return self.temperature_sensor.get_temperature()

    def set_all_leds(self, color):
        self.leds.set_all(color)

    def set_led(self, number, color):
        self.leds.set_led(number, color)

    def on_key_up(self, callback):
        self.key_up_callback = callback

    def on_key_down(self, callback):
        self.key_down_callback = callback

    def on_key_change(self, callback):
        self.key_change_callback = callback

    # To be removed later on (testing)
    def get_touch(self):
        return self.touch

    # def trigger(self, key):
    #     self.key_change_callback(key, state)
    #     self.key_up_callback(key)
    #     self.key_down_callback(key)
