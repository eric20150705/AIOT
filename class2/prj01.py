#########################匯入模組#########################
from machine import Pin
from time import sleep
import mcu
#########################函式與類別定義#########################

#########################宣告與設定#########################
gpio = mcu.gpio()
red = Pin(gpio.D5, Pin.OUT)
green = Pin(gpio.D6, Pin.OUT)
blue = Pin(gpio.D7, Pin.OUT)

red.value(0) # (1)
blue.value(0) # (1)
green.value(0) # (1)
#########################主程式#########################
while True:
    green.value(1) 
    sleep(1)
    red.value(1)
    sleep(1) 
    green.value(0)
    sleep(1)
    red.value(0) 