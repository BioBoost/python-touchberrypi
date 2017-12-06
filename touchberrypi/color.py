class Color(object):

    def __init__(self, red, green, blue):
        self.red = red
        self.green = green
        self.blue = blue

    def red(self):
        return self.red

    def green(self):
        return self.green

    def blue(self):
        return self.blue

    def values(self):
        return [self.red, self.green, self.blue]

    def __str__(self):
        return "{R = " + str(self.red)   \
            + ", G = " + str(self.green)   \
            + ", B = " + str(self.blue) + "}"
