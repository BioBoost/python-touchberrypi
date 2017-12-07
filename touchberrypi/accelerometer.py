class Accelerometer(object):
    I2C_ADDRESS = 0x1C
    WHO_AM_I = 0x1A

    REG_WHO_AM_I = 0x0D

    def __init__(self, i2c_bus):
        self.i2c_bus = i2c_bus
        self.self_check()

    def who_am_i(self):
        return self.read_register(Accelerometer.REG_WHO_AM_I)

    def read_register(self, register):
        return self.i2c_bus.read_byte_data(Accelerometer.I2C_ADDRESS, register)

    # I know not the best idea but i need a way to self check
    def self_check(self):
        if self.who_am_i() != Accelerometer.WHO_AM_I:
            print("Failed to talk to MMA8451Q Accelerometer")
        else:
            print("MMA8451Q Accelerometer online ...")
