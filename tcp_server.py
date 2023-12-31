"""
TCP套接字服务端
重点代码
"""

import socket

# 创建流式套接字
sockfd = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 　绑定地址
sockfd.bind(('192.168.43.192', 8888))

# 　设置监听
sockfd.listen(5)

# 　等待处理客户端链接
while True:
    print("Waiting for connect....")
    try:
        connfd, addr = sockfd.accept()
        print("Connect from:", addr)
    except KeyboardInterrupt:
        print("退出服务")
        break

    # 收发消息
    while True:
        data = connfd.recv(1024)
        # 　得到空则退出循环
        if not data:
            break
        print("接收到的消息:", data.decode())
        n = connfd.send(b'Receive your message')
        print("发送了 %d 个字节数据" % n)
    connfd.close()

# 关闭套接字
sockfd.close()
