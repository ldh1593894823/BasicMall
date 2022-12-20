from django.db import models
import uuid
from django.core.validators import validate_comma_separated_integer_list

# Create your models here.


# 超级管理员
class Adminster(models.Model): # 超级管理员
    username = models.CharField(max_length=32)  # 用户名
    password = models.CharField(max_length=32)  # 密码

#公告
class Announcement(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid1, editable=False)
    title = models.CharField(max_length=64) #公告标题
    content = models.CharField(max_length=128)  # 公告

# 普通用户
class User(models.Model): 
    username = models.CharField(max_length=32)  # 用户名
    password = models.CharField(max_length=32)  # 密码
    userphone = models.CharField(max_length=32)  # 手机号登录用
    user_qq = models.CharField(max_length=32)  # 用户qq号码

# 商品列表
class Shopping(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid1, editable=False)
    name = models.CharField(max_length=64)  # 商品名称
    first_add=models.DateTimeField(auto_now_add=True) #添加时间
    price = models.CharField(max_length=32)  # 商品价格
    num = models.CharField(max_length=32)        # 商品库存
    sales = models.CharField(max_length=32,default='0')      # 商品销量
    category = models.CharField(max_length=32)  # 商品分类
    myimage = models.CharField(max_length=256)  # 商品图片

#购物车
class Shop_cart(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid1, editable=False)
    user_id = models.CharField(max_length=64)  #用户手机号
    shop_num = models.IntegerField() #加购数量
    shop_id = models.CharField(max_length=64)  #商品id

#订单表
class Order(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid1, editable=False)
    user_id = models.CharField(max_length=32)     #用户id
    first_add=models.DateTimeField(auto_now_add=True) #创建时间
    price = models.CharField(max_length=16)       #最终价格
    shop_list = models.CharField(max_length=256)  #商品id列表
    order_status = models.IntegerField()  #订单状态  1未付款/2待发货/3待收货/0完成订单

    courier_name = models.CharField(max_length=16)  #收货人姓名
    courier_phone = models.CharField(max_length=16)  #收货人电话
    courier_place = models.CharField(max_length=64)  #收货人地址
