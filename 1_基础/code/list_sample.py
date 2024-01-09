# 定义一个列表
student_names = ["张三", "李四", "王五", "赵六", "钱七"]
print(student_names)

# 在数组中间指定位置增加一个元素
print(" * 加之后")
student_names.insert(0, "孙八")
print(student_names)

# 在数组末尾增加一个元素 append
print(" * 加之后", "周九")
student_names.append("周九")
print(student_names)


# 删除数组中的元素
print(" * 删除第一个元素")
del student_names[0]
print(student_names)

# 修改数组中的元素
student_names[0] = "张三三"
print(student_names)

# 访问数组中的元素 for  in
for name in student_names:
    print(f"你好,{name}")

# 用下标访问数组中的元素
for i in range(0, len(student_names)):
    print(f"你好,{student_names[i]}")

# range(start, stop, increment)
for i in range(0, 10, 3):
    print(i)

print(student_names)

# 判断,只想给张三三打招呼
for name in student_names:
    if name == "张三三":
        print(f"你好,{name}")
    elif name == "李四":
        print(f"你好,{name}")
    else:
        pass


greet_names = ["张三三", "李四", "王五"]
for name in student_names:
    if name in greet_names:
        print(f"你好,{name}")
    else:
        pass
# not 和if 一起使用
# 给除了周九之外的同学打招呼
print("------------------------------")
for name in student_names:
    if not name == "周九":
        print(f"你好,{name}")

# index 是负的
print("-1 坐标:", student_names[-1])
print("-2 坐标:", student_names[-2])

# print("坐标:", student_names[100])

# 切片 slice    [min_index,max_index)
print(student_names)
print(student_names[1:3])
