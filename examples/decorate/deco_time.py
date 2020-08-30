import time

"""函数运行时间装饰器
"""
def deco_time(func,*args,**kwargs):
    def wrapper(*args,**kwargs):
        start = time.time()
        result = func(*args,**kwargs)
        end = time.time()
        print(f'{func.__name__}运用时间：', end - start)
        return result
    return wrapper
