from polls import models
from django.http import JsonResponse
from script import gittoken
from django.views.decorators.http import require_POST ,require_GET
import json
from script import tools
import os
from django.forms.models import model_to_dict
from django.db.models import Q

return_nor_permi = {'result': 'not_permission', 'msg': '无权限',}

#管理员登录接口
@require_POST
def login_admin(request):
    respons = {}
    cookies = ''
    username = request.POST['username']
    password = request.POST['password']
    find_user = models.Adminster.objects.filter(username=username)
    if find_user and (find_user[0].password == password):
        cookies = gittoken.generate_token(
            (username[3]+password[3]), 3600)
        respons = {'result': 'ok', 'msg': '登录成功', 'cookies': cookies,'login_user':username,'user_type':'admin'}
    else:
        respons = {'result': 'error', 'msg': '用户名或密码错误', 'cookies': cookies}
    return JsonResponse(respons, json_dumps_params={'ensure_ascii': False})
 
#公告页面接口
class Announcement:
    #添加公告接口
    @require_POST
    def add_announcement(request):
        _title = request.POST['title']
        _content = request.POST['content']
        valida_status = tools.valida_cookies(request.POST,'admin')
        if(valida_status == False):
            return JsonResponse(return_nor_permi, json_dumps_params={'ensure_ascii': False})
        models.Announcement.objects.create(title=_title,content=_content)
        respons = {'result': 'ok', 'msg': '添加成功'}
        return JsonResponse(respons, json_dumps_params={'ensure_ascii': False})

    #删除公告接口
    @require_POST
    def del_announcement(request):
        valida_status = tools.valida_cookies(request.POST,'admin')
        if(valida_status == False):
            return JsonResponse(return_nor_permi, json_dumps_params={'ensure_ascii': False})
        models.Announcement.objects.filter(id=request.POST['id']).delete()
        respons = {'result': 'ok', 'msg': '删除成功'}
        return JsonResponse(respons, json_dumps_params={'ensure_ascii': False})

    #获取所有公告接口
    @require_POST
    def all_announcement(request):
        data_list = []
        find_list = models.Announcement.objects.all()
        for i in find_list:
            data_list.append({"title":i.title,"content":i.content,"id":i.id})
        respons = {'result': 'ok', 'msg': '查询成功',"comment_list":data_list}
        return JsonResponse(respons, json_dumps_params={'ensure_ascii': False})
    
#管理商品
class manage_shop:
    # 添加商品接口
    @require_POST
    def add_shop(request):
        respons = {}
        _shop_name     = request.POST['shop_name']  #商品名称
        _shop_price    = request.POST['shop_price'] #商品价格
        _shop_category = request.POST['shop_category'] #商品分类
        _shop_num      = request.POST['shop_num'] #商品库存
        _imageList     = request.POST['imageList'] #商品图片列表
        _imageList = json.loads(_imageList[1:])
        models.Shopping.objects.create(name=_shop_name,price=_shop_price,num=_shop_num,category=_shop_category,myimage=_imageList)
        respons = {'result': 'ok', 'msg': '添加成功',}
        return JsonResponse(respons, json_dumps_params={'ensure_ascii': False})


    # 删除商品接口
    @require_POST
    def del_shop(request):
        shop_id = request.POST['id']
        valida_status = tools.valida_cookies(request.POST,'admin')
        if(valida_status == False):
            return JsonResponse(return_nor_permi, json_dumps_params={'ensure_ascii': False})
        models.Shopping.objects.filter(id=shop_id).delete()
        respons = {'result': 'ok', 'msg': '删除成功',}
        return JsonResponse(respons, json_dumps_params={'ensure_ascii': False})
    
    # 修改商品接口
    @require_POST
    def modify_shop(request):
        valida_status = tools.valida_cookies(request.POST,'admin')
        if(valida_status == False):
            return JsonResponse(return_nor_permi, json_dumps_params={'ensure_ascii': False})
        shop_id = request.POST['id']
        detail_title = request.POST['detail_title']
        detail = request.POST['detail']
        try:
            if (detail_title == 'num'):
                models.Shopping.objects.filter(id=shop_id).update(num=detail)
            elif (detail_title == 'price'):
                models.Shopping.objects.filter(id=shop_id).update(price=detail)
            elif (detail_title == 'sales'):
                models.Shopping.objects.filter(id=shop_id).update(sales=detail)
            respons = {'result': 'ok', 'msg': '修改成功'}
            return JsonResponse(respons, json_dumps_params={'ensure_ascii': False})
        except:
            respons = {'result': 'error', 'msg': '修改失败',}
            return JsonResponse(respons, json_dumps_params={'ensure_ascii': False})
    
