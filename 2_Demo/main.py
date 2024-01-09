from counterfit_connection import CounterFitConnection
from prettytable import PrettyTable

import time
import pynmea2


class ButtonSensor:
    def __init__(self, connection, port) -> None:
        self.connection = connection
        self.port = port

    # 定义一个方案，用来表示按钮是否被按下
    @property
    def is_pressed(self):
        return self.connection.get_sensor_boolean_value(self.port)


# 定义一个类，用来表示光线传感器
class LightSensor:
    def __init__(self, connection, port) -> None:
        self.connection = connection
        self.port = port

    # 定义一个方法，用来表示光线传感器的强度
    @property
    def light(self):
        return self.connection.get_sensor_int_value(self.port)


# 定义一个类，用来表示温度
class TemperatureSensor:
    def __init__(self, connection, port) -> None:
        self.connection = connection
        self.port = port

    # 定义一个方法，用来表示温度
    @property
    def temperature(self):
        return self.connection.get_sensor_float_value(self.port)


# 定义一个类，用来表示湿度
class HumiditySensor:
    def __init__(self, connection, port) -> None:
        self.connection = connection
        self.port = port

    # 定义一个方法，用开表示湿度
    @property
    def humidity(self):
        return self.connection.get_sensor_float_value(self.port)


# 定义一个类，用来表示土壤湿度
class SoilMoistureSensor:
    def __init__(self, connection, port) -> None:
        self.connection = connection
        self.port = port

    # 定义一个方法，用来获取土壤湿度
    @property
    def soil_moisture(self):
        return self.connection.get_sensor_float_value(self.port)


class LED:
    def __init__(self, connection, port) -> None:
        self.connection = connection
        self.port = port

    def on(self):
        self.connection.set_actuator_boolean_value(self.port, True)

    def off(self):
        self.connection.set_actuator_boolean_value(self.port, False)


class Relay:
    def __init__(self, connection, port) -> None:
        self.connection = connection
        self.port = port

    def activate(self):
        self.connection.set_actuator_boolean_value(self.port, True)

    def deactivate(self):
        self.connection.set_actuator_boolean_value(self.port, False)


class GPS:
    def __init__(self, connection, port) -> None:
        self.connection = connection
        self.port = port

    def location(self):
        line = self.connection.read_serial_sensor_line(self.port)
        x = pynmea2.parse(line)
        return x.longitude, x.latitude


class Controller:
    def __init__(self, url, port):
        self.url = url
        self.port = port

        self.connection = CounterFitConnection()
        self.connection.init(url, port)

        self.light_sensor = LightSensor(self.connection, 0)

        self.tempearture_sensor = TemperatureSensor(self.connection, 1)

        self.humidity_sensor = HumiditySensor(self.connection, 2)

        self.soil_moisture_sensor = SoilMoistureSensor(self.connection, 3)

        self.led = LED(self.connection, 4)

        self.relay = Relay(self.connection, 5)

    @property
    def light(self):
        return self.light_sensor.light

    @property
    def temperature(self):
        return self.tempearture_sensor.temperature

    @property
    def humidity(self):
        return self.humidity_sensor.humidity

    @property
    def soil_moisture(self):
        return self.soil_moisture_sensor.soil_moisture

    def showSensorStatus(self):
        header = ["光照强度", "温度", "湿度", "土壤湿度"]
        table = PrettyTable(header, encoding="utf8")
        table.add_row([self.light, self.temperature, self.humidity, self.soil_moisture])
        print(table)

    def run(self):
        while True:
            self.showSensorStatus()
            self.led.on()
            time.sleep(0.1)
            self.led.off()
            time.sleep(0.1)


if __name__ == "__main__":
    print("hello world")
    c = Controller("127.0.0.1", 5000)
    c.run()
    '''
    gps = GPS(c.connection, "/dev/ttyAMA0")
    while True:
        lat, lon = gps.location()
        print(lat, lon)
        time.sleep(1)
    '''
