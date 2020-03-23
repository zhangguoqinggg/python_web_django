#既不想 直接修改原来的函数，也不想修改函数的调用方式，还要增加新功能
#https://www.cnblogs.com/liwenzhou/p/9878885.html
def create_people():
        print('女娲真厉害，一口气造一个人')

def a(func):
    def b():
        print('加点水')
        func()
    return b

create_people =   a(create_people)

create_people()