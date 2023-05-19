import socket
from config import *


class ServerSocket(socket.socket):
    """自定义套接字,初始化服务器套接字需要的相关参数"""

    def __init__(self):
        # 设置tcp类型,使用父类的构造器,并将创建后的对象赋值给self变量
        super(ServerSocket, self).__init__(socket.AF_INET, socket.SOCK_STREAM)

        # 绑定地址和端口号
        self.bind((SERVER_IP, SERVER_PORT))

        # 设置为监听模式
        self.listen(128)

        # soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # socket.AF_INET 说明是ipv4的地址,socket.SOCK_STREAM说明是tcp类型
        # soc.bind((ip, address))  # 绑定IP地址和端口号
        # soc.listen(128)  # 设置监听模式,监听tcp通信,其中括号内的数目指的是允许连接的最大数目
        # soc, addr = soc.accept()  # 获取客户端,客户端套接字,客户端地址
        # soc.send()  # 发送消息
        # soc.recv()  # 接受消息
