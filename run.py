import requests
import sys
import time
import telepot
token=str(sys.argv[2])
chat_id=str(sys.argv[3])
bot=telepot.Bot(token)

def send(message):
    bot.sendMessage(chat_id,message, parse_mode=None, disable_web_page_preview=None, disable_notification=None, reply_to_message_id=None, reply_markup=None)

if (len(sys.argv) >= 2):
    urls = sys.argv[1].split(',')
else:
    urls = ['https://bili33.top/']
for i in range(0, len(urls)):
    req = requests.get(urls[i])
    print(f'第{i}号网址唤醒状态:', req, time.strftime(
        '%Y-%m-%d %H:%M:%S', time.localtime(time.time())))
    message='[WakeLeancloud]唤醒状态：{}'.format(req.status_code)
    send(message)
