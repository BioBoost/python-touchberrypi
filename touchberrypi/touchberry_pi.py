import smbus
from .leds import Leds
from .temperature_sensor import TemperatureSensor
from .touch_sensor import TouchSensor
from .accelerometer import Accelerometer

class TouchberryPi(object):
    I2C_ADDRESS_ACCELEROMETER = 0x1C
    I2C_ADDRESS_TOUCH_SENSOR = 0x1B

    def __init__(self):
        self.i2c_bus = smbus.SMBus(1)

        self.key_down_callback = None
        self.key_up_callback = None
        self.key_change_callback = None

        self.touch = TouchSensor(self.i2c_bus, TouchberryPi.I2C_ADDRESS_TOUCH_SENSOR)
        self.temperature_sensor = TemperatureSensor(self.i2c_bus)
        self.leds = Leds(self.i2c_bus)
        self.accelerometer = Accelerometer(self.i2c_bus, TouchberryPi.I2C_ADDRESS_ACCELEROMETER)

    def temperature(self):
        return self.temperature_sensor.temperature()

    def set_all_leds(self, color):
        self.leds.set_all(color)

    def set_led(self, index, color):
        self.leds.set_led(index, color)

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
