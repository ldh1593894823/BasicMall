from django.shortcuts import HttpResponse
from polls import models
from django.http import JsonResponse
import os
import json
from ast import literal_eval
from script import tools ,gittoken
from django.views.decorators.http import require_POST ,require_GET
# Create your views here.

return_nor_permi = {'result': 'not_permission', 'msg': '无权限',}
Shop_obj = models.Shopping.objects
Shopcar_obj = models.Shop_cart.objects

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
    find_type = request.POST['find_type']
    if find_type == 'all':  #查询所有商品需要验证cookies 
        if(tools.valida_cookies(request.POST,'admin')) == True:
            shop_list = models.Shopping.objects.all()
        else:
            respons = {'result': 'not_permission', 'msg': '无权限',}
            return JsonResponse(respons, json_dumps_params={'ensure_ascii': False})
    elif find_type == 'hot_shop': #查询前8个销量最高的商品
        shop_list = models.Shopping.objects.order_by('-sales')[0:8]
    elif find_type == 'new_shop': #查询前8个上新商品
        shop_list = models.Shopping.objects.order_by('-first_add')[0:8]
    elif find_type == 'one_shop': #查询一个商品
        shop_id = request.POST['shop_id']
        shop_list = models.Shopping.objects.filter(id=shop_id)
    elif find_type == 'color': #查询彩妆
        shop_list = models.Shopping.objects.filter(category='彩妆')
    elif find_type == 'b_makeup': #查询底妆
        shop_list = models.Shopping.objects.filter(category='底妆')
    elif find_type == 'perfume': #查询香水
        shop_list = models.Shopping.objects.filter(category='香水')
    else: 
        respons = {'result': 'error', 'msg': '请求异常'}
        return JsonResponse(respons, json_dumps_params={'ensure_ascii': False})
    for i in shop_list:
        imagelist = literal_eval(i.myimage)
        data_list.append({'id':i.id,'name':i.name,'first_add':i.first_add,'price':i.price,
                            'num':i.num,'category':i.category,'myimage':imagelist,'sales':i.sales})
    respons = {'result': 'ok', 'msg': '查询成功','shop_list':data_list}
    return JsonResponse(respons, json_dumps_params={'ensure_ascii': False})

class Shop_Cart():
    # 加入购物车接口
    @require_POST
    def add_shop_car(request):
        if (tools.valida_cookies(request.POST,'user')) != True:
            return JsonResponse(return_nor_permi, json_dumps_params={'ensure_ascii': False})

        shop_id = request.POST['shop_id']
        add_shop_num = int(request.POST['add_shop_num'])
        user_phone = request.POST['user_data[login_user]']
        
        find_shopcart_obj = models.Shop_cart.objects.filter(user_id=user_phone,shop_id=shop_id)
        if find_shopcart_obj.count() == 0:
            models.Shop_cart.objects.create(user_id=user_phone,shop_id=shop_id,shop_num=add_shop_num)
        elif find_shopcart_obj.count() > 0:
            find_shopcart_obj.update(shop_num=find_shopcart_obj[0].shop_num + add_shop_num )
            
        respons = {'result': 'ok', 'msg': '添加成功'}
        return JsonResponse(respons, json_dumps_params={'ensure_ascii': False})

    #查询所有购物车列表
    @require_POST
    def all_shop_car(request):
        if (tools.valida_cookies(request.POST,'user')) != True:
            return JsonResponse(return_nor_permi, json_dumps_params={'ensure_ascii': False})
        
        user_phone = request.POST['user_data[login_user]']
        data_list = []
        
        find_list =  models.Shop_cart.objects.filter(user_id=user_phone)
        for i in find_list:
            shop = Shop_obj.get(id=i.shop_id)
            data_list.append({"name":shop.name,"myimage":literal_eval(shop.myimage)[0],"price":shop.price,"num":i.shop_num,"car_id":i.id})
        respons = {'result': 'ok', 'msg': '查询成功',"shop_list":data_list}
        return JsonResponse(respons, json_dumps_params={'ensure_ascii': False})


    #删除购物车中的一件商品
    @require_POST
    def del_shop_car(request):
        if (tools.valida_cookies(request.POST,'user')) != True:
            return JsonResponse(return_nor_permi, json_dumps_params={'ensure_ascii': False})
        
        shop_id = request.POST['car_id']
        Shopcar_obj.get(id=shop_id).delete()
        respons = {'result': 'ok', 'msg': '删除成功'}
        return JsonResponse(respons, json_dumps_params={'ensure_ascii': False})


#创建订单接口
@require_POST
def create_order(request):
    if (tools.valida_cookies(request.POST,'user')) != True:
        return JsonResponse(return_nor_permi, json_dumps_params={'ensure_ascii': False})
    price = 0 ;_shop_list = []
    courier_name  = request.POST['courier_name']
    courier_phone = request.POST['courier_phone']
    courier_place = request.POST['courier_place']
    login_user = request.POST['user_data[login_user]']
    harvest_type = request.POST['harvest_type']
    first_image = ''
    
    for index,i in enumerate(models.Shop_cart.objects.filter(user_id=login_user)):
        shop_info = models.Shopping.objects.get(id=i.shop_id)
        first_image = print("") if index == 0 else  literal_eval(shop_info.myimage)[0]
        price = price + (float(i.shop_num)*float(shop_info.price))
        _shop_list.append({"id":i.shop_id,"num":i.shop_num})

    created = models.Order.objects.create(user_id=login_user,price=price,shop_list=_shop_list,order_status=1,courier_name=courier_name,
                                            courier_phone=courier_phone,courier_place=courier_place,first_image=first_image,harvest_type=harvest_type)
        
    respons = {'result': 'ok', 'msg': '创建成功',"order_id":created.id}
    return JsonResponse(respons, json_dumps_params={'ensure_ascii': False})

#查询对应订单详情
@require_POST
def order_detail(request):
    if (tools.valida_cookies(request.POST,'user')) != True:
        return JsonResponse(return_nor_permi, json_dumps_params={'ensure_ascii': False})
    order_id  = request.POST['order_id']
    _order = models.Order.objects.get(id = order_id)
    shop_list_id = literal_eval(_order.shop_list)
    shop_list = []

    for i in shop_list_id:
        shop_obj = models.Shopping.objects.get(id = i['id'])
        shop_list.append({"name":shop_obj.name,"price":shop_obj.price,"num":i['num'],"image":literal_eval(shop_obj.myimage)[0]})

    respons = {'result': 'ok', 'msg': '查询成功',"order_detail":{"shop_list":shop_list,"all_price":_order.price}}
    return JsonResponse(respons, json_dumps_params={'ensure_ascii': False})