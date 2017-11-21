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

    key_down_callback = None
    key_up_callback = None
    key_change_callback = None

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

    def on_key_up(self, callback):
        self.key_up_callback = callback
    
    def on_key_down(self, callback):
        self.key_down_callback = callback
    
    def on_key_change(self, callback):
        self.key_change_callback = callback

    def trigger(self, key):
        # self.touch_callback(key)
        self.key_change_callback(key, status)
        self.key_up_callback(change)
        self.key_down_callback(key)


touchberry_pi = TouchberryPi()

def get_temperature():
    return touchberry_pi.get_temperature()

def set_all_leds(color):
    touchberry_pi.set_all_leds(color)

def set_led(number, color):
    touchberry_pi.set_led(number, color)

def on_key_up(callback):
    touchberry_pi.on_key_up(callback)

def on_key_down(callback):
    touchberry_pi.on_key_down(callback)

def on_key_change(callback):
    touchberry_pi.on_key_change(callback)
