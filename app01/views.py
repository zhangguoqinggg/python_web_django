"""
专门存放函数的文件
"""
from django.shortcuts import HttpResponse,render,redirect
from app01.models import UserInfo,Publisher,Book,Author
from django import views
def index(request):
    return render(request,"index.html")

def login(request):
    error_msg = ''
    if request.method =='POST':
        email = request.POST['email']
        pwd = request.POST['pwd']
        #去数据库中以username 和password为条件去检索
        ret = UserInfo.objects.filter(username=email,password=pwd)
        if ret:
            return redirect('/index/')
        else:
            error_msg = '用户名或密码错误！！！'
    return render(request,"login.html" ,{'error_msg':error_msg})

def publisher_list(request):
    #1.把数据库中所有出版社信息取出来
    ret = Publisher.objects.all()

    #2.在页面上吧出版社数据显示出来
    #2.在页面上吧出版社数据显示出来
    return  render(request,"publisher_list.html" ,{'publisher_list':ret})
#添加出版社
def add_publisher(request):
    # 跳转到添加出版社界面，有form表单让用户添加数据
    if request.method =='POST':
        new_name = request.POST.get('publisher_name')
        Publisher.objects.create(name = new_name)
        return redirect('/publisher_list/')
    return render(request, "add_publisher.html")


def delete_publisher(request):
    delete_id = request.GET.get('id')
    Publisher.objects.filter(id= delete_id).delete()
    return redirect('/publisher_list/')

def update_publisher(request):
    if request.method =='POST':
        update_id = request.POST.get('id')
        update_name = request.POST.get('publisher_name')
        Publisher.objects.filter(id= update_id).update(name=update_name)
        return redirect('/publisher_list/')

    # 跳转到添加出版社界面，有form表单让用户添加数据
    update_id = request.GET.get('id')
    ret = Publisher.objects.get(id = update_id)

    return render(request, "update_publisher.html",{'obj' :ret})


def book_list(request):
    #1.找出数据库中所有的书籍
    book_list = Book.objects.all()
    all_publisher = Publisher.objects.all()
    return render(request,'book_list.html',{'book_list':book_list,'publisher_list':all_publisher})

def delete_book(request):
    #1.找出数据库中所有的书籍
    delete_id = request.GET.get('id')
    Book.objects.filter(id=delete_id).delete()
    return redirect('/book_list/')

def add_book(request):
    #1.获取书籍名称
    new_title = request.POST.get('title')
    #2.获取出版社信息
    publisher_id = request.POST.get('publisher')
    Book.objects.create(title=new_title,publisher_id=publisher_id)
    return redirect('/book_list/')


def update_book(request):
    update_book_id = request.GET.get('id')
    update_book_obj = Book.objects.get(id=update_book_id)
    # #1.获取书籍名称
    if request.method=='POST':
        new_title = request.POST.get('title')
        publisher_id = request.POST.get('publisher')
        update_book_obj.publisher_id = publisher_id
        update_book_obj.title=new_title
        update_book_obj.save()
        #return HttpResponse('123')
        return redirect('/book_list/')
    # #2.获取出版社信息
    all_publisher = Publisher.objects.all()
    return render(request,'update_book.html',{'book_obj':update_book_obj,'publisher_list':all_publisher})

def author_book(request):
    data = Author.objects.all()
    return render(request,'author_list.html',{'author_list' :data})



def add_author(request):

    if request.method == 'POST':
        new_author_name = request.POST.get('author_name')
        new_author_age = request.POST.get('author_age')
        #如果提交的是数据是一个列表（多选的数据要用getlist获取）
        book_id_list= request.POST.getlist('book')
        #创建一个新的作者
        #更新 作者与书籍之间 的关系
        author_obj = Author.objects.create(name=new_author_name,age= new_author_age)
        author_obj.book.add(*book_id_list)
        return redirect('/author_list/')
    all_book = Book.objects.all()
    return render(request,'add_author.html' ,{'book_list' : all_book})

def delete_author(request):
    #从url中 获取要删除作者ID
    author_id =  request.GET.get('id')
    #多对多关系表中的数据通过外键也会删除
    Author.objects.filter(id = author_id ).delete()
    return redirect('/author_list/')

def update_author(request):
    author_id = request.GET.get('id')
    author_obj = Author.objects.get(id=author_id)
    if request.method == 'POST':
        new_author_name = request.POST.get('author_name')
        new_author_age = request.POST.get('author_age')
        new_book_list = request.POST.getlist('book')

        author_obj.name = new_author_name
        author_obj.age = new_author_age
        author_obj.save()

        author_obj.book.set(new_book_list) #把作者关联书籍的值修改
        return  redirect('/author_list/')
    all_book = Book.objects.all()
    return render(request,'update_author.html' ,{'author' : author_obj,'book_list' : all_book})

class UploadView(views.View):
    def get(self,request):
        return render(request,'upload_file.html')
    def post(self,request):
        #获取文件name
        file_obj = request.FILES.get('file_name')
        file_name = file_obj.name
        # with open(file_name,'wb') as f:
        #     for i in file_obj:
        #         f.write(i)
        with open(file_name,'wb') as f:
            for chunk in file_obj.chunks():
                f.write(chunk)

        return HttpResponse('收到了!!!')



def json_data(request):
    d = {"name":"ljj","age":'18' ,'school':'北大'}
    from django.http import JsonResponse
    # 如果非要返回list 需要加上 safe = Fales
    # list_1 = [1,2,3,4]
    # return JsonResponse(list_1,safe=False)
    return JsonResponse(d)