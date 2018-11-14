#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#第一行注释是为了告诉Linux/OS X系统，这是一个Python可执行程序，Windows系统会忽略这个注释；
#第二行注释是为了告诉Python解释器，按照UTF-8编码读取源代码，否则，你在源代码中写的中文输出可能会有乱码。

print('ABC'.encode('ascii'))
print('中文'.encode('utf-8'))
print("----------------")
#Traceback (most recent call last):
#  File ".\编码格式.py", line 3, in <module>
#    print( '中文'.encode('ascii'))
#UnicodeEncodeError: 'ascii' codec can't encode characters in position 0-1: ordinal not in range(128)
# code :::::::print( '中文'.encode('ascii'))
print(b'\xe4\xb8\xad\xe6\x96\x87'.decode('utf-8'))
# 如果有错误，可以添加ignore
print(b'\xe4\xb8\xad\xe6\x96'.decode('utf-8',errors='ignore'))
print("----------------")
#字符计算
print(len('ABC'))
print(len('中文'))
#字节计算，需要先转成byte
print(len(b'ABC'))
print(len("中文".encode("utf-8")))
print("------------------")
#格式化输出
print( 'Hi, %s, you have $%d.' % ('Michael', 1000000))
#另一种格式化输出
print('Hello, {0}, 成绩提升了 {1:.1f}%'.format('小明', 17.125))
