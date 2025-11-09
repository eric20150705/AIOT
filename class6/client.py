# pc直行
################################輸入模組########################################
import socket

################################宣告與設定#############################################
client_socket = socket.socket()
client_socket.connect(("127.0.0.1", 54088))

####################################主程式##############################################
while True:
    msg = input("Input Message:")
    client_socket.send(msg.encode("utf8"))
    reply = client_socket.recv(128).decode("utf8")
    if reply == "quit":
        print("Disconnected")
        client_socket.close()
        break
    print(reply)
