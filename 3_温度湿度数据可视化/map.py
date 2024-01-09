import folium

# 定义经纬度信息
# 经度
latitude = 126.71
# 纬度
longitude = 45.74

# 创建地图对象并设置初始位置为指定经纬度
map_obj = folium.Map(location=[longitude, latitude], zoom_start=15)

# 添加标记点到地图上
marker = folium.Marker([longitude, latitude], popup="Hello World!")
map_obj.add_child(marker)

# locations = [[37.7749, -122.4194], [37.8049, -122.4294], [37.7849, -122.4094]]  # 示例路径点
# folium.PolyLine(locations=locations, color="red", weight=2.5).add_to(map_obj)

# 保存生成的HTML文件
map_obj.save("map.html")
