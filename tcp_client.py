"""
tcp 客户端程序
重点代码
"""

from socket import *

#  创建tcp套接字
sockfd = socket()

#  发起连接
server_addr = ('192.168.43.192', 8888)
sockfd.connect(server_addr)

#  收发消息
while True:
    data = input("消息:")
    if not data:
        break
    sockfd.send(data.encode())
    data = sockfd.recv(1024)
    print("From server:", data.decode())

#  关闭
sockfd.close()
