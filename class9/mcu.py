import network
import sys


class gpio:
    def __init__(self):
        self._D0 = 16
        self._D1 = 5
        self._D2 = 4
        self._D3 = 0
        self._D4 = 2
        self._D5 = 14
        self._D6 = 12
        self._D7 = 13
        self._D8 = 15
        self._SDD3 = 10
        self._SDD2 = 9

    @property
    def D0(self):
        return self._D0

    @property
    def D1(self):
        return self._D1

    @property
    def D2(self):
        return self._D2

    @property
    def D3(self):
        return self._D3

    @property
    def D4(self):
        return self._D4

    @property
    def D5(self):
        return self._D5

    @property
    def D6(self):
        return self._D6

    @property
    def D7(self):
        return self._D7

    @property
    def D8(self):
        return self._D8

    @property
    def SDD3(self):
        return self._SDD3

    @property
    def SDD2(self):
        return self._SDD2


class wifi:
    def __init__(self, ssid=None, password=None):
        """
        初始化 WiFi 模組
        ssid: WiFi 名稱
        password: WiFi 密碼
        """
        self.sta = network.WLAN(network.STA_IF)
        self.ap = network.WLAN(network.AP_IF)
        self.ssid = ssid
        self.password = password
        self.ap_active = False
        self.sta_active = False
        self.ip = None

    def setup(self, ap_active=False, sta_active=False):
        """
        設定 WiFi 模組
        ap_active: 是否啟用 AP 模式
        sta_active: 是否啟用 STA 模式

        使用方法:
        wi.setpup(ap_active=True|False, sta_active=True|False)
        """
        self.ap_active = ap_active
        self.sta_active = sta_active
        self.ap.active(ap_active)
        self.sta.active(sta_active)

    def scan(self):
        """
        搜尋 WiFi
        返回: WIFI 列表

        使用方法:
        wi.scan()
        """
        if self.sta_active:
            wifi_list = self.sta.scan()
            print("Scan results:")
            for i in range(len(wifi_list)):
                print(wifi_list[i][0])
        else:
            print("STA 模式未啟用")

    def connect(self, ssid=None, password=None) -> bool:
        """
        連接 WiFi
        ssid: WiFi 名稱
        password: WiFi 密碼

        使用方法:
        wi.connect("WIfI_NAME", "WIFI_PASSWORD")
        或在初始化時設定過就可以不用再設定:
        wi.connect()
        """
        ssid = ssid if ssid is not None else self.ssid
        password = password if password is not None else self.password

        if not self.sta_active:
            print("STA 模式未啟用")
            return False

        if ssid is None or password is None:
            print("WIFI 名稱或密碼未設定")
            return False

        if self.sta_active:
            self.sta.connect(ssid, password)
            while not self.sta.isconnected():
                pass
            self.ip = self.sta.ifconfig()[0]  # 取得 IP
            print("connet successfully", self.sta.ifconfig())
            return True


class LED:
    def __init__(self, r_pin, g_pin, b_pin, pwm: bool = False):
        """
        LED 類用於控制 RGB LED

        屬性:
        RED(Pin): 紅色 LED 腳位
        GREEN(Pin): 綠色 LED 腳位
        BLUE(Pin): 藍色 LED 腳位

        方法:
        __init__(r_pin, g_pin, b_pin, pwm: bool = False): 初始化 LED
        當 pwm 為 True 時，使用 PWM 控制亮度
        當 pwm 為 False 時，使用數位輸出控制開關

        """
        from machine import Pin, PWM

        if pwm:
            self.RED = PWM(Pin(r_pin), freq=1000, duty=0)
            self.GREEN = PWM(Pin(g_pin), freq=1000, duty=0)
            self.BLUE = PWM(Pin(b_pin), freq=1000, duty=0)
        else:
            self.RED = Pin(r_pin, Pin.OUT)
            self.GREEN = Pin(g_pin, Pin.OUT)
            self.BLUE = Pin(b_pin, Pin.OUT)


class MQTT:
    def __init__(self, client_id, server, user=None, password=None):
        """
        初始化 MQTT 客戶端

        屬性:
        client_id(str): 客戶端 ID
        server(str): MQTT 伺服器位址
        user(str): 使用者名稱
        password(str): 密碼
        keepalive(int): 保持連線時間

        方法:
        __init__(client_id, server, user=None, password=None): 初始化 MQTT 客戶端
        """
        from umqtt.simple import MQTTClient

        self.client_id = client_id
        self.server = server
        self.user = user
        self.password = password
        self.keepalive = 60
        self.mqclient = MQTTClient(
            client_id=self.client_id,
            server=self.server,
            user=self.user,
            password=self.password,
            keepalive=self.keepalive,
        )

    def connect(self):
        """
        連接到 MQTT 伺服器

        使用方法:
        mqtt.connect()
        """
        try:
            self.mqclient.connect()
            print("connected to MQTT Broker")
        except:
            sys.exit()

    def subscribe(self, topic, callback):
        """
        訂閱主題

        topic(str): 要訂閱的主題名稱
        callback(function): 收到訊息時要用的指令
        使用方法:
        mqtt.subscribe("topic_name", callback_function)
        """
        self.mqclient.set_callback(callback)
        self.mqclient.subscribe(topic)

    def check_msg(self):
        """
        檢查是否有收到訊息

        使用方法:
        mqtt.check_msg()
        """
        self.mqclient.check_msg()
        self.mqclient.ping()
