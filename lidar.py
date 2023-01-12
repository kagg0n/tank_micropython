#-----LIB DEF-----
from time import sleep
from machine import Pin, PWM,I2C
import VL53L0X
import sh1106

#-----VAR DEF-----
rotation_angle = 0
n1 = 14
n2 = 114
#-----LIB INIT----
pwm = PWM(Pin(6))
pwm.freq(50)

i2c1 = I2C(0,scl=Pin(5), sda=Pin(4), freq=400000)
display = sh1106.SH1106_I2C(128, 64, i2c1, Pin(16), 0x3c)
display.sleep(False)

i2c = I2C(1,scl=Pin(3), sda=Pin(2), freq=400000)
tof = VL53L0X.VL53L0X(i2c)
tof.set_Vcsel_pulse_period(tof.vcsel_period_type[0], 18)
tof.set_Vcsel_pulse_period(tof.vcsel_period_type[1], 14)
#-----MAIN CODE-----
def distance_drawing():
    endLine_point = dist_value // 20 # конечная точка по которой будет строиться линия
    display.line(n1,0,n1,endLine_point,1) # нач x;нач y; конеч x; конеч y; цвет
    display.show()
def distance_drawingReverse():
    endLine_point = dist_value // 20 # конечная точка по которой будет строиться линия
    display.line(n2,0,n2,endLine_point,1) # нач x;нач y; конеч x; конеч y; цвет
    display.show()
def servo_rotation_with_laser(): #постоянное вращение сервопривода
    #Tech.info:1000-6000 диапазон,необходимый для лидара;50 пунктов-1 градус вращения
    for rotation_angle in range(1000,6000,50):
        pwm.duty_u16(rotation_angle)
        tof.start()
        tof.read()
        global dist_value
        dist_value = (tof.read())
        tof.stop()
        distance_drawing()
        global n1
        n1 = n1+1
    display.fill(0)
    for rotation_angle in range(6000,1000,-50):
        pwm.duty_u16(rotation_angle)
        tof.start()
        tof.read()
        dist_value = (tof.read())
        tof.stop()
        distance_drawingReverse()
        global n2
        n2 = n2 -1
    display.fill(0)
    n1 = 14
    n2 = 114
while True:
    servo_rotation_with_laser()
    #pwm.duty_u16(2500)
