#########################匯入模組#########################
from machine import Pin, ADC, PWM
from time import sleep
import mcu
#########################函式與類別定義#########################

#########################宣告與設定#########################
frequency = 1000
duty_cycle = 0

gpio = mcu.gpio()
light_sensor = ADC(0)
RED = PWM(Pin(gpio.D5), freq=frequency, duty=duty_cycle)
GREEN = PWM(Pin(gpio.D6), freq=frequency, duty=duty_cycle)
BLUE = PWM(Pin(gpio.D7), freq=frequency, duty=duty_cycle)
#########################主程式#########################
while True:
     duty_cycle = light_sensor.read() 
     print(duty_cycle)
     sleep(0.5)

     RED.duty(duty_cycle)
     GREEN.duty(duty_cycle)
     BLUE.duty(duty_cycle)