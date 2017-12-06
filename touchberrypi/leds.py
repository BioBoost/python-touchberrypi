from .color import Color
from time import sleep

class Leds(object):
    I2C_ADDRESS = 0x60
    DEF_ALL_CALL_ADDR = 0xD0

    REG_MODE_1 = 0x00
    REG_LED_0 = 0x02
    REG_LEDOUT0 = 0x14
    REG_ALLCALL = 0x1B

    NUMBER_OF_RGB_LEDS = 5

    def __init__(self, i2c_bus):
        self.i2c_bus = i2c_bus
        self.self_check()
        self.configure_for_pwn()
        self.enable()
        self.all_off()

    def all_off(self):
        self.set_all(Color(0, 0, 0))

    def set_all(self, color):
        register = Leds.REG_LED_0
        register = self.get_auto_increment_reg_address(register)
        values = color.values() * Leds.NUMBER_OF_RGB_LEDS
        self.i2c_bus.write_i2c_block_data(Leds.I2C_ADDRESS, register, values)

    def set_led(self, index, color):
        register = Leds.REG_LED_0 + (index * 3)
        register = self.get_auto_increment_reg_address(register)
        self.i2c_bus.write_i2c_block_data(Leds.I2C_ADDRESS, register, color.values())

    def configure_for_pwn(self):
        register = self.get_auto_increment_reg_address(Leds.REG_LEDOUT0)
        values = [0xAA] * 4
        self.i2c_bus.write_i2c_block_data(Leds.I2C_ADDRESS, register, values)

    def enable(self):
        mode = self.i2c_bus.read_byte_data(Leds.I2C_ADDRESS, Leds.REG_MODE_1)
        mode &= (~0x01 << 4);
        self.i2c_bus.write_byte_data(Leds.I2C_ADDRESS, Leds.REG_MODE_1, mode)

    def all_call_address(self):
        return self.i2c_bus.read_byte_data(Leds.I2C_ADDRESS, Leds.REG_ALLCALL)

    def get_auto_increment_reg_address(self, register):
        return register | (0x01 << 7)

    # I know not the best idea but i need a way to self check
    def self_check(self):
        if self.all_call_address() != Leds.DEF_ALL_CALL_ADDR:
            print("Failed to talk to TLC59116 Led Driver")
        else:
            print("TLC59116 Led Driver online ...")
