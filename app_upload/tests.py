# from django.test import TestCase
from PIL import Image, ImageDraw, ImageFont
import django
import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "diary.settings")

django.setup()
# image = Image.open('E:/term\diary\media\images/4.png')
# # # im.size
# # im_resize = im.resize((256, 256)) #default 情况下是NEAREST插值方法
# # im_resize0 = im.resize((256,256), Image.BILINEAR)
# # # im_resize0.size
# # im_resize1 = im.resize((256,256), Image.BICUBIC)
# # im_resize2 = im.resize((256,256), Image.ANTIALIAS)
# # im_resize2.save('E:/term\diary\media\images/22.png')
# width, height = image.size
# rate = 1.0 # 压缩率
#
# # 根据图像大小设置压缩率
# if width >= 2000 or height >= 2000:
#     rate = 0.5
# elif width >= 1000 or height >= 1000:
#     rate = 0.7
# elif width >= 500 or height >= 500:
#     rate = 0.9
#
# width = int(width * rate)   # 新的宽
# height = int(height * rate) # 新的高
#
# image.thumbnail((width, height), Image.ANTIALIAS) # 生成缩略图
#
# k = 20
# text = 'http://Blog.cyanzoy.top'
# Font = ImageFont.truetype("C:\Windows\Fonts\simsunb.ttf", k)  # 创建Font对象，k之为字号
# textW, textH = Font.getsize(text)            # 获取文字尺寸
# d = ImageDraw.Draw(image)
# d.ink = 238 + 240 * 256 + 248 * 256 * 256          # 黑色
# d.text([int(width/10), 0], text, font=Font)
#
# image.save('E:/term\diary\media\images/watermark.png')


def test_twilo():
    from twilio.rest import Client

    # Your Account Sid and Auth Token from twilio.com/console
    account_sid = 'AC1463d5e2fd370153a1ea3243ecb00db8'
    auth_token = 'ade6147290ec1a7e59d02d7d8cfea9de'
    client = Client(account_sid, auth_token)

    message = client.messages.create(
        body="您好.我是你大哥",
        from_='+14235454908',
        to='+8615657857080'
    )

    print(message.sid)


def test_haspas():
    from django.contrib.auth.hashers import make_password,check_password

    pwd = make_password("1996Chan", None, "default")
    print(pwd)
    print(check_password("1996Chan",  "pbkdf2_sha256$120000$dnQiKyWwYHWt$6M7+wYF8afQtz4SH2l3E4l8xDPr2CccY0aTWe5pfVyc="))

def test_three():
    str = "adsad.hh.1.ppo"
    print(str.rsplit(".", 2))


if __name__ == "__main__":
    # test_twilo()
    test_haspas()
    # test_three()
