from machine import Pin,UART
uart = UART(0,9600,rx=Pin(17),tx=Pin(16))
signal1 = Pin(6,Pin.OUT)
signal2 = Pin(7,Pin.OUT)
signal3 = Pin(8,Pin.OUT)
signal4 = Pin(9,Pin.OUT)
while True:
    if uart.any():
        data = uart.readline()
        print(data)
        if data== b'0':			#BACK
            signal1.value(1)
            signal2.value(0)
            signal3.value(0)
            signal4.value(1)
            
                                #STRAIGHT
        elif data== b'1':
            signal1.value(0)
            signal2.value(1)
            signal3.value(1)
            signal4.value(0)
                                #LEFT_TO_RIGHT
        elif data==b'2':
            signal1.value(1)
            signal2.value(0)
            signal3.value(1)
            signal4.value(0)
                                #RIGHT_TO_LEFT
        elif data==b'3':
            signal1.value(0)
            signal2.value(1)
            signal3.value(0)
            signal4.value(1)
                                #STOP
        elif data==b'4':
            signal1.value(0)
            signal2.value(0)
            signal3.value(0)
            signal4.value(0)
            