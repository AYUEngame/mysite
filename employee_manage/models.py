from django.db import models


# Create your models here.
class Department(models.Model):
    # 部门表 verbose_name==对列名注解
    title = models.CharField(verbose_name='部门名', max_length=32)
    '''通过__str__(self)返回获取的对象中的某个值，很重要'''

    def __str__(self):
        return self.title


class Userinfo(models.Model):
    """员工表"""
    name = models.CharField(verbose_name='姓名', max_length=16)
    '''性别只有两个选择,在django中做约束'''
    sex_choices = (
        (1, '男'),
        (2, '女'),
    )
    sex = models.SmallIntegerField(verbose_name='性别', choices=sex_choices)
    age = models.IntegerField(verbose_name='年龄')
    password = models.CharField(max_length=64, verbose_name='用户密码')
    account = models.DecimalField(verbose_name='账户余额', max_digits=10, decimal_places=2, default=0)
    '''整数部分最多10位，小数部分最多2位，默认0'''
    creat_time = models.DateField(verbose_name='入职时间')
    # 无约束
    # depart_id = models.BigIntegerField(verbose_name='部门ID')

    # 1.有约束
    # -to 确定关联的表
    # -to_filed 关联的列名
    # 2. -此时django写的depart 生成数据列时位depart_id
    # 3. -部门表被删除 # 员工对应的部门id和部门一一对应，需要约束
    # ##3.1级联删除
    depart = models.ForeignKey(to='Department', to_field='id', on_delete=models.CASCADE)
    # ##3.2 置空
    #  depart = models.ForeignKey(to='Department', to_field='id', null=True, blank=True,on_delete=models.SET_NULL)


class AdminInfo(models.Model):
    name = models.CharField(verbose_name='用户名', max_length=16)
    admin = models.CharField(verbose_name='账号', max_length=16)
    password = models.CharField(verbose_name='密码', max_length=16)
