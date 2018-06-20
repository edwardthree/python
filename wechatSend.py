# 不要抄下源码就运行，你需要改动几个地方

from __future__ import unicode_literals
from threading import Timer
from wxpy import *
import requests

bot = Bot()


# linux执行登陆请调用下面的这句
# bot = Bot(console_qr=2,cache_path="botoo.pkl")


def get_news():
    """获取金山词霸每日一句，英文和翻译"""

    url = "http://open.iciba.com/dsapi/"
    r = requests.get(url)
    content = r.json()['content']
    note = r.json()['note']
    return content, note


def send_news():
    try:
        contents = get_news()

        # 你朋友的微信名称，不是备注，也不是微信帐号。

        my_friend = bot.friends().search(u'Ms.')[0]
        my_friend.send(contents[0])
        my_friend.send(contents[1])
        my_friend.send(u"媳妇该睡觉啦，爱你么么哒（づ￣3￣）づ╭❤～(¦3[▓▓] 晚安")
        # 每86400秒（1天），发送1次
        t = Timer(86400, send_news)
        t.start()
    except Exception as  e:

        # 你的微信名称，不是微信帐号。
        print(e);
        my_friend = bot.friends().search('m')[0]
        my_friend.send(u"今天消息发送失败了")
        send_news()


if __name__ == "__main__":
    send_news()