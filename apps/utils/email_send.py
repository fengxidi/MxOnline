# _*_ coding: utf-8 _*_
__auther__ = 'guozheng'
__date__ = '2019-10-6 20:16'

import  random
from users.models import EmailVerifyRecord
from django.core.mail import  send_mail
from MxOnline.settings import EMAIL_HOST_USER


def random_captcha(randomlength=6):
    code = ''
    chars = 'abcdefghijkmlnopqrstuvwxyzABCDEFGHIJKMLNOPQRSTUVXYZ0123456789'

    for i in range(randomlength):
        code += chars[random.randint(0, 60)]
    return code

def send_register_email(email, send_type='register'):
    email_record = EmailVerifyRecord()
    code = random_captcha() #验证码
    email_record.code = code
    email_record.email = email
    email_record.send_type = send_type
    email_record.save()

    email_title = ""
    email_body = ""

    if send_type == 'register':
        email_title = '溪枫教育注册激活链接'
        email_body = '请点击下面链接激活你的账号：http://127.0.0.1:8000/active/{0}'.format(code)
        #可以返回一个状态码 status = send_mail(subject=email_title, message=email_body, from_email=EMAIL_HOST_USER, recipient_list=[email,], fail_silently=False)
        send_mail(subject=email_title, message=email_body, from_email=EMAIL_HOST_USER, recipient_list=[email,], fail_silently=False)
    elif send_type == 'forget':
        email_title = '溪枫教育密码重置链接'
        email_body = '请点击下面链接重置你的密码：http://127.0.0.1:8000/reset/{0}'.format(code)
        send_mail(subject=email_title, message=email_body, from_email=EMAIL_HOST_USER, recipient_list=[email, ],
                  fail_silently=False)

