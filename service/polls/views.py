from django.shortcuts import HttpResponse
from polls import models
from django.http import JsonResponse
from script import gittoken
import os
import json
from ast import literal_eval
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
                respons = {'result': 'ok', 'msg': '登录成功', 'cookies': cookies,'login_user':user_phone,'user_type':'user'}
            else:
                respons = {'result': 'error', 'msg': '密码错误'}
        else:
            respons = {'result': 'error', 'msg': '此用户不存在'}
    else:
        respons = {'result': 'error', 'msg': '接口异常'}
    return JsonResponse(respons, json_dumps_params={'ensure_ascii': False})

def valida_cookies(data):
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

    if user_type == 'admin': #判断管理员身份
        find_user = models.Adminster.objects.filter(username=login_user)[0] #查找用户结果
        if(find_user):
            cookies_password = login_user[3] + (find_user.password)[3]
            cookies_valida = gittoken.verifi_token(cookies_password,cookies)

    elif user_type == 'user':#判断用户身份
        find_user = models.User.objects.filter(username=login_user)[0]   #查找用户结果
        if(find_user):
            cookies_password = login_user[3] + (find_user.password)[3]
            cookies_valida = gittoken.verifi_token(cookies_password,cookies)

    return cookies_valida
            
    
# 查询商品接口
def find_shoping(request):
    respons = {}
    data_list = [] #整理好的数据
    shop_list = [] #查询到的数据
    if request.method == 'POST':
        valida_status = valida_cookies(request.POST)
        find_type = request.POST['find_type']
        if find_type == 'all':  #查询所有商品需要验证cookies 
            if(valida_status):
                shop_list = models.Shopping.objects.all()
            else:
                respons = {'result': 'not_permission', 'msg': '无权限',}
                return JsonResponse(respons, json_dumps_params={'ensure_ascii': False})
        elif find_type == 'hot_shop': #查询前8个销量最高的商品
            shop_list = models.Shopping.objects.order_by('-sales')[0:8]
        elif find_type == 'new_shop': #查询前8个上新商品
            shop_list = models.Shopping.objects.order_by('-first_add')[0:8]
        else: 
            respons = {'result': 'error', 'msg': '请求异常'}
            return JsonResponse(respons, json_dumps_params={'ensure_ascii': False})

        for i in shop_list:
            imagelist = literal_eval(i.myimage)
            data_list.append({'id':i.id,'name':i.name,'first_add':i.first_add,'price':i.price,
                                'num':i.num,'category':i.category,'myimage':imagelist,'sales':i.sales})
        respons = {'result': 'ok', 'msg': '查询成功','shop_list':data_list}
        
    else:
        respons = {'result': 'error', 'msg': '接口异常'}
    return JsonResponse(respons, json_dumps_params={'ensure_ascii': False})
            

# 添加商品接口
def add_shop(request):
    respons = {}
    cookies = ''
    if request.method == 'POST':
            _shop_name     = request.POST['shop_name']  #商品名称
            _shop_price    = request.POST['shop_price'] #商品价格
            _shop_category = request.POST['shop_category'] #商品分类
            _shop_num      = request.POST['shop_num'] #商品库存
            _imageList     = request.POST['imageList'] #商品图片列表
            _imageList = json.loads(_imageList[1:])

            models.Shopping.objects.create(name=_shop_name,price=_shop_price,num=_shop_num,category=_shop_category,myimage=_imageList)

            respons = {'result': 'ok', 'msg': '好的',}
    return JsonResponse(respons, json_dumps_params={'ensure_ascii': False})


#请求方法为POST时，执行文件上传
def upload(request):
    respons = {}
    if request.method == "POST":
        #获取上传的文件，如果没有文件，就默认为None
        myFile = request.FILES.get("file",None)

        if not myFile:
            respons = {'result': 'error', 'msg': '没有图片文件'}
        else:
            new_image_name = request.POST['uuid']+'.'+myFile.name.split('.')[1]
            f = open(os.path.join("./static/image",new_image_name),"wb+")
            for chunk in myFile.chunks():#分块写入文件
                f.write(chunk)
            f.close()
            respons = {'result': 'ok', 'msg': '上传成功', 'image_name': new_image_name}
    else:
        #请求方法为get时，生成文件上传页面
        respons = {'result': 'error', 'msg': '请求异常'}
    return JsonResponse(respons, json_dumps_params={'ensure_ascii': False})