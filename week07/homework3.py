from datetime import datetime

def timer(func):
    def func2(*args,**kwargs):
        print(f'func begin: {datetime.now()}')
        func(*args,**kwargs)
        print(f'func end: {datetime.now()}')
    return func2

@timer
def aaa(*args):
    str1=''
    for i in args:
        str1+=str(i)
    print(str1)

    
aaa('a','b','c')