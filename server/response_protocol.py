# 使用类中的静态方法,在不需要定义对象的前提下,直接通过类中方法调用,即使不产生对象
'''
join()方法可以用来连接任意的sequance序列
使用join()的连接测试,将字符串逆序后使用join拼接
s=''.join(reversed("abc"))
print(s)
'''
from config import *


class ResponseProtocol(object):
    """服务器响应的格式化字符串拼接"""
    '''
    需要注意的是在python中不同于Java,在一个方法|函数的前面写注释时,在Java中是写在函数前
    但是在python中是需要写在函数的内部,并且使用一个tab风格,idea会自动补全参数
    '''

    @staticmethod
    def response_login_result(result, nickname, username):
        """
        返回用户登录的结果字符串
        :param result:值为0表示登录失败,值为1表示登录成功
        :param nickname:登录的昵称,如果登录失败则为空
        :param username:登录用户的账号,如果登录时报则为空
        :return:返回给用户的登录结果协议字符串
        通过对登录协议的解析,判断出是否将
        """
        return DELIMITER.join([RESPONSE_LOGIN_RESULT, result, nickname, username])

    @staticmethod
    def response_chat(nickname, message):
        '''
        生成返回给用户的消息字符串
        :param nickname:发送消息的用户名称
        :param message:消息正文
        :return:返回给用户的消息字符串

        '''
        return DELIMITER.join([RESPONSE_CHAT, nickname, message])
