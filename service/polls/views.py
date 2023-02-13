from django.shortcuts import HttpResponse
from polls import models
from django.http import JsonResponse
import os
import json
from ast import literal_eval
from script import tools ,gittoken
from django.views.decorators.http import require_POST ,require_GET
from django.forms.models import model_to_dict
from django.core import serializers
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

# 购物车管理模块
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


#用户创建订单接口
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
        if index == 0:
            first_image = literal_eval(shop_info.myimage)[0]
        price = price + (float(i.shop_num)*float(shop_info.price))
        _shop_list.append({"id":i.shop_id,"num":i.shop_num})
    
    created = models.Order.objects.create(user_id=login_user,price=price,shop_list=_shop_list,order_status=1,courier_name=courier_name,
                                            courier_phone=courier_phone,courier_place=courier_place,first_image=first_image,harvest_type=harvest_type)
        
    respons = {'result': 'ok', 'msg': '创建成功',"order_id":created.id}
    return JsonResponse(respons, json_dumps_params={'ensure_ascii': False})

#订单创建后还没有支付，查询订单金额
@require_POST
def order_list(request):
    if (tools.valida_cookies(request.POST,'user')) != True:
        return JsonResponse(return_nor_permi, json_dumps_params={'ensure_ascii': False})
    order_id  = request.POST['order_id']
    _order = models.Order.objects.get(id = order_id)
    shop_list_id = literal_eval(_order.shop_list)
    shop_list = []

    for i in shop_list_id:
        shop_obj = models.Shopping.objects.get(id = i['id'])
        shop_list.append({"name":shop_obj.name,"price":shop_obj.price,"num":i['num'],"image":literal_eval(shop_obj.myimage)[0]})

    respons = {'result': 'ok', 'msg': '查询成功',"order_list":{"shop_list":shop_list,"all_price":_order.price}}
    return JsonResponse(respons, json_dumps_params={'ensure_ascii': False})

# 用户查询订单 1待付款 2待发货 3待收货 4已完成
@require_POST
def find_order(request):
    if (tools.valida_cookies(request.POST,'user')) != True:
        return JsonResponse(return_nor_permi, json_dumps_params={'ensure_ascii': False})

    login_user = request.POST['user_data[login_user]'] ##用户id
    order_status = request.POST['order_status']        ##订单状态
    order_list = []
    Queried = models.Order.objects.filter(user_id=login_user,order_status=order_status)

    for i in Queried:
        dict_data = model_to_dict(i,fields=['first_image', 'harvest_type','price','first_add','harvest_type','evaluation'])
        dict_data['first_add'] = str(i.first_add)
        dict_data['id'] = str(i.id)
        order_list.append(dict_data)
    respons = {'result': 'ok', 'msg': '查询成功',"order_list":order_list}
    return JsonResponse(respons, json_dumps_params={'ensure_ascii': False})

# #用户删除订单接口
@require_POST
def del_myorder(request):
    if (tools.valida_cookies(request.POST,'user')) != True:
        return JsonResponse(return_nor_permi, json_dumps_params={'ensure_ascii': False})
    
    order_id  = request.POST['order_id']
    models.Order.objects.get(id=order_id).delete()
    respons = {'result': 'ok', 'msg': '删除成功'}
    return JsonResponse(respons, json_dumps_params={'ensure_ascii': False})

#用户付款成功接口
@require_POST
def pay_myorder(request):
    if (tools.valida_cookies(request.POST,'user')) != True:
        return JsonResponse(return_nor_permi, json_dumps_params={'ensure_ascii': False})
    
    order_id  = request.POST['order_id']
    models.Order.objects.filter(id=order_id).update(order_status=2)
    respons = {'result': 'ok', 'msg': '支付成功'}
    return JsonResponse(respons, json_dumps_params={'ensure_ascii': False})


#用户确认收货
@require_POST
def harvest_myorder(request):
    if (tools.valida_cookies(request.POST,'user')) != True:
        return JsonResponse(return_nor_permi, json_dumps_params={'ensure_ascii': False})
    
    order_id  = request.POST['order_id']
    models.Order.objects.filter(id=order_id).update(order_status=0)
    respons = {'result': 'ok', 'msg': '收货成功'}
    return JsonResponse(respons, json_dumps_params={'ensure_ascii': False})

