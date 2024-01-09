# 字典dict
# 字典是一种可变容器模型，且可存储任意类型对象。名字到体重的映射,单位KG
students = {"Tom": 90, "Jerry": 80, "Jack": 70}
print(students)

# 增加一个元素
students["Marry"] = 60
print(students)

# 访问Tom的体重
print(f'Tom 的体重是{students["Tom"]} KG')

# 如果key不存在导致程序的崩溃
# print(f'Tomm 的体重是{students["Tomm"]} KG')
# print(students.get('Tomm'))

# 借助if 进行判断
if students.get("Tomm") is None:
    print("Tomm 不存在")

print(students)

# 删除一个元素
del students["Tom"]
print(students)

# 修改一个元素
students["Marry"] = 99
print(students)

# 遍历字典

print("------------------------")
# 遍历key
for name in students.keys():
    print(name)
# 遍历 value
print("------------------------")

for age in students.values():
    print(age)

print("------------------------")
# k,v一起返回

for name, height in students.items():
    print(f"{name} 的体重是:{height } kg")

# 删除dict 中的某一个元素
print("------------------------")
print(students)
students.pop("Jerry")
del students["Jack"]
print(students)
