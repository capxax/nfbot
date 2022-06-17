import os
import time
import requests

token = "botid"
chat_id = chatid

while True:
    time.sleep(300)
    cmd = os.popen('./nf | grep \"支持非自制剧\"').read()  //nf解锁检测
    if cmd.find('支持非自制剧') >= 0:
        print(cmd)
        r = requests.post(f'https://api.telegram.org/bot{token}/sendMessage', json={"chat_id": chat_id, "text": "已解锁"})// post给bot
        print(r.json())

    else:
        print('解锁失败')
        os.popen(f'bash /root/warp.sh wgd') //warp脚本
