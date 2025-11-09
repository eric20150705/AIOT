################################輸入模組########################################
import socket

################################宣告與設定#############################################
HOST = "localhost"  # IP
PORT = 54088  # port.可自行更改但要與客戶端相同
server_socket = socket.socket()  # 建立socket
server_socket.bind((HOST, PORT))  # 綁定IP與port
server_socket.listen(5)  # 最大連接數數量,超過則拒絕連接
print(f"server: {HOST}, port: {PORT} start")  # 顯示伺服器IP和PORT
client, addr = server_socket.accept()  # 接受客戶端連接,反回客戶端socket與地址
print(f"client address:{addr[0]} port:{addr[1]} connected")  # 顯示客戶端IP和PORT
####################################主程式##############################################
while True:
    msg = client.recv(128).decode("utf8")
    # 接收客戶端訊息,100為接收訊息長度上限,utf8為解碼方式
    print(f"Receive Message:{msg}")  # 顯示接收到的訊息
    reply = ""  # 建立伺服器回覆字串

    if msg == "Hello":
        reply = "Hi"
        client.send(reply.encode("utf8"))
    elif msg == "bye":
        client.send(b"quit")
        break
    else:
        reply = "what?"
        client.send(reply.encode("utf8"))

client.close()
server_socket.close()
