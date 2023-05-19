# ---------数据协议相关配置---------
# 由于数据在通信过程中需要特定的格式区分什么是通信的内容,什么是通信的开始,什么是通信的结束..
REQUEST_LOGIN = '0001'  # 登录请求
REQUEST_CHAT = '0002'  # 聊天请求
RESPONSE_LOGIN_RESULT = '1001'  # 登录结果响应
RESPONSE_CHAT = '1002'  # 聊天响应
DELIMITER = '|'  # 作为通信格式中的分隔符

# 服务器相关配置
SERVER_IP = '127.0.0.1'
SERVER_PORT = '8090'
