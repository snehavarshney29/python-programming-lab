def func1(i):
    return i/0
def func2():
    raise Exception("raising exception")
def func3():
    try:
        func1(5)
    except Exception as e:
        print(e)
    try:
        func2()
    except Exception as e:
        print(e)
    func3()
            
