class HumiditySensor:
    def __init__(self, connection, port) -> None:
        self.connection = connection
        self.port = port

    # 定义一个方法，用开表示湿度
    @property
    def humidity(self):
        return self.connection.get_sensor_float_value(self.port)
