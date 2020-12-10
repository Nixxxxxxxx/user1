import json

from django.http import HttpResponse, JsonResponse, response
from django.shortcuts import render, redirect
from django.views import View

from user.models import Register
# Create your views here.


def login(request):
    """用户登录"""
    username = request.session.get('username', '')

    if username:
        # username 在 session 中存在，则用户已登录
        return HttpResponse('%s用户已登录' % username)

    if request.method == 'GET':
        return render(request, 'login.html')
    else:
        # 判断客户输入的账号和密码和数据库里面的是否一样，返回登录成功或者失败
        username = request.POST.get('username')
        password = request.POST.get('password')
        remember = request.POST.get('remember')
        try:
            Register.objects.get(username=username, password=password)

        except Register.DoesNotExist:
            return JsonResponse({"message": "Not find"})
        else:
            # 客户登录，账户密码正确，设置session
            request.session['user_id'] = Register.id
            request.session['username'] = Register.username

            if remember != 'true':
                # 标识不记住登录浏览器，关闭就删除session
                request.session.set_expiry(0)

            return JsonResponse({"message": "success"})


def view_info(request, id):
    # 通过id在数据库里面找到客户的数据，通过json返回给客户端
    try:
        user = Register.objects.get(id=id)   # 从数据库里面获取id=1的客户所有字段信息
    except Register.DoesNotExist:
        return JsonResponse({'message': '用户不存在'})
    else:
        user_dict = {
            'username': user.username,
            'password': user.password,
            'gender': user.gender,
            'age': user.age,
            'user_id': user.id,
        }
    return JsonResponse(user_dict)


class RegisterView(View):
    def get(self, request):
        """客户注册信息，并且把信息保存到数据库里面"""
        if request.method == 'GET':
            return render(request, 'register.html')

    def post(self, request):
        # 如果客户post访问，把json信息保存到数据库，并且返回注册成功
        # 如果传入的是表单，json转换格式不认识
        res_dict = json.loads(request.body)
        username = res_dict.get('username')
        password = res_dict.get('password')

        # 把客户信息保存到数据库
        user_msg = Register.objects.create(username=username, password=password)
        # 注册成功，重定向到登录页面
        return HttpResponse('<h1>注册成功，欢迎成为王二狗网站的一员<h1/>')
