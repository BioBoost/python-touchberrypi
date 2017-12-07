class I2cPeripheral(object):
    def __init__(self, i2c_bus, slave_address):
        self.i2c_bus = i2c_bus
        self.slave_address = slave_address
        self.self_check()

    def i2c_bus(self):
        return i2c_bus

    def slave_address(self):
        return slave_address

    def read_register(self, register):
        return self.i2c_bus.read_byte_data(self.slave_address, register)

    def write_register(self, register, value):
        self.i2c_bus.write_byte_data(self.slave_address, register, value)

    def self_check(self):
        """Read value from peripheral register and checks against known value"""
        raise NotImplementedError("Please Implement this method")
