class TouchSensor(object):
    I2C_ADDRESS = 0x1B
    CHIP_ID_CHECK = 0x2E
    REG_CHIP_ID = 0
    REG_KEY_STATE = 3
    REG_CALIBRATE = 56
    REG_RESET = 57

    def __init__(self, i2c_bus):
        self.i2c_bus = i2c_bus
        self.self_check()

    def chip_id(self):
        return self.read_register(TouchSensor.REG_CHIP_ID)

    def key_state(self):
        return self.read_register(TouchSensor.REG_KEY_STATE)

    def calibrate(self):
        self.write_register(TouchSensor.REG_CALIBRATE, 0xFF)

    def reset(self):
        self.write_register(TouchSensor.REG_RESET, 0xFF)

    def write_register(self, register, value):
        self.i2c_bus.write_byte_data(TouchSensor.I2C_ADDRESS, register, value)

    def read_register(self, register):
        return self.i2c_bus.read_byte_data(TouchSensor.I2C_ADDRESS, register)

    def self_check(self):
        if self.chip_id() != TouchSensor.CHIP_ID_CHECK:
            print("Failed to talk to QT1070 Touch Sensor")
        else:
            print("QT1070 Touch Sensor online ...")