#请求方法为POST时，执行文件上传
@require_POST
def upload(request):
    respons = {}
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
    return JsonResponse(respons, json_dumps_params={'ensure_ascii': False})

#管理订单
class manage_order:
    #查询不同类型订单 
    #1待付款/2待发货/3待收货/0完成订单  /4申请退货/5退货成功  /6申请换货/7换货成功
    @require_POST
    def all_orders(request):
        if (tools.valida_cookies(request.POST,'admin')) != True:
            return JsonResponse(return_nor_permi, json_dumps_params={'ensure_ascii': False})
        order_status = int(request.POST['order_status'])

        order_list = []
        
        print(order_status)
        if(order_status == 10):
            print("查询所有")
            find_obj = models.Order.objects.filter(Q(order_status=4) | Q(order_status=5)| Q(order_status=6)| Q(order_status=7))
            print(find_obj.count())
        else:
            find_obj = models.Order.objects.filter(order_status=order_status)
        for i in find_obj:
            order_list.append({"user_id":i.user_id,"price":i.price,"image":i.first_image,"order_time":i.first_add,"id":i.id,"express_id":"","order_status":i.order_status,"harvest_type":i.harvest_type})
        respons = {'result': 'ok', 'msg': '查询成功', 'order_list': order_list}
        return JsonResponse(respons, json_dumps_params={'ensure_ascii': False})

    #管理员删除订单接口
    @require_POST
    def admin_del_order(request):
        if (tools.valida_cookies(request.POST,'admin')) != True:
            return JsonResponse(return_nor_permi, json_dumps_params={'ensure_ascii': False})
        
        order_id  = request.POST['order_id']
        models.Order.objects.get(id=order_id).delete()
        respons = {'result': 'ok', 'msg': '删除成功'}
        return JsonResponse(respons, json_dumps_params={'ensure_ascii': False})

    #管理员对订单进行发货
    @require_POST
    def deliver_goods(request):
        if (tools.valida_cookies(request.POST,'admin')) != True:
            return JsonResponse(return_nor_permi, json_dumps_params={'ensure_ascii': False})
        order_id = request.POST['order_id']
        express_id = request.POST['express_id']
        models.Order.objects.filter(id=order_id).update(express_id=express_id,order_status=3)
        respons = {'result': 'ok', 'msg': '发货成功'}
        return JsonResponse(respons, json_dumps_params={'ensure_ascii': False})

    #管理员审核订单退换货
    @require_POST
    def modify_order(request):
        if (tools.valida_cookies(request.POST,'admin')) != True:
            return JsonResponse(return_nor_permi, json_dumps_params={'ensure_ascii': False})
        order_id = request.POST['id']    
        order_type = request.POST['type']
        models.Order.objects.filter(id=order_id).update(order_status=int(order_type))
        respons = {'result': 'ok', 'msg': '审核成功'}
        return JsonResponse(respons, json_dumps_params={'ensure_ascii': False})

#查询评论订单
@require_POST
def find_evaluationed(request):
    if (tools.valida_cookies(request.POST,'admin')) != True:
        return JsonResponse(return_nor_permi, json_dumps_params={'ensure_ascii': False})

    order_list =[]
    find_obj = models.Order.objects.filter(order_status=0)
    for i in find_obj:
        if(len(i.evaluation)):
            order_list.append({"user_id":i.user_id,"price":i.price,"image":i.first_image,"evaluation":i.evaluation,"id":i.id,"express_id":"","order_status":i.order_status,"harvest_type":i.harvest_type})
    respons = {'result': 'ok', 'msg': '查询成功', 'order_list': order_list}
    return JsonResponse(respons, json_dumps_params={'ensure_ascii': False})

#删除评论订单
@require_POST
def del_evaluationed(request):
    if (tools.valida_cookies(request.POST,'admin')) != True:
        return JsonResponse(return_nor_permi, json_dumps_params={'ensure_ascii': False})
    
    order_id = request.POST['order_id']
    models.Order.objects.filter(id=order_id).update(evaluation="")
    respons = {'result': 'ok', 'msg': '删除成功'}
    return JsonResponse(respons, json_dumps_params={'ensure_ascii': False})