class TemperatureSensor(object):
    I2C_ADDRESS = 0x48

    REG_TEMPERATURE = 0
    REG_CONFIG = 1
    REG_HYSTERESIS = 2
    REG_LIMIT = 3

    def __init__(self, i2c_bus):
        self.i2c_bus = i2c_bus

    def temperature(self):
        values = self.i2c_bus.read_i2c_block_data(TemperatureSensor.I2C_ADDRESS, TemperatureSensor.REG_TEMPERATURE)
        temperature = (values[0]*1.0) + values[1]/256.0
        return temperature
