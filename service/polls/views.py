from django.shortcuts import HttpResponse
from polls import models
from django.http import JsonResponse
import os
import json
from ast import literal_eval
from script import tools ,gittoken
from django.views.decorators.http import require_POST ,require_GET
# Create your views here.


# 注册接口
@require_POST
def register(request):
    respons = {}
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
    return JsonResponse(respons, json_dumps_params={'ensure_ascii': False})


# 登录接口
@require_POST
def login(request):
    respons = {}
    cookies = ''
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
    return JsonResponse(respons, json_dumps_params={'ensure_ascii': False})

    
# 查询商品接口
@require_POST
def find_shoping(request):
    respons = {}
    data_list = [] #整理好的数据
    shop_list = [] #查询到的数据
    valida_status = tools.valida_cookies(request.POST)
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
    return JsonResponse(respons, json_dumps_params={'ensure_ascii': False})