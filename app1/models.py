from django.db import models


# Create your models here.
class User(models.Model):
    """用户信息表"""
    gender = (
        ('male', "男"),
        ('female', "女"),
    )
    usertype = (
        ('student', '学生'),
        ('teacher', '教师'),
    )

    name = models.CharField(max_length=20, verbose_name='姓名')
    username = models.CharField(max_length=20, unique=True, verbose_name='学号/工号', primary_key=True)
    password = models.CharField(max_length=20, verbose_name='密码')
    email = models.EmailField(unique=True, verbose_name='电子邮箱')
    qq = models.CharField(max_length=20, null=True, blank=True, verbose_name='QQ')
    tel = models.CharField(max_length=20, null=True, blank=True, verbose_name='手机')
    wechat = models.CharField(max_length=20, null=True, blank=True, verbose_name='微信')
    collage = models.CharField(max_length=20, verbose_name='学院')
    classname = models.CharField(max_length=20, null=True, blank=True, verbose_name='专业班级')
    sex = models.CharField(max_length=20, choices=gender, verbose_name='性别', default="男")
    usertype = models.CharField(max_length=20, choices=usertype, verbose_name='用户类型', default='学生')

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['username']
