from polls import models
from django.http import JsonResponse
from script import gittoken
# Create your views here.


# 注册接口
def register(request):
    respons = {}
    if request.method == 'POST':
        usname = request.POST['username']
        uspass = request.POST['password']
        phone = request.POST['phone']
        # 查找数据库相应的用户数据
        find_user = models.User.objects.filter(username=usname)
        find_phone = models.User.objects.filter(userphone=phone)

        if find_user:
            respons = {'result': 'error', 'msg': '账号已存在'}
        elif find_phone:
            respons = {'result': 'error', 'msg': '手机号已存在'}
        elif len(phone) != 11:
            respons = {'result': 'error', 'msg': '手机号格式错误'}
        elif len(uspass) <= 8:
            respons = {'result': 'error', 'msg': '密码小于8位数'}
        else:
            models.User.objects.create(
                username=usname, password=uspass, userphone=phone)
            respons = {'result': 'ok', 'msg': '注册成功'}

    else:
        respons = {'result': 'error', 'msg': '接口异常'}
    return JsonResponse(respons, json_dumps_params={'ensure_ascii': False})


# 登录接口

def login(request):
    respons = {}
    cookies = ''
    if request.method == 'POST':
        user_phone = request.POST['phone']
        user_password = request.POST['password']
        find_phone = models.User.objects.filter(userphone=user_phone)
        if find_phone:
            if find_phone[0].password == user_password:
                cookies = gittoken.generate_token(
                    (user_phone[3]+user_password[3]), 3600)
                respons = {'result': 'ok', 'msg': '登录成功', 'cookies': cookies}
            else:
                respons = {'result': 'error', 'msg': '密码错误'}
        else:
            respons = {'result': 'error', 'msg': '此用户不存在'}
    else:
        respons = {'result': 'error', 'msg': '接口异常'}
    return JsonResponse(respons, json_dumps_params={'ensure_ascii': False})


def login_admin(request):
    respons = {}
    cookies = ''
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        find_user = models.Adminster.objects.filter(username=username)
        if find_user and (find_user[0].password == password):
            cookies = gittoken.generate_token(
                (username[3]+password[3]), 3600)
            respons = {'result': 'ok', 'msg': '登录成功', 'cookies': cookies}
        else:
            respons = {'result': 'error', 'msg': '用户名或密码错误', 'cookies': cookies}
    else:
        respons = {'result': 'error', 'msg': '用户名或密码错误', 'cookies': cookies}
    return JsonResponse(respons, json_dumps_params={'ensure_ascii': False})

# def new_hot_shop(request):
#     respons = {}
#     if request.method == 'GET':
