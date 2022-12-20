from polls import models
from script import gittoken
from django.http import JsonResponse


def valida_cookies(data,_type):
    """
    :用于验证cookies否则权限异常
    :param data: 前端发送过来的cookies/login_user/user_type
    :return: true,false
    """
    cookies_valida = False
    cookies_password =''
    try:
        cookies = data['user_data[cookies]']
        login_user = data['user_data[login_user]']
        user_type = data['user_data[user_type]']
    except:
        return

    if _type == 'admin': #判断管理员身份
        find_user = models.Adminster.objects.filter(username=login_user) #查找用户结果
        if(find_user.count()):
            cookies_password = login_user[3] + (find_user[0].password)[3]
            cookies_valida = gittoken.verifi_token(cookies_password,cookies)

    elif _type == 'user':#判断用户身份
        find_user = models.User.objects.filter(userphone=login_user)   #查找用户结果
        if(find_user.count()):
            cookies_password = login_user[3] + (find_user[0].password)[3]
            cookies_valida = gittoken.verifi_token(cookies_password,cookies)

    return cookies_valida