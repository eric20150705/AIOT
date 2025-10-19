################################輸入模組########################################
import network
################################宣告與設定#######################################
wlan = network.WLAN(network.STA_IF)  # 初始化 STA 模式
ap = network.WLAN(network.AP_IF)    # 初始化 AP 模式
ap.active(False)  # 關閉 AP 模式
wlan.active(True)  # 啟動 STA 模式

# 搜尋 wifi
wifi_list = wlan.scan()
print("Scan result:")
for i in range(len(wifi_list)):
    print(wifi_list[i])

# 選擇要連接的 wifi
wlSSID = "Singular_AI"
wlPWD = "Singular#1234"
wlan.connect(wlSSID, wlPWD)
while not wlan.isconnected():
    pass
print("connet sucsessfully", wlan.ifconfig())
while True:
    pass