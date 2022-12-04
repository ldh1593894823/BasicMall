from django.db import models
import uuid
from django.core.validators import validate_comma_separated_integer_list

# Create your models here.


# 超级管理员
class Adminster(models.Model): # 超级管理员
    username = models.CharField(max_length=32)  # 用户名
    password = models.CharField(max_length=32)  # 密码



# 普通用户
class User(models.Model): 
    username = models.CharField(max_length=32)  # 用户名
    password = models.CharField(max_length=32)  # 密码
    userphone = models.CharField(max_length=32)  # 手机号登录用
    user_qq = models.CharField(max_length=32)  # 用户qq号码

# 所有商品
class Shopping(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid1, editable=False)
    name = models.CharField(max_length=64)  # 商品名称
    first_add=models.DateTimeField(auto_now_add=True) #添加时间
    price = models.CharField(max_length=32)  # 商品价格
    num = models.CharField(max_length=32)        # 商品库存
    sales = models.CharField(max_length=32,default='0')      # 商品销量
    category = models.CharField(max_length=32)  # 商品分类
    myimage = models.CharField(max_length=256)  # 商品图片

