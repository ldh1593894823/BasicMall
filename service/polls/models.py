from django.db import models

# Create your models here.


# 超级管理员
class Adminster(models.Model):
    username = models.CharField(max_length=32)  # 用户名
    password = models.CharField(max_length=32)  # 密码

# 普通用户


class User(models.Model):
    username = models.CharField(max_length=32)  # 用户名
    password = models.CharField(max_length=32)  # 密码
    userphone = models.CharField(max_length=32)  # 手机号登录用
    user_qq = models.CharField(max_length=32)  # 用户qq号码

# 商品详情


class Shopping(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=64)  # 商品名称
    price = models.CharField(max_length=32)  # 商品价格
    num = models.CharField(max_length=32)  # 商品库存
    category = models.CharField(max_length=32)  # 商品分类
    main_img = models.CharField(max_length=200)  # 商品主图
    detal_img = models.CharField(max_length=2000)  # 商品详情页图片
