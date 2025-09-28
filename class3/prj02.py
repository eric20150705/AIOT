#########################匯入模組#########################
from machine import Pin, ADC
from time import sleep
import mcu
#########################函式與類別定義#########################

#########################宣告與設定#########################
gpio = mcu.gpio()
light_sensor = ADC(0)
red = Pin(gpio.D5, Pin.OUT)

red.value(0)
#########################主程式#########################
while True:
    light_sensor_reading = light_sensor.read()
    if light_sensor_reading > 700:
         red.value(1)
    else:
         red.value(0)
        