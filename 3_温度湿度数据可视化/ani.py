import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from counterfit_connection import CounterFitConnection

from humidity_sensor import HumiditySensor
from soil_moisture_sensor import SoilMoistureSensor


CounterFitConnection.init("127.0.0.1", 5000)

ts = []
ss = []


# define canvas
fig, ax = plt.subplots()

line = ax.plot([], [], lw=2)[0]
line.set_color("red")

line2 = ax.plot([], [], lw=5)[0]
line2.set_color("blue")


def update(frame):
    h = HumiditySensor(CounterFitConnection, 0)
    ts.append(h.humidity)

    s = SoilMoistureSensor(CounterFitConnection, 1)
    ss.append(s.soil_moisture)

    ax.set_xlim(0, len(ts))
    ax.set_ylim(0, 100)

    x = [i for i in range(len(ts))]

    line.set_data(x, ts)

    line2.set_data(x, ss)
    return line


ani = FuncAnimation(fig, update, frames=np.linspace(0, 200, 201), interval=100)
plt.show()
