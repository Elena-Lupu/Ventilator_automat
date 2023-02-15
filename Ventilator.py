import machine
import utime
import math
from pico_i2c_lcd import I2cLcd

thermistor = machine.ADC(28)
pwmPIN=16
cwPin=14
acwPin=15
i2c = machine.I2C(0, sda=machine.Pin(0), scl=machine.Pin(1), freq=100000)
lcd = I2cLcd(i2c, 39, 2, 16)
temp_p = 0
prag = 20
nr = 20
buton1 = machine.Pin(13,machine.Pin.IN,machine.Pin.PULL_UP)
buton2 = machine.Pin(12,machine.Pin.IN,machine.Pin.PULL_UP)
hot = machine.Pin(6,machine.Pin.OUT)
led_verde = machine.Pin(8,machine.Pin.OUT)
led_albastru = machine.Pin(17,machine.Pin.OUT)
led_rosu = machine.Pin(7,machine.Pin.OUT)

def motorMove(speed,direction,speedGP,cwGP,acwGP):
    if speed > 100: speed=100
    if speed < 0: speed=0
    Speed = machine.PWM(machine.Pin(speedGP))
    Speed.freq(50)
    cw = machine.Pin(cwGP, machine.Pin.OUT)
    acw = machine.Pin(acwGP, machine.Pin.OUT)
    Speed.duty_u16(int(speed/100*65536))
    if direction == 0:
        cw.value(0)
        acw.value(0)
    if direction > 0:
        cw.value(1)
        acw.value(0)

while True:
    temp = 1/(((math.log((10000*(3.3*float(thermistor.read_u16())/65535)/(3.3-(3.3*float(thermistor.read_u16())/65535)))/10000))/3950)+(1/(273.15+25)))-273.15
    if (temp > prag+10): viteza = 100
    if (temp > prag+5 and temp < prag+10): viteza = 50
    if (temp > prag+2 and temp < prag+5): viteza = 15
    if abs(temp-temp_p) >= 1:
        temp_p = temp
        lcd.clear()
        lcd.putstr('Temp:   %d  C\nPrag:   %d  C' % (temp,prag))
    if (temp > prag+2):
        motorMove(viteza,1,pwmPIN,cwPin,acwPin)
        led_verde.value(0)
        led_albastru.value(1)
        led_rosu.value(0)
        hot.value(0)
    elif (temp < prag-2):
        motorMove(100,1,pwmPIN,cwPin,acwPin)
        hot.value(1)
        led_verde.value(0)
        led_rosu.value(1)
        led_albastru.value(0)
    else:
        motorMove(viteza,0,pwmPIN,cwPin,acwPin)
        hot.value(0)
        led_rosu.value(0)
        led_albastru.value(0)
        led_verde.value(1)
    if buton1.value()==True:
        nr = nr+1
        if (nr > prag+2):
            prag = prag+1
            lcd.clear()
            lcd.putstr('Temp:   %d  C\nPrag:   %d  C' % (temp,prag))
        utime.sleep(0.1)
    if buton2.value()==True:
        nr = nr-1
        if (nr < prag-2):
            prag = prag-1
            lcd.clear()
            lcd.putstr('Temp:   %d  C\nPrag:   %d  C' % (temp,prag))
        utime.sleep(0.1)
    utime.sleep(0.5)