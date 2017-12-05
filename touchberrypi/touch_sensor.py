class TouchSensor(object):
    I2C_ADDRESS = 0x1b
    CHIP_ID_CHECK = 0x2E
    REG_CHIP_ID = 0x00
    REG_KEY_STATE = 0x03

    def __init__(self, i2c_bus):
        self.i2c_bus = i2c_bus
        self.self_check()

    def chip_id(self):
        return self.read_register(TouchSensor.REG_CHIP_ID)

    def key_state(self):
        return self.read_register(TouchSensor.REG_KEY_STATE)

    def read_register(self, register):
        self.i2c_bus.write_byte(TouchSensor.I2C_ADDRESS, register)
        return self.i2c_bus.read_byte(TouchSensor.I2C_ADDRESS)

    def self_check(self):
        if self.chip_id() != TouchSensor.CHIP_ID_CHECK:
            print("Failed to talk to QT1070 Touch Sensor")
        else:
            print("QT1070 Touch Sensor online ...")
