lst = [1, 2, 3]

def foo(name, *arg):
    print(arg)

foo('bane', *lst)