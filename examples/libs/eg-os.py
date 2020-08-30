import os

def test():
    result = os.popen('ls')
    res = result.read()
    for line in res.splitlines()[6:]:
        # print(line, line.rstrip(".7z"))
        print(line, os.path.splitext(line)[0])
        

test()