class TemperatureSensor(object):
    I2C_ADDRESS = 0x48
    DEF_HYSTERESIS = 75

    REG_TEMPERATURE = 0
    REG_CONFIG = 1
    REG_HYSTERESIS = 2
    REG_LIMIT = 3

    def __init__(self, i2c_bus):
        self.i2c_bus = i2c_bus
        self.self_check()

    def temperature(self):
        values = self.i2c_bus.read_i2c_block_data(TemperatureSensor.I2C_ADDRESS, TemperatureSensor.REG_TEMPERATURE)
        temperature = (values[0]*1.0) + values[1]/256.0
        return temperature

    def hysteresis(self):
        values = self.i2c_bus.read_i2c_block_data(TemperatureSensor.I2C_ADDRESS, TemperatureSensor.REG_HYSTERESIS)
        hysteresis = (values[0]*1.0) + values[1]/256.0
        return hysteresis

    # I know not the best idea but i need a way to self check
    def self_check(self):
        if int(self.hysteresis()) != TemperatureSensor.DEF_HYSTERESIS:
            print("Failed to talk to MCP9800 Temperature Sensor")
        else:
            print("MCP9800 Temperature Sensor online ...")
