class Leds(object):
    def set_all(self, color):
        for i in range(5):
            set_led(i, color)

    def set_led(self, number, color):
        print("Setting led {} with a value of {}".format(number, color))
