#########################匯入模組#########################
from umqtt.simple import MQTTClient
import sys
import time
import mcu
#########################函式與類別定義#########################
def on_message(topic, msg):
    msg = msg.decode("utf8")
    topic = topic.decode("utf8")
    print(f"my subscribe topic:{topic}, msg:{msg}")
#########################宣告與設定#########################
wi = mcu.wifi()
wi.setup(ap_active=False, sta_active=True)
if wi.connect("Singular_AI", "Singular#1234"):
    print(f"IP={wi.ip}")

mq_server = "mqtt.singularinnovation-ai.com"
mqttClientID = "ID"
mqttUsername = "singular"
mqttPassword = "Singular#1234"
mqclient = MQTTClient(client_id=mqttClientID,server=mq_server,user=mqttUsername,password=mqttPassword, keepalive=30)

try:
    mqclient.connect()
except:
    sys.exit()
finally:
    print("connected to MQTT Broker")

mqclient.set_callback(on_message)
mqclient.subscribe("eric")
#########################主程式#########################
while True:
    mqclient.check_msg()
    mqclient.ping()
    time.sleep(1)
