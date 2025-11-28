#########################匯入模組#########################
import time
import mcu
from machine import ADC


#########################函式與類別定義#########################
def on_message(topic, msg):
    global m
    msg = msg.decode("utf8")
    topic = topic.decode("utf8")
    print(f"my subscribe topic:{topic}, msg:{msg}")
    m = msg


def LED_ON():
    LED.RED.value(1)
    LED.GREEN.value(1)
    LED.BLUE.value(1)


def LED_OFF():
    LED.RED.value(0)
    LED.GREEN.value(0)
    LED.BLUE.value(0)


#########################宣告與設定#########################
wi = mcu.wifi()
wi.setup(ap_active=False, sta_active=True)
if wi.connect("Singular_AI", "Singular#1234"):
    print(f"IP={wi.ip}")


mqclient = mcu.MQTT(
    client_id="ID",
    server="mqtt.singularinnovation-ai.com",
    user="singular",
    password="Singular#1234",
)
mqclient.connect()
mqclient.subscribe("eric", on_message)
gpio = mcu.gpio()
LED = mcu.LED(r_pin=gpio.D5, g_pin=gpio.D6, b_pin=gpio.D7, pwm=False)
LED.RED.value(0)
LED.GREEN.value(0)
LED.BLUE.value(0)
Light_Sensor = ADC(0)
m = ""
#########################主程式#########################
while True:
    mqclient.check_msg()
    if m == "on":
        LED_ON()
    elif m == "off":
        LED_OFF()
    elif m == "auto":
        if Light_Sensor.read() > 700:
            LED_ON()
        else:
            LED_OFF()
    time.sleep(0.1)
