class SoilMoistureSensor:
    def __init__(self, connection, port) -> None:
        self.connection = connection
        self.port = port

    # 定义一个方法，用来获取土壤湿度
    @property
    def soil_moisture(self):
        return self.connection.get_sensor_float_value(self.port)
