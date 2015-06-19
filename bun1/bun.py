import time

print(time.asctime())

def hello(name):
    print(name + "さん、こんにちは")


import sys

print('お名前は？ ')
name = str(sys.stdin.readline()).strip()
hello(name)
