from deco_time import deco_time
import time

@deco_time
def test1(a,c):
    print('aaaaaa')
    time.sleep(3)
    print(a)
    time.sleep(1)
    for k,v in c.items():
        print(k,'--->',v)

@deco_time
def test2():
    print('bbbbb')
    time.sleep(2)

@deco_time
def test3(a='123',b='fasdfa'):
    print(a)
    time.sleep(2)
    print(b)

@deco_time
def test4(a={'ccc':888,'ddd':999},b='fasdfa'):
    print(a)
    time.sleep(2)
    print(b)

# test1(9999,{'aaa':123,'bbb':456})
# test2()
# test3('tttt','ggggg')
test4()