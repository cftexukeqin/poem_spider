import re

# 1 匹配手机号
# text = '18220568578'
# ret = re.match('1[3578]\d{9}',text)
# print(ret.group())

# 2 匹配邮箱
# text = 'cftyexuekqing@163.com'
# ret = re.match('\w+@\w+.\w+',text)
# print(ret.group())

# 3 url 匹配
# 注意，脱字符^ 在中括号中的含义是取反，在正常的字符串中是以后面的字符串开始的功能！
# text = 'http://sem.tanzhouedu.com/shiguang/it/python/pc-ty/'
# ret = re.match('(http|https|ftp)://[^\s]+',text)
# print(ret.group())

# 测试.
# text = '.'
# ret = re.match('\w',text)
# print(ret.group())

# 4 匹配1-100的数字
# 01不合法，101不合法
# 1位，2位，3位
# 问号表示匹配一个或者0个
# text = "100"
# ret = re.match('[1-9]\d?$|100$',text)
# print(ret.group())
# 贪婪和非贪婪
# 默认情况下是贪婪模式，也就是尽可能多的匹配，非贪婪模式，最后加？
# text = "<h1>title</h1>"
# ret = re.match('<.+?>',text)
# print(ret.group())

# group,分组

# text = "apple's price is $299,orange's price is $10"
# ret = re.search('.*(\$\d+).*(\$\d+)',text)
# group() 默认是等于group(0)
# group默认分组，groups()可以打印所有的结果
# print(ret.group())
# print(ret.group(0))
# print(ret.group(1))
# print(ret.group(2))
# print(ret.groups())
# print(ret.group(1,2))
