import touchberrypi 

def on_key_up_handler(key):
    print("Key {} pressed".format(key))


touchberrypi.on_key_up(on_key_up_handler)

print(touchberrypi.get_temperature())

touchberrypi.set_all_leds("blue")

touchberrypi.set_led(5, "red")


