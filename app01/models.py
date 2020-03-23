from django.db import models
# python manage.py makemigrations
# python manage.py migrate
# Create your models here.
# django2.2与mysql5.0 不兼容

#用户表
class UserInfo(models.Model):
    id = models.AutoField(primary_key=True)#在数据库中生成自增的ID主键字段
    username = models.CharField(max_length=20) #varchar(20)
    password = models.CharField(max_length=20) #varchar(20)


#出版社表
class Publisher(models.Model):
    id = models.AutoField(primary_key=True)#在数据库中生成自增的ID主键字段
    name = models.CharField(max_length=20)
    def __str__(self):
            return self.name

#书籍表
class Book(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=20)
    publisher = models.ForeignKey(to='Publisher',on_delete=models.CASCADE)#on_delete=True不清楚为什么我这个是需要加的  外键关联导致的
    def __str__(self):
            return '《'+self.title+'》'

#作者
class Author(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=20)
    age = models.IntegerField()
    book = models.ManyToManyField(to='Book')
    def __str__(self):
        return  self.name

# class Author2Book(models.Model):
#     id = models.AutoField(primary_key=True)
#     author_id = models.ForeignKey(to='Author',on_delete=True)#
#     book_id =models.ForeignKey(to='Book',on_delete=True)#
#     def __str__(self):
#         return  self.name
