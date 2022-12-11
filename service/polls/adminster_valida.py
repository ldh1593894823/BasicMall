from polls import models
from django.http import JsonResponse
from script import gittoken
from django.views.decorators.http import require_POST ,require_GET
import json
from script import tools
import os

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

#添加公告接口
@require_POST
def add_announcement(request):
    _title = request.POST['title']
    _content = request.POST['content']
    valida_status = tools.valida_cookies(request.POST)
    if(valida_status == False):
        return JsonResponse(return_nor_permi, json_dumps_params={'ensure_ascii': False})
    models.Announcement.objects.create(title=_title,content=_content)
    respons = {'result': 'ok', 'msg': '添加成功'}
    return JsonResponse(respons, json_dumps_params={'ensure_ascii': False})

#删除公告接口
@require_POST
def del_announcement(request):
    valida_status = tools.valida_cookies(request.POST)
    if(valida_status == False):
        return JsonResponse(return_nor_permi, json_dumps_params={'ensure_ascii': False})
    models.Announcement.objects.filter(id=request.POST['id']).delete()
    respons = {'result': 'ok', 'msg': '删除成功'}
    return JsonResponse(respons, json_dumps_params={'ensure_ascii': False})

@require_POST
def all_announcement(request):
    data_list = []
    find_list = models.Announcement.objects.all()
    for i in find_list:
        data_list.append({"title":i.title,"content":i.content,"id":i.id})
    respons = {'result': 'ok', 'msg': '查询成功',"comment_list":data_list}
    return JsonResponse(respons, json_dumps_params={'ensure_ascii': False})
    

# 添加商品接口
@require_POST
def add_shop(request):
    respons = {}
    cookies = ''
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