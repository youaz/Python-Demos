# 包含yield关键字，就变成了生成器函数
# 调用函数并不会执行语句
def foo():
    print('Starting.....')
    res = 0
    while True:
        # res = yield 4
        res = 4
        print("before yield, res:", res)
        res = yield res
        print("after yield, res:", res)


# 下面调用函数并没有执行，可以先将后面的语句注释掉, 逐行运行代码观察效果
g = foo()

print("第一次调用执行结果：")
print(next(g))
print("*" * 50)

print("第二次调用执行结果：")
x = g.send(7)
print(x)

print("第三次调用执行结果：")
print(next(g))
print("*" * 50)
