class TemperatureSensor(object):

    def get_temperature(self):
        return 23.45

class Leds(object):
    def set_all(self, color):
        for i in range(5):
            set_led(i, color)
    
    def set_led(self, number, color):
        print("Setting led {} with a value of {}".format(number, color))


class TouchberryPi(object):

    i2c_bus = None

    touch_callback = None

    def __init__(self):
        self.temperature_sensor = TemperatureSensor()
        self.leds = Leds()

    def get_temperature(self):
        return self.temperature_sensor.get_temperature()

    def set_all_leds(self, color):
        self.leds.set_all(color)

    def set_led(self, number, color):
        self.leds.set_led(number, color)
        # self.trigger("A")

    def attach(self, callback):
        self.touch_callback = callback

    def trigger(self, key):
        self.touch_callback(key)


touchberry_pi = TouchberryPi()

def get_temperature():
    return touchberry_pi.get_temperature()

def set_all_leds(color):
    touchberry_pi.set_all_leds(color)

def set_led(number, color):
    touchberry_pi.set_led(number, color)

def attach(callback):
    touchberry_pi.attach(callback)