#获取一条公告
@require_POST
def get_a_announcement(request):
    announcement = models.Announcement.objects.get().content
    respons = {'result': 'ok', 'msg': '获取成功','content':announcement}
    return JsonResponse(respons, json_dumps_params={'ensure_ascii': False})

#用户申请退换货
#/4申请退货/5退货成功  /6申请换货/7换货成功
@require_POST
def refunds_exchanges(request):
    if (tools.valida_cookies(request.POST,'user')) != True:
        return JsonResponse(return_nor_permi, json_dumps_params={'ensure_ascii': False})

    order_id  = request.POST['order_id']
    return_type = request.POST['return_type']
    print(order_id)

    try:
        find_obj = models.Order.objects.filter(id=order_id,order_status=0)
        if(find_obj.count() == 0):
            respons = {'result': 'error', 'msg': '请求异常'}
        elif(return_type == "return"):
            find_obj.update(order_status=4)
            respons = {'result': 'ok', 'msg': '退货审核中'}
        elif(return_type == "exchanges"):
            find_obj.update(order_status=6)
            respons = {'result': 'ok', 'msg': '换货审核中'}
            
    except:
        respons = {'result': 'error', 'msg': '异常'}
    return JsonResponse(respons, json_dumps_params={'ensure_ascii': False})

#用户取消退货
@require_POST
def cancel_refunds(request):
    if (tools.valida_cookies(request.POST,'user')) != True:
        return JsonResponse(return_nor_permi, json_dumps_params={'ensure_ascii': False})
    order_id  = request.POST['order_id']
    models.Order.objects.filter(id=order_id,order_status=4).update(order_status=0)
    respons = {'result': 'ok', 'msg': '修改成功'}
    return JsonResponse(respons, json_dumps_params={'ensure_ascii': False})

#用户取消换货
@require_POST
def cancel_exchanges(request):
    if (tools.valida_cookies(request.POST,'user')) != True:
        return JsonResponse(return_nor_permi, json_dumps_params={'ensure_ascii': False})
    order_id  = request.POST['order_id']
    models.Order.objects.filter(id=order_id,order_status=6).update(order_status=0)
    respons = {'result': 'ok', 'msg': '修改成功'}
    return JsonResponse(respons, json_dumps_params={'ensure_ascii': False})

@require_POST
def add_evaluation(request):
    if (tools.valida_cookies(request.POST,'user')) != True:
        return JsonResponse(return_nor_permi, json_dumps_params={'ensure_ascii': False})
    order_id  = request.POST['order_id']
    detail = request.POST['detail']

    order_obj = models.Order.objects.filter(id=order_id)
    if(len(order_obj[0].evaluation) == 0):
        order_obj.update(evaluation=detail)
        respons = {'result': 'ok', 'msg': '发布成功'}
    else:
        respons = {'result': 'error', 'msg': '异常'}
    return JsonResponse(respons, json_dumps_params={'ensure_ascii': False})

#获取用户个人信息
@require_POST
def get_userinfo(request):
    if (tools.valida_cookies(request.POST,'user')) != True:
        return JsonResponse(return_nor_permi, json_dumps_params={'ensure_ascii': False})
    
    login_user = request.POST['user_data[login_user]']
    find_info = models.User.objects.get(userphone=login_user)
    user_info = model_to_dict(find_info,fields=['username','user_qq','user_gender','contact_number','delivery_address'])
    print(find_info.username)
    respons = {'result': 'ok', 'msg': '获取成功','user_info':user_info}
    return JsonResponse(respons, json_dumps_params={'ensure_ascii': False})

#修改个人信息
@require_POST
def modify_userinfo(request):
    if (tools.valida_cookies(request.POST,'user')) != True:
        return JsonResponse(return_nor_permi, json_dumps_params={'ensure_ascii': False})

    username = request.POST['user_info[username]']
    user_qq= request.POST['user_info[user_qq]'] 
    user_gender= request.POST['user_info[user_gender]'] 
    contact_number= request.POST['user_info[contact_number]'] 
    delivery_address= request.POST['user_info[delivery_address]']  
    login_user = request.POST['user_data[login_user]'] 
    
    models.User.objects.filter(userphone=login_user).update(username=username,user_qq=user_qq,user_gender=user_gender,contact_number=contact_number,delivery_address=delivery_address)
    respons = {'result': 'ok', 'msg': '修改成功'}
    return JsonResponse(respons, json_dumps_params={'ensure_ascii': False})

