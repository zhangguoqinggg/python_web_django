def foo1(func):
    print("d1")

    def inner1():
        print("inner1")
        return "<i>{}</i>".format(func())

    return inner1


def foo2(func):
    print("d2")

    def inner2():
        print("inner2")
        return "<b>{}</b>".format(func())

    return inner2


@foo1
@foo2
def f1():
    return "Hello Andy"

# f1 = foo2(f1)  ==> print("d2") ==> f1 = inner2
# f1 = foo1(f1)  ==> print("d1") ==> f1 = foo1(inner2) ==> inner1

ret = f1()  # 调用f1() ==> inner1()  ==> <i>inner2()</i>  ==> <i><b>inner1()</b></i> ==> <i><b>Hello Andy</b></i>
print(ret)