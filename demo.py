import touchberrypi 

def on_key_up(key):
    print("Key {} pressed".format(key))


touchberrypi.attach(on_key_up)

print(touchberrypi.get_temperature())

touchberrypi.set_all_leds("blue")

touchberrypi.set_led(5, "red")


