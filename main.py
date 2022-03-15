import machine #calling libraries
import ads1x15
import uasyncio

uart = UART(0,9600)
gain = 1
i2c = machine.I2C(0, scl=machine.Pin(17), sda=machine.Pin(16)) #I2C initialization
ads = ads1x15.ADS1115(i2c, 0x48, gain) #ADS-1115 object initialization

# Co-routine: read channel-1 and print 16-bit values with time dela
async def read_ch1(delay):
    while True:
        ch1 = ads.read(1,0)
        msg1 = 'Channel 1 : ' + str(ch1) + ' '
        uart.write(msg1)
        await uasyncio.sleep(delay)
        
# Co-routine: read channel-2 and print 16-bit values with time delay      
async def read_ch2(delay):
    while True:
        ch1 = ads.read(1,1)
        msg2 = 'Channel 2 : ' + str(ch2) + ' '
        uart.write(msg2)
        await uasyncio.sleep(delay)
        
# Co-routine: read channel-3 and print 16-bit values with time delay
async def read_ch3(delay):
    while True:
        ch1 = ads.read(1,2)
        msg3 = 'Channel 3 : ' + str(ch3) + ' '
        uart.write(msg3)
        await uasyncio.sleep(delay)
        
# Co-routine: read channel-4 and print 16-bit values with time delay
async def read_ch4(delay):
    while True:
        ch1 = ads.read(1,3)
        msg4 = 'Channel 4 : ' + str(ch1) + ' '
        uart.write(msg4)
        await uasyncio.sleep(delay)
        
#entry point for asyncio co-routines
async def main():
    uasyncio.create_task(read_ch1(0.5)) #creating tasks for calling coroutines
    uasyncio.create_task(read_ch2(0.5))
    uasyncio.create_task(read_ch3(0.5))
    uasyncio.create_task(read_ch4(0.5))
    await uasyncio.sleep_ms(1000)

while True:  
    uasyncio.run(main()) #calling main function in while loop