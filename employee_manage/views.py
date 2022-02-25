from django.shortcuts import render, redirect
from employee_manage import models
from django import forms

# Create your views here.
'''部门列表'''


def depart_list(request):
    '''去数据库中查询all()'''
    # 封装对象列表
    depart_data = models.Department.objects.all()
    return render(request, 'depart_list.html', {'depart_data': depart_data})


def depart_add(request):
    '''新增部门'''
    if request.method == "GET":
        return render(request, 'depart_add.html')
    '''获取返回得新建部门名'''
    depart_title = request.POST.get("title")
    # print("test", depart_title)
    # print("method:", request.method)

    # 创建数据库表中元素
    models.Department.objects.create(title=depart_title)
    # 重定向回列表页面
    return redirect("/depart/list/")


def depart_delete(request):
    '''删除部门'''
    # 根据id删除
    nid = request.GET.get('nid')
    models.Department.objects.filter(id=nid).delete()
    return redirect("/depart/list/")


def depart_edit(request, nid):
    '''编辑部门'''
    if request.method == "GET":
        # 根据 id获取当前默认部门
        edit_data = models.Department.objects.filter(id=nid).first()
        # print("test", edit_data.id, edit_data.title)
        # 把edit_data当作参数传递到edit.html文件
        return render(request, 'depart_edit.html', {"edit_data": edit_data})
    update_title = request.POST.get("title")
    # print("test", update_title)
    # print("nid", nid)
    models.Department.objects.filter(id=nid).update(title=update_title)
    return redirect("/depart/list/")


def user_list(request):
    '''去数据库中查询all()'''
    # 封装对象列表
    user_data = models.Userinfo.objects.all()
    return render(request, 'user_list.html', {'user_data': user_data})


class UserModelForm(forms.ModelForm):
    '''重写列名 ，增添校验'''

    # name = forms.CharField(min_length=3, label="xxx")

    class Meta:
        '''直接获取定义的表中所有列名，并可以field选择'''
        model = models.Userinfo
        fields = ["name", "password", "age", "account", "creat_time", "sex", "depart"]
        '''利用widgets插件 额外添加html属性 类型为字典'''
        widgets = {
            #     "name":forms.TextInput(attrs={"class":"form-control"}),
            #     "age":forms.TextInput(attrs={"class":"form-control"}),
            # "password": forms.PasswordInput(attrs={"class": "form-control"})
        }

        '''重新定义init方法'''

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for name, field in self.fields.items():
            # if name == "password":
            #     continue
            # else:
            field.widget.attrs = {"class": "form-control", "placeholder": field.label}


# **********
def user_add(request):
    ''' 添加用户 '''
    if request.method == 'GET':
        form = UserModelForm()
        return render(request, 'user_add.html', {"form": form})
    # 用POST提交数据时，数据校验
    form = UserModelForm(data=request.POST)  # 获取所有post提交上来的数据
    if form.is_valid():  # 进行校验，合法保存到数据库
        form.save()
        return redirect("/user/list/")
    else:
        '''在form里也封装了所有错误信息'''
        return render(request, 'user_add.html', {"form": form})


def user_delete(request, nid):
    '''删除用户'''
    # 根据id删除
    models.Userinfo.objects.filter(id=nid).delete()
    return redirect("/user/list/")


def user_edit(request, nid):
    '''编辑用户'''
    edit_data = models.Userinfo.objects.filter(id=nid).first()
    if request.method == "GET":
        # 根据 id获取当前默认用户
        # edit_data = models.Department.objects.filter(id=nid).first()
        '''默认显示instance实例'''
        form = UserModelForm(instance=edit_data)
        return render(request, 'user_edit.html', {"form": form})
    # method=="POST"
    # edit_data=models.Userinfo.objects.filter(id=nid).first()
    # 获取所有post提交上来的数据,且有默认数据的情况下是在原数据基础上做更新
    form = UserModelForm(data=request.POST, instance=edit_data)

    if form.is_valid():  # 进行校验，合法保存到数据库
        form.save()
        return redirect("/user/list/")
    else:
        '''在form里也封装了所有错误信息'''
        return render(request, 'user_edit.html', {"form": form})


