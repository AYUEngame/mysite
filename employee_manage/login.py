from django.shortcuts import render, redirect
from employee_manage import models
from django import forms


class LoginModelForm(forms.ModelForm):
    class Meta:
        model = models.AdminInfo
        fields = ["admin", "password"]


'''因为不对数据库进行增删改查，可以继承form组件实现'''


# class LoginForm(forms.Form):
#     account = forms.CharField(lable="账户", required=True)
#     password = forms.CharField(lable="密码", required=True)

def LoginIn(request):
    print("11222211")
    # 用POST提交数据时，数据校验
    form = LoginModelForm(data=request.POST)  # 获取所有post提交上来的数据
    if form.is_valid():
        print("1111111111")
        account = form.cleaned_data.get("admin")
        password = form.cleaned_data.get("password")
        admin_object = models.AdminInfo.objects.filter(admin=account, password=password).first()
        '''数据库校验,filter里是定义的字典'''
        '''如果用户名和密码错误，admin_object为空'''
        if not admin_object:
            '''自动添加一个错误提示 '''
            print("test:xxxxx", admin_object)
            form.add_error("password", "用户名或密码错误")
            return render(request, 'login.html')

        return redirect("/admin/list/")
    return render(request,'login.html')
