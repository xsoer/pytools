import argparse

parser = argparse.ArgumentParser(description='字节转换器')


# Add argument
parser.add_argument('--version', '-v', action='version',
                    version='%(prog)s version: v 0.0.1',
                    help='show the version')
parser.add_argument('--debug', '-d',
                    action='store_true',
                    help='show the version',
                    default=False)

group = parser.add_mutually_exclusive_group()
group.add_argument('-b', type=int, help='bytes', dest='b')
group.add_argument('-k', type=int, help='Kb', dest="k")
group.add_argument('-m', type=int, help='Mb', dest="m")
group.add_argument('-g', type=int, help='Gb', dest="g")
group.add_argument('-t', type=int, help='Tb', dest="t")

arg = parser.parse_args()

def trans():
    if arg.b:
        v = arg.b
        print(f'{v / 2**10} Kb')
        print(f'{v / 2**20} Mb')
        print(f'{v / 2**30} Gb')
        print(f'{v / 2**40} Tb')
    elif arg.k:
        v = arg.k
        print(f'{v * 2**10} bytes')
        print('{0:.2f} Mb'.format(v / 2**10 ))
        print(f'{v / 2**20} Gb')
        print(f'{v / 2**30} Tb')
    elif arg.m:
        v = arg.m
        print(f'{v * 2**20 :2f} bytes')
        print(f'{v * 2**10} Kb')
        print(f'{v / 2**10} Gb')
        print(f'{v / 2**20} Tb')
    elif arg.g:
        v = arg.g
        print(f'{v * 2**30} bytes')
        print(f'{v * 2**20} Kb')
        print(f'{v * 2**10} Mb')
        print(f'{v / 2**10} Tb')
    elif arg.t:
        v = arg.t
        print(f'{v * 2**40} bytes')
        print(f'{v * 2**30} Kb')
        print(f'{v * 2**30} Mb')
        print(f'{v * 2**10} Tb')

trans()
# %%
# help(argparse)
# print(argparse.__dict__)

# %%
