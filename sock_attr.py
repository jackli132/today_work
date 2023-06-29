from socket import *

# 　创建一个ｔｃｐ套接字
s = socket()

# 　设置套接字端口立即重用
s.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)

s.bind(("0.0.0.0", 8888))
s.listen(3)
c, addr = s.accept()
print("Connect:", addr)
c.recv(1024)

print("地址类型：", s.family)
print("套接字类型:", s.type)
print("绑定地址：", s.getsockname())
print("描述符:", s.fileno())
print("客户端地址:", c.getpeername())  # 连接套接字调用
