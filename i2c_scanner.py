import machine

i2c = machine.I2C(0, scl=machine.Pin(17), sda = machine.Pin(16))
devices = i2c.scan()

if devices:
    for d in devices:
        print(hex(d))
else:
    print('device not found')