# **********
def login(request):
    ''' 登录界面 '''
    # 用POST提交数据时，数据校验
    form = UserModelForm(data=request.POST)  # 获取所有post提交上来的数据
    if form.is_valid():  # 进行校验，合法保存到数据库
        '''再比较和数据库管理员账户是否一致'''
        return redirect("/depart/list/")
    else:
        '''在form里也封装了所有错误信息'''
        return render(request, 'login.html', {"form": form})


# **************

'''管理员函数'''


class AdminModelForm(forms.ModelForm):
    '''新增密码确认，且以密码形式输入 ，增添校验'''
    confirm_pass = forms.CharField(label="确认密码", widget=forms.PasswordInput)

    # name = forms.CharField(min_length=3, label="xxx")

    class Meta:
        '''直接获取定义的表中所有列名，并可以field选择'''
        model = models.AdminInfo
        fields = ["name", "admin", "password", "confirm_pass"]
        '''利用widgets插件 额外添加html属性 类型为字典'''
        widgets = {
            #         "name":forms.TextInput(attrs={"class":"form-control"}),
            #          "age":forms.TextInput(attrs={"class":"form-control"}),
            "password": forms.PasswordInput(attrs={"class": "form-control"})
        }

        '''重新定义init方法'''

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for name, field in self.fields.items():
            # if name == "password":
            #     continue
            # else:
            field.widget.attrs = {"class": "form-control", "placeholder": field.label}
    # 定义一个钩子来获取字典里的数据(视频方法)
    # def __init__(self):
    #     print(self.cleaned_data.get(""))
    #     return ""


def admin_list(request):
    '''去数据库中查询all()'''
    # 封装对象列表
    admin_data = models.AdminInfo.objects.all()
    return render(request, 'admin_list.html', {'admin_data': admin_data})


def admin_delete(request, nid):
    '''删除管理员'''
    # 根据id删除
    models.AdminInfo.objects.filter(id=nid).delete()
    return redirect("/admin/list/")


def admin_add(request):
    ''' 添加管理员 '''
    if request.method == 'GET':
        form = AdminModelForm()
        return render(request, 'admin_add.html', {"form": form})
    # 用POST提交数据时，数据校验
    # 获取所有post提交上来的数据
    form = AdminModelForm(data=request.POST)
    if form.is_valid() and form.cleaned_data.get("confirm_pass") == form.cleaned_data.get("password"):
        # 进行校验，合法保存到数据库and两次密码输入一致
        '''form.cleaned_data 以字典形式包含所有post数据'''
        # print(form.cleaned_data)
        form.save()
        return redirect("/admin/list/")
    else:
        '''在form里也封装了所有错误信息'''
        return render(request, 'user_add.html', {"form": form})


def admin_edit(request, nid):
    '''编辑管理员信息'''
    edit_data = models.AdminInfo.objects.filter(id=nid).first()
    if request.method == "GET":
        # 根据 id获取当前默认用户
        # edit_data = models.Department.objects.filter(id=nid).first()
        '''默认显示instance实例'''
        form = AdminModelForm(instance=edit_data)
        return render(request, 'admin_edit.html', {"form": form})
    # method=="POST"
    # edit_data=models.Userinfo.objects.filter(id=nid).first()
    # 获取所有post提交上来的数据,且有默认数据的情况下是在原数据基础上做更新
    form = AdminModelForm(data=request.POST, instance=edit_data)

    if form.is_valid() and form.cleaned_data.get("confirm_pass") == form.cleaned_data.get("password"):  # 进行校验，合法保存到数据库
        form.save()
        return redirect("/admin/list/")
    else:
        '''在form里也封装了所有错误信息'''
        return render(request, 'admin_edit.html', {"form": form})






