from django.db import models

# Create your models here.


class Register(models.Model):
    """创建模型表对应数据库，先模型迁移，在迁移"""
    username = models.CharField(max_length=10, verbose_name='用户名')
    password = models.CharField(max_length=128, verbose_name='密码')
    gender = models.IntegerField(default=0, verbose_name='性别')
    age = models.IntegerField(default=23, verbose_name='年龄')
    tel = models.CharField(max_length=11, null=True, verbose_name='用户名')

    class Meta:
        db_table = 'user_message'
        verbose_name = '用户信息表'
