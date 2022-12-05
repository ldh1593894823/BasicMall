from polls import models
from django.http import JsonResponse
from script import gittoken

#管理员登录接口
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
            respons = {'result': 'ok', 'msg': '登录成功', 'cookies': cookies,'login_user':username,'user_type':'admin'}
        else:
            respons = {'result': 'error', 'msg': '用户名或密码错误', 'cookies': cookies}
    else:
        respons = {'result': 'error', 'msg': '用户名或密码错误', 'cookies': cookies}
    return JsonResponse(respons, json_dumps_params={'ensure_ascii': False})