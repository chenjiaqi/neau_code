# 定义一个变量message，赋值为"Hello world !"
message = "Hello world !"

# 打印变量message的值
print(message)

message = 1234567
print(message)

# message 变量的值被改变
message = 1.234567
print(message)

_mesage = 123
message_1 = 123

# 第一种， 双引号包含
message = "Hello world !"

# 第二种， 单引号包含
message = "Hello world !"

# 第三种， 三引号包含
message = """
        Hello world !
        Hello world !
"""

print(message)

# 求字符串长度

message = "hello world !"

print(message, ' 长度是:', len(message))

# 字符串 title 方法
message = "hello world !"
print(message.title())

print(message.split(' '))

message = "hello,world !"
print(message.split(','))

message = "Hello,world !"
print(message.upper())

print(message.lower())
message.expandtabs


# 使用format 来优化值一样代码
# 优化前
print(message, ' 长度是:', len(message))

# 使用format 来优化值一样代码
print('{} 长度是: {}'.format(message, len(message)))

# 使用f-string 来优化值一样代码,更加符合人的阅读习惯
print(f'{message} 长度是: {len(message)}')

# 字符串的拼接
'''
first_name = "ada"
last_name = "lovelace"

print(first_name + " " + last_name)
'''

num_of_students = 30

temperature = 36.6

# + - * /
print(1 + 2)
print(1 - 2)
print(1 * 2)
print(1 / 2)
#
print(10 ** 6)
# 关于溢出 32 位系统，最大值是 2 ** 31 - 1
print(2 ** 31)
print(10 * 1000000000000000000000000000)






