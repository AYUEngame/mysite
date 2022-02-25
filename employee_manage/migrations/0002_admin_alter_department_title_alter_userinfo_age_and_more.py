# Generated by Django 4.0.2 on 2022-02-24 22:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee_manage', '0001_initial'),
    ]

    operations = [

        migrations.AlterField(
            model_name='department',
            name='title',
            field=models.CharField(max_length=32, verbose_name='部门名'),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='age',
            field=models.IntegerField(verbose_name='年龄'),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='password',
            field=models.CharField(max_length=64, verbose_name='用户密码'),
        ),
    ]