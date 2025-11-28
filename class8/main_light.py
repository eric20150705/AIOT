#########################匯入模組#########################
from umqtt.simple import MQTTClient
import sys
import time
import mcu
from machine import Pin, ADC


#########################函式與類別定義#########################
def on_message(topic, msg):
    global m
    msg = msg.decode("utf8")
    topic = topic.decode("utf8")
    print(f"my subscribe topic:{topic}, msg:{msg}")
    m = msg


def LED_ON():
    RED.value(1)
    GREEN.value(1)
    BLUE.value(1)


def LED_OFF():
    RED.value(0)
    GREEN.value(0)
    BLUE.value(0)


#########################宣告與設定#########################
wi = mcu.wifi()
wi.setup(ap_active=False, sta_active=True)
if wi.connect("Singular_AI", "Singular#1234"):
    print(f"IP={wi.ip}")

mq_server = "mqtt.singularinnovation-ai.com"
mqttClientID = "ID"
mqttUsername = "singular"
mqttPassword = "Singular#1234"
mqclient = MQTTClient(
    client_id=mqttClientID,
    server=mq_server,
    user=mqttUsername,
    password=mqttPassword,
    keepalive=30,
)

try:
    mqclient.connect()
except:
    sys.exit()
finally:
    print("connected to MQTT Broker")

mqclient.set_callback(on_message)
mqclient.subscribe("eric")

gpio = mcu.gpio()
RED = Pin(gpio.D5, Pin.OUT)
GREEN = Pin(gpio.D6, Pin.OUT)
BLUE = Pin(gpio.D7, Pin.OUT)

RED.value(0)
GREEN.value(0)
BLUE.value(0)
Light_Sensor = ADC(0)
m = ""
#########################主程式#########################
while True:
    mqclient.check_msg()
    mqclient.ping()
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
