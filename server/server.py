from server_socket import ServerSocket


class Server(object):
    '''服务器核心类'''

    def __init__(self):
        # 创建服务器套接字对象
        self.server_socket = ServerSocket()

    def startup(self):
        '''获取服务器客户端并开启服务'''
        # 获取客户端连接
        soc, addr = self.server_socket.accept()

        # 收发消息
        recv_data = soc.recv(512)  # 由于直接通过socket收到的消息是二进制数据,需要解码,并接受512字节的数据
        print(recv_data.decode('utf-8'))
        recv_data.send("成功连接到服务器".encode('utf-8'))

        # 关闭客户端套接字
        soc.close()
