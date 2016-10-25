# coding=utf-8
import re

m = re.match(r'^(\d{3})-(\d{3,8})$', '010-12345')
print m
print m.group(0)
print m.group(1)
print m.group(2)
print m.groups()
print re.match(r'^(\d+)(0*)$', '102300').groups()
print re.match(r'^(\d+?)(0*)$', '102300').groups()

'''
当我们在Python中使用正则表达式时，re模块内部会干两件事情：

编译正则表达式，如果正则表达式的字符串本身不合法，会报错；

用编译后的正则表达式去匹配字符串。

如果一个正则表达式要重复使用几千次，出于效率的考虑，我们可以预编译该正则表达式，接下来重复使用时就不需要编译这个步骤了，直接匹配：
'''
re_telephone = re.compile(r'^(\d{3})-(\d{3,8})')
print re_telephone.match('010-12345').groups()
print re_telephone.match('020-9844').groups()
